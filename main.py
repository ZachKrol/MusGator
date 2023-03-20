import sys
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


# Splash Page
class SplashPage(QMainWindow):
    def __init__(self, pages):
        super(SplashPage, self).__init__()
        loadUi("SplashPage.ui", self)
        self.homeIndex = 1
        self.learnIndex = 2
        self.quizIndex = 3
        self.progressIndex = 4

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
        self.learnIndex = 2
        self.quizIndex = 3
        self.progressIndex = 4
        
        # self.learnButton.clicked.connect(lambda: self.toLearn(pages))
        # self.quizButton.clicked.connect(lambda: self.toQuiz(pages))
        # self.progressButton.clicked.connect(lambda: self.toProgress(pages))

    def toLearn(self, pages):
        pages.setCurrentIndex(self.learnIndex)

    def toQuiz(self, pages):
        pages.setCurrentIndex(self.quizIndex)

    def toProgress(self, pages):
        pages.setCurrentIndex(self.progressIndex)



# Learn Page
class LearnPage(QMainWindow):
    def __init__(self, pages):
        super(LearnPage, self).__init__()
        loadUi("LearnPage.ui", self)
        self.quizIndex = 3
        self.progressIndex = 4

        # self.quizButton.clicked.connect(lambda: self.toQuiz(pages))
        # self.progressButton.clicked.connect(lambda: self.toProgress(pages))

    def toQuiz(self, pages):
        pages.setCurrentIndex(self.quizIndex)

    def toProgress(self, pages):
        pages.setCurrentIndex(self.progressIndex)


# Quiz Page
class QuizPage(QMainWindow):
    def __init__(self, pages):
        super(QuizPage, self).__init__()
        loadUi("QuizPage.ui", self)
        self.learnIndex = 2
        self.progressIndex = 4

        # self.learnButton.clicked.connect(lambda: self.toLearn(pages))
        # self.progressButton.clicked.connect(lambda: self.toProgress(pages))

    def toLearn(self, pages):
        pages.setCurrentIndex(self.learnIndex)

    def toProgress(self, pages):
        pages.setCurrentIndex(self.progressIndex)


# Progress Page
class ProgressPage(QMainWindow):
    def __init__(self, pages):
        super(ProgressPage, self).__init__()
        loadUi("ProgressPage.ui", self)
        self.learnIndex = 2
        self.quizIndex = 3

        # self.learnButton.clicked.connect(lambda: self.toLearn(pages))
        # self.quizButton.clicked.connect(lambda: self.toQuiz(pages))

    def toLearn(self, pages):
        pages.setCurrentIndex(self.learnIndex)

    def toQuiz(self, pages):
        pages.setCurrentIndex(self.quizIndex)


def main():
    app = QApplication(sys.argv)

    # 'pages' is an array with each page at a different index
    pages = QStackedWidget()
    pages.setWindowTitle("MusGator")
    pages.setMinimumSize(800,600)

    # NOTE: if pages need some information before loading, then don't initialize them here

    splashPage = SplashPage(pages)
    homePage = HomePage(pages)
    learnPage = LearnPage(pages)
    quizPage = QuizPage(pages)
    progressPage = ProgressPage(pages)


    pages.addWidget(splashPage) # index 0
    pages.addWidget(homePage) # index 1
    pages.addWidget(learnPage) # index 2
    pages.addWidget(quizPage) # index 3
    pages.addWidget(progressPage) # index 4

    pages.show()

    app.exec_()


if __name__ == '__main__':
    main()
