import pyaudio
import numpy as np
import aubio
from scipy.signal import find_peaks
import time
import threading
import pygame.midi as midi
from mingus.containers import Note
notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

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
    note = notes[pitch_index % 12]
    octave = pitch_index // 12 - 1
    
    return note + str(octave)
def match_note(target_note, duration):
    c = Note()
    c.from_int(target_note)
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32, channels=1, rate=44100, input=True, frames_per_buffer=2048)
    note_held_time = 0.0
    while True:
        data = stream.read(1024, exception_on_overflow=False)
        signal = np.frombuffer(data, dtype=np.float32)
        pitch = get_pitch(signal)
        note = pitch_to_note(pitch)
        if pitch > 0:
            if note == c.name + str(c.octave):
                note_held_time += 1024/44100 # increment the note held time by the buffer length
                if note_held_time >= duration:
                    break # exit the loop if the note has been held for more than two seconds
            elif note_held_time > 0:
                note_held_time -= 1024/44100 # decrement the note held time if the note changes
       # print(note, note_held_time)
    return True

def midi_quit():
    del player
    midi.quit()

def play_note_helper(player, note):
    player.note_off(note, 127)
    
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
ear_train_multiple([24, 26, 28, 29, 31])