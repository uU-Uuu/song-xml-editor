from PySide2 import QtWidgets

from ui.ui_windows.ui_splash_window import Ui_SplashWindow


class SplashWindow(QtWidgets.QSplashScreen, Ui_SplashWindow):
    def __init__(self):
        super(SplashWindow, self).__init__()
        self.setupUi(self)
        self.move(600, 260)