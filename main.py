import sys
import csv
import rc_logo
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
        
        self.learnNotes.clicked.connect(lambda: self.toNoteLearn(pages))
        self.learnSight.clicked.connect(lambda: self.toSightLearn(pages))
        self.learnRhythm.clicked.connect(lambda: self.toRhythmLearn(pages))
        self.learnEar.clicked.connect(lambda: self.toEarLearn(pages))

    def toNoteLearn(self, pages):
        pages.setCurrentIndex(self.noteLearnIndex)
    
    def toSightLearn(self, pages):
        pages.setCurrentIndex(self.sightLearnIndex)

    def toRhythmLearn(self, pages):
        pages.setCurrentIndex(self.rhythmLearnIndex)
    
    def toEarLearn(self, pages):
        pages.setCurrentIndex(self.earLearnIndex)



# Learn Page
class LearnPage(QMainWindow):
    def __init__(self, pages, lesson_name):
        super(LearnPage, self).__init__()
        
        loadUi("Learning.ui", self)

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

    def clickNextButton(self, pages):
        if self.index == len(self.text) - 1:
            pages.setCurrentIndex(1) # Return to home page
            self.nextButton.setText("Next")
            self.index = 0

            self.lessonTextLabel.setText(self.title[self.index])
            self.lessonText.setText(self.text[self.index])
        
        else:
            if self.index == len(self.text) - 2:
                self.nextButton.setText("Finish")
            
            if self.index == 0:
                self.previousButton.setText("Previous")

            self.index = self.index + 1
            self.lessonTextLabel.setText(self.title[self.index])
            self.lessonText.setText(self.text[self.index])




def main():
    app = QApplication(sys.argv)

    # 'pages' is an array with each page at a different index
    pages = QStackedWidget()
    pages.setWindowTitle("MusGator")
    pages.setMinimumSize(800,600)

    # NOTE: if pages need some information before loading, then don't initialize them here
 
    splashPage = SplashPage(pages)
    homePage = HomePage(pages)

    noteLearnPage = LearnPage(pages, "Note Learning")
    sightLearnPage = LearnPage(pages, "Sight Reading")
    rhythmLearnPage = LearnPage(pages, "Rhythm")
    earLearnPage = LearnPage(pages, "Ear Training")

    pages.addWidget(splashPage) # index 0
    pages.addWidget(homePage) # index 1

    pages.addWidget(noteLearnPage) # index 2
    pages.addWidget(sightLearnPage) # index 3
    pages.addWidget(rhythmLearnPage) # index 4
    pages.addWidget(earLearnPage) # index 5

    pages.show()

    app.exec_()


if __name__ == '__main__':
    main()
