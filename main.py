import sys
import csv
import logo.rc_logo as rc_logo
import banner.rc_banner as rc_banner
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtGui import *

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
        
        self.learnNotes.clicked.connect(lambda: self.toNoteLearn(pages))
        self.learnSight.clicked.connect(lambda: self.toSightLearn(pages))
        self.learnRhythm.clicked.connect(lambda: self.toRhythmLearn(pages))
        self.learnEar.clicked.connect(lambda: self.toEarLearn(pages))
        self.quizNotes.clicked.connect(lambda: self.toNoteQuiz(pages))

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

    def clickPreviousButton(self, pages):
        if self.index == 0:
            pages.setCurrentIndex(1) # Return to home page
        
        else:
            if self.index == 1:
                self.previousButton.setText("Back")
            
            self.index = self.index - 1
            self.lessonTextLabel.setText(self.title[self.index])

            scene = QGraphicsScene()
            scene.addPixmap(QPixmap("./images/" + self.imagename[self.index]))
            self.lessonImage.setScene(scene)

    def clickNextButton(self, pages):
        if self.index == len(self.text) - 1:
            pages.setCurrentIndex(1) # Return to home page
            self.nextButton.setText("Next")
            self.index = 0

            self.lessonTextLabel.setText(self.title[self.index])

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

            scene = QGraphicsScene()
            scene.addPixmap(QPixmap("./images/" + self.imagename[self.index]))
            self.lessonImage.setScene(scene)



# Quiz Page
class QuizPage(QMainWindow):
    def __init__(self, pages, quiz_name, quiz_type):
        super(QuizPage, self).__init__()
        
        if quiz_type == 1:
            loadUi("note-rythQuiz.ui", self)
        
        elif quiz_type == 2:
            loadUi("sight-earQuiz.ui", self)

        self.text = []
        self.imagename = []

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

    def clickPreviousButton(self, pages):
        if self.index == 0:
            pages.setCurrentIndex(1) # Return to home page
        
        else:
            if self.index == 1:
                self.previousButton.setText("Back")
            
            self.index = self.index - 1
            self.quizText.setText(self.text[self.index])

            scene = QGraphicsScene()
            scene.addPixmap(QPixmap("./images/" + self.imagename[self.index]))
            self.quizImage.setScene(scene)

    def clickNextButton(self, pages):
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

    noteQuizPage = QuizPage(pages, "Note Quiz", 1)
    noteQuizPage = QuizPage(pages, "Rhythm Quiz", 1)
    noteQuizPage = QuizPage(pages, "Sight Reading Quiz", 1)
    noteQuizPage = QuizPage(pages, "Ear Training Quiz", 1)


    pages.addWidget(splashPage) # index 0
    pages.addWidget(homePage) # index 1

    pages.addWidget(noteLearnPage) # index 2
    pages.addWidget(sightLearnPage) # index 3
    pages.addWidget(rhythmLearnPage) # index 4
    pages.addWidget(earLearnPage) # index 5

    pages.addWidget(noteQuizPage) # index 6

    pages.show()

    app.exec_()


if __name__ == '__main__':
    main()