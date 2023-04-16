import sys
import csv
import logo.rc_logo as rc_logo
import banner.rc_banner as rc_banner
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtGui import *
import random
import audio_framework as af
from PyQt5.QtCore import QThreadPool, QRunnable

# 0 - Splash page
# 1 - Home page
# 2 - Note Learning page

# Splash Page
class SplashPage(QMainWindow):
    def __init__(self, pages):
        super(SplashPage, self).__init__()
        loadUi("SplashPage.ui", self)
        self.homeIndex = 1

        self.startButton.clicked.connect(lambda: self.toHome(pages))

    def toHome(self, pages):
        pages.setCurrentIndex(self.homeIndex)


# Home Page
class HomePage(QMainWindow):
    def __init__(self, pages):
        super(HomePage, self).__init__()
        loadUi("HomePage.ui", self)

        self.noteLearnIndex = 2
        self.sightLearnIndex = 3
        self.rhythmLearnIndex = 4
        self.earLearnIndex = 5

        self.noteQuizIndex = 6
        self.sightQuizIndex = 7
        self.rhythmQuizIndex = 8
        self.earQuizIndex = 9

        
        self.learnNotes.clicked.connect(lambda: self.toNoteLearn(pages))
        self.learnSight.clicked.connect(lambda: self.toSightLearn(pages))
        self.learnRhythm.clicked.connect(lambda: self.toRhythmLearn(pages))
        self.learnEar.clicked.connect(lambda: self.toEarLearn(pages))

        self.quizNotes.clicked.connect(lambda: self.toNoteQuiz(pages))
        self.quizSight.clicked.connect(lambda: self.toSightQuiz(pages))
        self.quizRhythm.clicked.connect(lambda: self.toRhythmQuiz(pages))
        self.quizEar.clicked.connect(lambda: self.toEarQuiz(pages))


    def toNoteLearn(self, pages):
        pages.setCurrentIndex(self.noteLearnIndex)
    
    def toSightLearn(self, pages):
        pages.setCurrentIndex(self.sightLearnIndex)

    def toRhythmLearn(self, pages):
        pages.setCurrentIndex(self.rhythmLearnIndex)
    
    def toEarLearn(self, pages):
        pages.setCurrentIndex(self.earLearnIndex)

    def toNoteQuiz(self, pages):
        pages.setCurrentIndex(self.noteQuizIndex)

    def toSightQuiz(self, pages):
        pages.setCurrentIndex(self.sightQuizIndex)

    def toRhythmQuiz(self, pages):
        pages.setCurrentIndex(self.rhythmQuizIndex)

    def toEarQuiz(self, pages):
        pages.setCurrentIndex(self.earQuizIndex)            



# Learn Page 1
class LearnPage1(QMainWindow):
    def __init__(self, pages, lesson_name):
        super(LearnPage1, self).__init__()
        
        loadUi("note-rythLesson.ui", self)

        self.text = []
        self.title = []
        self.imagename = []

        self.index = 0

        with open('data.csv') as file:
            csv_reader = csv.reader(file, delimiter=',')

            for row in csv_reader:
                    if row[0] == "Lesson":
                        if row[1] == lesson_name:
                            self.title.append(row[2])
                            self.text.append(row[3])
                            self.imagename.append(row[4])

        self.previousButton.setText("Back")
        self.lessonTitle.setText(lesson_name)
        self.lessonTextLabel.setText(self.title[self.index])
        self.lessonText.setText(self.text[self.index])
        
        scene = QGraphicsScene()
        scene.addPixmap(QPixmap("./images/" + self.imagename[self.index]))
        self.lessonImage.setScene(scene)

        self.previousButton.clicked.connect(lambda: self.clickPreviousButton(pages))
        self.nextButton.clicked.connect(lambda: self.clickNextButton(pages))

    def clickPreviousButton(self, pages):
        if self.index == 0:
            pages.setCurrentIndex(1) # Return to home page
        
        else:
            if self.index == 1:
                self.previousButton.setText("Back")
            
            if self.index == len(self.text) - 1:
                self.nextButton.setText("Next")

            self.index = self.index - 1
            self.lessonTextLabel.setText(self.title[self.index])
            self.lessonText.setText(self.text[self.index])

            scene = QGraphicsScene()
            scene.addPixmap(QPixmap("./images/" + self.imagename[self.index]))
            self.lessonImage.setScene(scene)

    def clickNextButton(self, pages):
        if self.index == len(self.text) - 1:
            pages.setCurrentIndex(1) # Return to home page
            self.nextButton.setText("Next")
            self.index = 0

            self.lessonTextLabel.setText(self.title[self.index])
            self.lessonText.setText(self.text[self.index])

            scene = QGraphicsScene()
            scene.addPixmap(QPixmap("./images/" + self.imagename[self.index]))
            self.lessonImage.setScene(scene)
        
        else:
            if self.index == len(self.text) - 2:
                self.nextButton.setText("Finish")
            
            if self.index == 0:
                self.previousButton.setText("Previous")

            self.index = self.index + 1
            self.lessonTextLabel.setText(self.title[self.index])
            self.lessonText.setText(self.text[self.index])

            scene = QGraphicsScene()
            scene.addPixmap(QPixmap("./images/" + self.imagename[self.index]))
            self.lessonImage.setScene(scene)


# Learn Page 2
class LearnPage2(QMainWindow):
    def __init__(self, pages, lesson_name):
        super(LearnPage2, self).__init__()

        loadUi("sight-earLesson.ui", self)

        self.title = []
        self.imagename = []
        self.index = 0
        with open('data.csv') as file:
            csv_reader = csv.reader(file, delimiter=',')

            for row in csv_reader:
                    if row[0] == "Lesson":
                        if row[1] == lesson_name:
                            self.title.append(row[2])
                            self.imagename.append(row[3])

        self.previousButton.setText("Back")
        self.lessonTitle.setText(lesson_name)
        self.lessonTextLabel.setText(self.title[self.index])
        
        scene = QGraphicsScene()
        scene.addPixmap(QPixmap("./images/" + self.imagename[self.index]))
        self.lessonImage.setScene(scene)

        self.previousButton.clicked.connect(lambda: self.clickPreviousButton(pages))
        self.nextButton.clicked.connect(lambda: self.clickNextButton(pages))
        self.playAudioButton.clicked.connect(lambda: self.clickPlayAudioButton())

    def clickPreviousButton(self, pages):
        if self.index == 0:
            pages.setCurrentIndex(1) # Return to home page
        
        else:
            if self.index == 1:
                self.previousButton.setText("Back")

            if self.index == len(self.text) - 1:
                self.nextButton.setText("Next")
            
            self.index = self.index - 1
            self.lessonTextLabel.setText(self.title[self.index])

            scene = QGraphicsScene()
            scene.addPixmap(QPixmap("./images/" + self.imagename[self.index]))
            self.lessonImage.setScene(scene)

    def clickNextButton(self, pages):
        if self.index == len(self.title) - 1:
            pages.setCurrentIndex(1) # Return to home page
            self.nextButton.setText("Next")
            self.index = 0

            self.lessonTextLabel.setText(self.title[self.index])

            scene = QGraphicsScene()
            scene.addPixmap(QPixmap("./images/" + self.imagename[self.index]))
            self.lessonImage.setScene(scene)
        
        else:
            if self.index == len(self.title) - 2:
                self.nextButton.setText("Finish")
            
            if self.index == 0:
                self.previousButton.setText("Previous")

            self.index = self.index + 1
            self.lessonTextLabel.setText(self.title[self.index])

            scene = QGraphicsScene()
            scene.addPixmap(QPixmap("./images/" + self.imagename[self.index]))
            self.lessonImage.setScene(scene)
    def clickPlayAudioButton(self):
        af.play_note(24 + af.notes.note_to_int(af.scales.get_notes("C")[self.index]))
        
            


# Quiz Page 1
class QuizPage1(QMainWindow):
    def __init__(self, pages, quiz_name):
        super(QuizPage1, self).__init__()

        loadUi("note-rythQuiz.ui", self)

        self.button_group = QButtonGroup()
        self.button_group.setExclusive(True)

        self.selection1.setCheckable(True)
        self.selection2.setCheckable(True)
        self.selection3.setCheckable(True)
        self.selection4.setCheckable(True)

        self.button_group.addButton(self.selection1)
        self.button_group.addButton(self.selection2)
        self.button_group.addButton(self.selection3)
        self.button_group.addButton(self.selection4)
        self.button_group.buttonClicked.connect(lambda: self.clickAnswerSelection())


        self.text = []
        self.imagename = []
        self.answerChoices = []
        self.correctAnswer = []

        self.index = 0

        with open('data.csv') as file:
            csv_reader = csv.reader(file, delimiter=',')

            for row in csv_reader:
                    if row[0] == "Quiz":
                        if row[1] == quiz_name:
                            self.text.append(row[2])
                            self.imagename.append(row[4])

                            answers = [row[5], row[6], row[7], row[8]]
                            random.shuffle(answers)
                            self.answerChoices.append(answers)

                            self.correctAnswer.append(row[9])

        self.previousButton.setText("Back")
        self.quizTitle.setText(quiz_name)
        self.quizText.setText(self.text[self.index])

        self.selection1.setText(self.answerChoices[self.index][0])
        self.selection2.setText(self.answerChoices[self.index][1])
        self.selection3.setText(self.answerChoices[self.index][2])
        self.selection4.setText(self.answerChoices[self.index][3])

        
        scene = QGraphicsScene()
        scene.addPixmap(QPixmap("./images/" + self.imagename[self.index]))
        self.quizImage.setScene(scene)

        self.previousButton.clicked.connect(lambda: self.clickPreviousButton(pages))
        self.nextButton.clicked.connect(lambda: self.clickNextButton(pages))
        self.answerButton.clicked.connect(lambda: self.clickAnswerButton(pages))


    def clickAnswerButton(self, pages):
        # add logic for checking correct answer
        # need to set button as selected when answer is chosen to select it
        if self.button_group.checkedButton().text() == self.correctAnswer[self.index]:
            self.button_group.checkedButton().setStyleSheet("background-color: green; color: rgb(255, 255, 255);")
        else:
            self.button_group.checkedButton().setStyleSheet("background-color: red; color: rgb(255, 255, 255);")
    

    def clickAnswerSelection(self):
        self.button_group.checkedButton().setStyleSheet("background-color: #18A0FB; color: rgb(255, 255, 255);")


    def clickPreviousButton(self, pages):
        if self.index == 0:
            pages.setCurrentIndex(1) # Return to home page
        
        else:
            if self.index == 1:
                self.previousButton.setText("Back")

            if self.index == len(self.text) - 1:
                self.nextButton.setText("Next")

            self.index = self.index - 1
            self.quizText.setText(self.text[self.index])

            self.selection1.setStyleSheet("color: #18A0FB; background-color: rgb(255, 255, 255);")
            self.selection2.setStyleSheet("color: #18A0FB; background-color: rgb(255, 255, 255);")
            self.selection3.setStyleSheet("color: #18A0FB; background-color: rgb(255, 255, 255);")
            self.selection4.setStyleSheet("color: #18A0FB; background-color: rgb(255, 255, 255);")

            self.selection1.setText(self.answerChoices[self.index][0])
            self.selection2.setText(self.answerChoices[self.index][1])
            self.selection3.setText(self.answerChoices[self.index][2])
            self.selection4.setText(self.answerChoices[self.index][3])

            scene = QGraphicsScene()
            scene.addPixmap(QPixmap("./images/" + self.imagename[self.index]))
            self.quizImage.setScene(scene)

    def clickNextButton(self, pages):
        if self.index == len(self.text) - 1:
            pages.setCurrentIndex(1) # Return to home page
            self.nextButton.setText("Next")
            self.index = 0

            self.quizText.setText(self.text[self.index])

            self.selection1.setStyleSheet("color: #18A0FB; background-color: rgb(255, 255, 255);")
            self.selection2.setStyleSheet("color: #18A0FB; background-color: rgb(255, 255, 255);")
            self.selection3.setStyleSheet("color: #18A0FB; background-color: rgb(255, 255, 255);")
            self.selection4.setStyleSheet("color: #18A0FB; background-color: rgb(255, 255, 255);")

            self.selection1.setText(self.answerChoices[self.index][0])
            self.selection2.setText(self.answerChoices[self.index][1])
            self.selection3.setText(self.answerChoices[self.index][2])
            self.selection4.setText(self.answerChoices[self.index][3])

            scene = QGraphicsScene()
            scene.addPixmap(QPixmap("./images/" + self.imagename[self.index]))
            self.quizImage.setScene(scene)
        
        else:
            if self.index == len(self.text) - 2:
                self.nextButton.setText("Finish")
            
            if self.index == 0:
                self.previousButton.setText("Previous")

            self.index = self.index + 1
            self.quizText.setText(self.text[self.index])

            self.selection1.setStyleSheet("color: #18A0FB; background-color: rgb(255, 255, 255);")
            self.selection2.setStyleSheet("color: #18A0FB; background-color: rgb(255, 255, 255);")
            self.selection3.setStyleSheet("color: #18A0FB; background-color: rgb(255, 255, 255);")
            self.selection4.setStyleSheet("color: #18A0FB; background-color: rgb(255, 255, 255);")

            self.selection1.setText(self.answerChoices[self.index][0])
            self.selection2.setText(self.answerChoices[self.index][1])
            self.selection3.setText(self.answerChoices[self.index][2])
            self.selection4.setText(self.answerChoices[self.index][3])

            scene = QGraphicsScene()
            scene.addPixmap(QPixmap("./images/" + self.imagename[self.index]))
            self.quizImage.setScene(scene)


# Quiz Page 2
class QuizPage2(QMainWindow):
    def __init__(self, pages, quiz_name):
        super(QuizPage2, self).__init__()
        
        loadUi("sight-earAudioQuiz.ui", self)
        
        self.listeningThread = None
        self.interruptListening = False
        self.noteSequence = af.scales.get_notes("C")
        self.curNoteIndex = 0
        self.startStopButton.clicked.connect(lambda: self.play_notes_in_thread())
        self.answerButton.clicked.connect(lambda: self.listen_in_thread())

        self.text = []
        self.imagename = []
        self.audioThread = None
        self.interruptAudio = False
        self.index = 0

        with open('data.csv') as file:
            csv_reader = csv.reader(file, delimiter=',')

            for row in csv_reader:
                    if row[0] == "Quiz":
                        if row[1] == quiz_name:
                            self.text.append(row[2])
                            self.imagename.append(row[3])

        self.previousButton.setText("Back")
        self.quizTitle.setText(quiz_name)
        self.quizText.setText(self.text[self.index])
        
        scene = QGraphicsScene()
        scene.addPixmap(QPixmap("./images/" + self.imagename[self.index]))
        self.quizImage.setScene(scene)

        self.previousButton.clicked.connect(lambda: self.clickPreviousButton(pages))
        self.nextButton.clicked.connect(lambda: self.clickNextButton(pages))
        self.answerButton.clicked.connect(lambda: self.clickAnswerButton(pages))

    def play_notes_in_thread(self):
        if self.audioThread == None:   
            self.audioThread = af.threading.Thread(target=self.playNotes)
            self.audioThread.start()
        else:
            self.interruptAudio = True
    def listen_in_thread(self):
        if self.listeningThread == None:   
            self.listeningThread = af.threading.Thread(target=self.check_pitch)
            self.listeningThread.start()
        else:
            self.interruptListening = True
    
    
    def check_pitch(self):
        if(af.match_note(24 + af.notes.note_to_int(self.noteSequence[self.curNoteIndex]), 0.5, self)):
            self.curNoteIndex+=1
        self.listeningThread = None
        self.interruptListening = False
        
    
    def clickAnswerButton(self, pages):
        # add logic for checking correct answer
        # need to set button as selected when answer is chosen to select it

        # if selectedText == answer[index]
            # set styling for correct
        # else
            # set styling for wrong
        print("pressed")


    def clickPreviousButton(self, pages):
        self.interruptAudio = True
        if self.index == 0:
            pages.setCurrentIndex(1) # Return to home page
        
        else:
            if self.index == 1:
                self.previousButton.setText("Back")
            
            if self.index == len(self.text) - 1:
                self.nextButton.setText("Next")

            self.index = self.index - 1
            self.quizText.setText(self.text[self.index])

            scene = QGraphicsScene()
            scene.addPixmap(QPixmap("./images/" + self.imagename[self.index]))
            self.quizImage.setScene(scene)

    def clickNextButton(self, pages):
        self.interruptAudio = True
        if self.index == len(self.text) - 1:
            pages.setCurrentIndex(1) # Return to home page
            self.nextButton.setText("Next")
            self.index = 0

            self.quizText.setText(self.text[self.index])

            scene = QGraphicsScene()
            scene.addPixmap(QPixmap("./images/" + self.imagename[self.index]))
            self.quizImage.setScene(scene)
        
        else:
            if self.index == len(self.text) - 2:
                self.nextButton.setText("Finish")
            
            if self.index == 0:
                self.previousButton.setText("Previous")

            self.index = self.index + 1
            self.quizText.setText(self.text[self.index])

            scene = QGraphicsScene()
            scene.addPixmap(QPixmap("./images/" + self.imagename[self.index]))
            self.quizImage.setScene(scene)
    def playNotes(self):
        for i in range(self.curNoteIndex, len(self.noteSequence)):
            if not self.interruptAudio:
                af.play_note(24 + af.notes.note_to_int(self.noteSequence[i]))
                af.time.sleep(1)
        self.audioThread = None
        self.interruptAudio = False

def main():
    app = QApplication(sys.argv)

    # 'pages' is an array with each page at a different index
    pages = QStackedWidget()
    pages.setWindowTitle("MusGator")
    pages.setMinimumSize(800,600)

    # NOTE: if pages need some information before loading, then don't initialize them here
 
    splashPage = SplashPage(pages)
    homePage = HomePage(pages)

    noteLearnPage = LearnPage1(pages, "Note Learning")
    sightLearnPage = LearnPage2(pages, "Sight Reading")
    rhythmLearnPage = LearnPage1(pages, "Rhythm")
    earLearnPage = LearnPage2(pages, "Ear Training")

    noteQuizPage = QuizPage1(pages, "Note Quiz")
    sightQuizPage = QuizPage2(pages, "Sight Reading Quiz")
    rhythmQuizPage = QuizPage1(pages, "Rhythm Quiz")
    earQuizPage = QuizPage2(pages, "Ear Training Quiz")

    
    pages.addWidget(splashPage) # index 0
    pages.addWidget(homePage) # index 1

    pages.addWidget(noteLearnPage) # index 2
    pages.addWidget(sightLearnPage) # index 3
    pages.addWidget(rhythmLearnPage) # index 4
    pages.addWidget(earLearnPage) # index 5

    pages.addWidget(noteQuizPage) # index 6
    pages.addWidget(sightQuizPage) # index 7
    pages.addWidget(rhythmQuizPage) # index 8
    pages.addWidget(earQuizPage) # index 9
    pages.audioThread = None

    pages.show()

    app.exec_()


if __name__ == '__main__':
    main()