from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_SplashWindow(object):
    def setupUi(self, SplashWindow):
        if SplashWindow.objectName():
            SplashWindow.setObjectName(u"SplashWindow")
        SplashWindow.resize(637, 361)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SplashWindow.sizePolicy().hasHeightForWidth())
        SplashWindow.setSizePolicy(sizePolicy)
        SplashWindow.setCursor(QCursor(Qt.ArrowCursor))
        SplashWindow.setStyleSheet(u"")
        self.frame = QFrame(SplashWindow)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-10, -10, 660, 380))
        self.frame.setCursor(QCursor(Qt.WaitCursor))
        self.frame.setStyleSheet(u"background-image: url('../img/noah-silliman-_k9dCeh5Ca0-unsplash.jpg');\n"
"background-repeat: no-repeat;\n"
"background-position: center;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(370, 280, 381, 111))
        font = QFont()
        font.setFamily(u"Yu Mincho Demibold")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_2.setFont(font)
        self.label_2.setCursor(QCursor(Qt.WaitCursor))
        self.label_2.setStyleSheet(u"color: rgb(206, 225, 231);\n"
"font: 63 16pt \"Yu Mincho Demibold\";\n"
"background: transparent;")

        self.retranslateUi(SplashWindow)

        QMetaObject.connectSlotsByName(SplashWindow)
    # setupUi

    def retranslateUi(self, SplashWindow):
        SplashWindow.setWindowTitle(QCoreApplication.translate("SplashWindow", u"Song XML Editor", None))
        self.label_2.setText(QCoreApplication.translate("SplashWindow", u"Song XML Editor", None))
    # retranslateUi