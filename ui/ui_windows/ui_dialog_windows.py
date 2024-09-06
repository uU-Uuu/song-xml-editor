################################################################################
## Form generated from reading UI file 'XMLWindowHwfibn.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide2.QtGui import QCursor, QFont
from PySide2.QtWidgets import *


class Ui_XMLWindow(object):
    def setupUi(self, XMLWindow):
        if XMLWindow.objectName():
            XMLWindow.setObjectName(u"XMLWindow")
        XMLWindow.resize(495, 824)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(XMLWindow.sizePolicy().hasHeightForWidth())
        XMLWindow.setSizePolicy(sizePolicy)
        XMLWindow.setMaximumSize(QSize(700, 900))
        XMLWindow.setStyleSheet(u"background-color: rgb(25, 37, 48)")
        self.verticalLayout = QVBoxLayout(XMLWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.xmlEdit = QPlainTextEdit(XMLWindow)
        self.xmlEdit.setObjectName(u"xmlEdit")
        self.xmlEdit.setEnabled(True)
        sizePolicy.setHeightForWidth(self.xmlEdit.sizePolicy().hasHeightForWidth())
        self.xmlEdit.setSizePolicy(sizePolicy)
        self.xmlEdit.setMaximumSize(QSize(700, 800))
        self.xmlEdit.setStyleSheet(u"font: 63 9pt \"Yu Mincho Demibold\";\n"
"border-radius: 10px;\n"
"color: rgba(162, 198, 208, 200);\n"
"margin: 10px;\n"
"border: 1px solid  rgba(88, 109, 117, 200);\n"
"padding: 15px 10px;\n"
"background-color: rgb(36, 46, 57);\n"
"selection-background-color: rgb(110, 135, 142);\n"
"")
        self.xmlEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.xmlEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

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
        self.frame.setStyleSheet(u"background-color: transparent")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.XMLInfoLabel = QLabel(self.frame)
        self.XMLInfoLabel.setObjectName(u"XMLInfoLabel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.XMLInfoLabel.sizePolicy().hasHeightForWidth())
        self.XMLInfoLabel.setSizePolicy(sizePolicy2)
        self.XMLInfoLabel.setMaximumSize(QSize(100, 16777215))
        self.XMLInfoLabel.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 14px;\n"
"color: rgb(110, 135, 142);\n"
"background-color: transparent")
        self.XMLInfoLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.XMLInfoLabel)

        self.editXMLFileBtn = QToolButton(self.frame)
        self.editXMLFileBtn.setObjectName(u"editXMLFileBtn")
        self.editXMLFileBtn.setMinimumSize(QSize(125, 35))
        font = QFont()
        font.setFamily(u"Yu Mincho Demibold")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.editXMLFileBtn.setFont(font)
        self.editXMLFileBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.editXMLFileBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 16px;\n"
"border: 0.5px solid rgb(70, 70, 70);\n"
"background: rgb(110, 135, 142);\n"
"border-radius: 10px;\n"
"color: rgb(242, 255, 245)")

        self.horizontalLayout.addWidget(self.editXMLFileBtn)

        self.saveXMLFIleBtn = QToolButton(self.frame)
        self.saveXMLFIleBtn.setObjectName(u"saveXMLFIleBtn")
        self.saveXMLFIleBtn.setMinimumSize(QSize(125, 35))
        self.saveXMLFIleBtn.setFont(font)
        self.saveXMLFIleBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.saveXMLFIleBtn.setAutoFillBackground(False)
        self.saveXMLFIleBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 16px;\n"
"border: 0.5px solid rgb(70, 70, 70);\n"
"background: rgb(110, 135, 142);\n"
"border-radius: 10px;\n"
"color: rgb(242, 255, 245)")

        self.horizontalLayout.addWidget(self.saveXMLFIleBtn)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(XMLWindow)

        QMetaObject.connectSlotsByName(XMLWindow)
    # setupUi

    def retranslateUi(self, XMLWindow):
        XMLWindow.setWindowTitle(QCoreApplication.translate("XMLWindow", u"XML Preview", None))
        self.xmlEdit.setPlainText("")
        self.XMLInfoLabel.setText(QCoreApplication.translate("XMLWindow", u"Read Mode", None))
        self.editXMLFileBtn.setText(QCoreApplication.translate("XMLWindow", u"Edit", None))
        self.saveXMLFIleBtn.setText(QCoreApplication.translate("XMLWindow", u"Save", None))
    # retranslateUi




class Ui_LilyPondWindow(object):
    def setupUi(self, LilyPondWindow):
        if LilyPondWindow.objectName():
            LilyPondWindow.setObjectName(u"LilyPondWindow")
        LilyPondWindow.resize(1000, 800)
        LilyPondWindow.setMaximumSize(QSize(1200, 800))
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


class Ui_MessageBoxStyled(object):
    def setupUi(self, MessageBoxStyled):
        if MessageBoxStyled.objectName():
            MessageBoxStyled.setObjectName(u"MessageBoxStyled")
        MessageBoxStyled.resize(499, 224)
        MessageBoxStyled.setStyleSheet("""
                                       
             QMessageBox {
                font: 63 9pt Yu Mincho Demibold;
                background-color: rgb(36, 46, 57);
            }
            QLabel {
                font: 63 9pt Yu Mincho Demibold;
                color: rgb(130, 160, 168);      
            }
            QPushButton {
                font: 63 9pt Yu Mincho Demibold;
                border: 0.5px solid rgb(70, 70, 70);
                background: rgb(110, 135, 142);
                color: rgb(242, 255, 245);
                width: 50px;
                height: 15px;
                padding: 10px;
                border-radius: 10px;
                cursor:                        
            }
        """)
        self.retranslateUi(MessageBoxStyled)

        QMetaObject.connectSlotsByName(MessageBoxStyled)
    # setupUi

    def retranslateUi(self, MessageBoxStyled):
        MessageBoxStyled.setWindowTitle(QCoreApplication.translate("MessageBoxStyled", u"Dialog", None))
    # retranslateUi

