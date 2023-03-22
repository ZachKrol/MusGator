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
        
        self.learnNotes.clicked.connect(lambda: self.toNoteLearn(pages))

    def toNoteLearn(self, pages):
        pages.setCurrentIndex(self.noteLearnIndex)



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


    pages.addWidget(splashPage) # index 0
    pages.addWidget(homePage) # index 1
    pages.addWidget(noteLearnPage) # index 2

    pages.show()

    app.exec_()


if __name__ == '__main__':
    main()
