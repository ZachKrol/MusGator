import sys
import csv
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

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

        # self.learnButton.clicked.connect(lambda: self.toLearn(pages))
        # self.quizButton.clicked.connect(lambda: self.toQuiz(pages))
        # self.progressButton.clicked.connect(lambda: self.toProgress(pages))

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

        text = []
        title = []

        with open('data.csv') as file:
            csv_reader = csv.reader(file, delimiter=',')

            for row in csv_reader:
                    if row[0] == "Lesson":
                        if row[1] == lesson_name:
                            title.append(row[2])
                            text.append(row[3])

        self.lessonTitle.setText(lesson_name)
        self.lessonTextLabel.setText(title[0])
        self.lessonText.setText(text[0])



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
