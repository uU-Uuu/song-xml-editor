from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *



class Ui_XMLWindow(object):
    def setupUi(self, XMLWindow):
        if XMLWindow.objectName():
            XMLWindow.setObjectName(u"XMLWindow")
        XMLWindow.resize(450, 824)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(XMLWindow.sizePolicy().hasHeightForWidth())
        XMLWindow.setSizePolicy(sizePolicy)
        XMLWindow.setMaximumSize(QSize(700, 900))
        self.verticalLayout = QVBoxLayout(XMLWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.xmlEdit = QPlainTextEdit(XMLWindow)
        self.xmlEdit.setObjectName(u"xmlEdit")
        sizePolicy.setHeightForWidth(self.xmlEdit.sizePolicy().hasHeightForWidth())
        self.xmlEdit.setSizePolicy(sizePolicy)
        self.xmlEdit.setMaximumSize(QSize(700, 800))

        self.verticalLayout.addWidget(self.xmlEdit)

        self.frame = QFrame(XMLWindow)
        self.frame.setObjectName(u"frame")
        self.frame.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setMinimumSize(QSize(0, 50))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.editXMLFileBtn = QToolButton(self.frame)
        self.editXMLFileBtn.setObjectName(u"editXMLFileBtn")
        self.editXMLFileBtn.setMinimumSize(QSize(125, 35))
        font = QFont()
        font.setFamily(u"Yu Mincho")
        font.setPointSize(9)
        self.editXMLFileBtn.setFont(font)

        self.horizontalLayout.addWidget(self.editXMLFileBtn)

        self.saveXMLFIleBtn = QToolButton(self.frame)
        self.saveXMLFIleBtn.setObjectName(u"saveXMLFIleBtn")
        self.saveXMLFIleBtn.setMinimumSize(QSize(125, 35))
        self.saveXMLFIleBtn.setFont(font)
        self.saveXMLFIleBtn.setAutoFillBackground(False)

        self.horizontalLayout.addWidget(self.saveXMLFIleBtn)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(XMLWindow)

        QMetaObject.connectSlotsByName(XMLWindow)
    # setupUi

    def retranslateUi(self, XMLWindow):
        XMLWindow.setWindowTitle(QCoreApplication.translate("XMLWindow", u"XML Editor", None))
        self.editXMLFileBtn.setText(QCoreApplication.translate("XMLWindow", u"Edit", None))
        self.saveXMLFIleBtn.setText(QCoreApplication.translate("XMLWindow", u"Save", None))
    # retranslateUi



class Ui_LilyPondWindow(object):
    def setupUi(self, LilyPondWindow):
        if LilyPondWindow.objectName():
            LilyPondWindow.setObjectName(u"LilyPondWindow")
        LilyPondWindow.resize(660, 556)
        LilyPondWindow.setMaximumSize(QSize(850, 800))
        self.verticalLayout = QVBoxLayout(LilyPondWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lilyPondSheetView = QGraphicsView(LilyPondWindow)
        self.lilyPondSheetView.setObjectName(u"lilyPondSheetView")

        self.verticalLayout.addWidget(self.lilyPondSheetView)


        self.retranslateUi(LilyPondWindow)

        QMetaObject.connectSlotsByName(LilyPondWindow)
    # setupUi

    def retranslateUi(self, LilyPondWindow):
        LilyPondWindow.setWindowTitle(QCoreApplication.translate("LilyPondWindow", u"Music Sheet Preview", None))
    # retranslateUi

