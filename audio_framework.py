import pyaudio
import numpy as np
import aubio
from scipy.signal import find_peaks
import time
import threading
import pygame.midi as midi
from mingus.containers import Note
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
import mingus.core.scales as scales
import mingus.core.notes as notes

main_notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

def get_pitch(signal):
    pitch_detector = aubio.pitch("default", 2048, 2048 // 2, 44100)
    pitch_detector.set_unit("Hz")
    pitch_detector.set_silence(-40)
    pitch = pitch_detector(signal)[0]
    return pitch

def pitch_to_note(pitch):
    # Define the standard pitches for each note
    standard_pitches = 440 * 2**((np.arange(12 * 8) - 57) / 12)
    
    # Find the nearest standard pitch
    pitch_index = np.abs(standard_pitches - pitch).argmin()
    
    # Map the pitch to the nearest musical note
    note = main_notes[pitch_index % 12]
    octave = pitch_index // 12 - 1
    
    return note + str(octave)
def match_note(target_note, duration, self, app):
    c = Note()
    c.from_int(target_note)
    self.quizText.setText(f'Listening for note: {c.name}')

    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32, channels=1, rate=44100, input=True, frames_per_buffer=2048)
    note_held_time = 0.0

    startTime = time.time()
    endTime = time.time()

    while True:
        if self.interruptListening:
            return False
        data = stream.read(1024, exception_on_overflow=False)
        signal = np.frombuffer(data, dtype=np.float32)
        pitch = get_pitch(signal)
        note = pitch_to_note(pitch)
        if pitch > 0:
            if note == c.name + str(c.octave):
                self.quizText.setText(f'Your last note was {note}. Keep going!')
                # print(f'Your last note was {note}. Keep going!')
                note_held_time += 1024/44100 # increment the note held time by the buffer length
                if note_held_time >= duration:
                    self.quizText.setText(f'You matched the note!')
                    # print(f'You matched the note!')
                    break # exit the loop if the note has been held for more than two seconds
            elif note_held_time > 0:
                self.quizText.setText(f'Your last note was {note}. Keep Trying!')
                # print(f'Your last note was {note}. Try Again')
                note_held_time -= 1024/44100 # decrement the note held time if the note changes
            else:
                self.quizText.setText(f'Your last note was {note}. Keep Trying!')
                # print(f'Your last note was {note}. Try Again')
        # print(note, note_held_time)
        app.processEvents()
        endTime = time.time()
        elapsedTime = endTime - startTime
        if elapsedTime > 5:
            self.quizText.setText(f'You didn\'t match the note: {c.name}. Try Again.')
            # print(f'You didn\'t match the note within 5 seconds. Try Again')
            return False
        
    return True

def match_note_in_sequence(target_notes, duration, self, app):
    c = Note()
    index = 0
    length = len(target_notes)
    c.from_int(target_notes[index])
    self.quizText.setText(f'Listening for note: {c.name}')

    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32, channels=1, rate=44100, input=True, frames_per_buffer=2048)
    note_held_time = 0.0

    startTime = time.time()
    endTime = time.time()

    while True:
        if self.interruptListening:
            return False
        data = stream.read(1024, exception_on_overflow=False)
        signal = np.frombuffer(data, dtype=np.float32)
        pitch = get_pitch(signal)
        note = pitch_to_note(pitch)
        if pitch > 0:
            if note == c.name + str(c.octave):
                note_held_time += 1024/44100 # increment the note held time by the buffer length
                if note_held_time >= duration[index]:
                    index += 1
                    note_held_time = 0.0
                    if index >= length:
                        break
                    else:
                        c.from_int(target_notes[index])
                        self.quizText.setText(f'Listening for note: {c.name}')
            elif note_held_time > 0:
                note_held_time -= 1024/44100
        app.processEvents()
        endTime = time.time()
        elapsedTime = endTime - startTime
        if elapsedTime > 5:
            return False
    self.quizText.setText(f'Note sequence matched!')        
    return True

def midi_quit():
    del player
    midi.quit()

def play_note_helper(player, note):
    player.note_off(note, 127)
def play_note_sequence(note_sequence, duration):
    for i in range(len(duration)):
        player.note_on(note_sequence[i] + 24, 127)
        timer = threading.Timer(duration[i], play_note_helper, [player, note_sequence[i] + 24])
        timer.start()
        time.sleep(duration[i])

def play_note(note):
    player.note_on(note + 24, 127) # the pygame midi is offset by two octaves for some reason
    timer = threading.Timer(1, play_note_helper, [player, note + 24])
    timer.start()
def ear_train(note, duration):
    
    play_note(note)
    match_note(note, duration)
def ear_train_multiple(notes):
    for note in notes:
        play_note(note)
        time.sleep(1)
    for note in notes:
        match_note(note, 0.5)
#midi setup
midi.init()
player = midi.Output(midi.get_default_output_id())
player.set_instrument(0)
# ear_train_multiple([24, 26, 28, 29, 31])