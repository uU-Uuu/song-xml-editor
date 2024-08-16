# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'workspacePaneluibfDWcf.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

class Ui_WorkspacePanelWindow(object):
    def setupUi(self, WorkspacePanelWindow):
        if WorkspacePanelWindow.objectName():
            WorkspacePanelWindow.setObjectName(u"WorkspacePanelWindow")
        WorkspacePanelWindow.resize(647, 436)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(WorkspacePanelWindow.sizePolicy().hasHeightForWidth())
        WorkspacePanelWindow.setSizePolicy(sizePolicy)
        WorkspacePanelWindow.setMaximumSize(QSize(647, 436))
        WorkspacePanelWindow.setStyleSheet(u"background: rgb(25, 37, 48);")
        self.frame = QFrame(WorkspacePanelWindow)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(270, 10, 361, 431))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.createXMLDocBtn = QToolButton(self.frame)
        self.createXMLDocBtn.setObjectName(u"createXMLDocBtn")
        self.createXMLDocBtn.setGeometry(QRect(160, 360, 121, 41))
        self.createXMLDocBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.createXMLDocBtn.setFocusPolicy(Qt.NoFocus)
        self.createXMLDocBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 16px;\n"
"border: 0.5px solid rgb(70, 70, 70);\n"
"background:rgba(186, 223, 225, 150);\n"
"border-radius: 10px;\n"
"color: rgb(242, 255, 245)")
        self.createWorkspaceBtn = QToolButton(self.frame)
        self.createWorkspaceBtn.setObjectName(u"createWorkspaceBtn")
        self.createWorkspaceBtn.setGeometry(QRect(160, 110, 121, 41))
        self.createWorkspaceBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.createWorkspaceBtn.setFocusPolicy(Qt.NoFocus)
        self.createWorkspaceBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 16px;\n"
"border: 0.5px solid rgb(70, 70, 70);\n"
"background:rgba(186, 223, 225, 150);\n"
"border-radius: 10px;\n"
"color: rgb(242, 255, 245)")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(50, 230, 301, 121))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayoutWidget = QWidget(self.frame_2)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 61, 111))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.lyricLabel = QLabel(self.verticalLayoutWidget)
        self.lyricLabel.setObjectName(u"lyricLabel")
        self.lyricLabel.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 16px;\n"
"color: rgb(242, 255, 245)")

        self.verticalLayout.addWidget(self.lyricLabel)

        self.lyricLabel_3 = QLabel(self.verticalLayoutWidget)
        self.lyricLabel_3.setObjectName(u"lyricLabel_3")
        self.lyricLabel_3.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 16px;\n"
"color: rgb(242, 255, 245)")

        self.verticalLayout.addWidget(self.lyricLabel_3)

        self.lyricLabel_4 = QLabel(self.verticalLayoutWidget)
        self.lyricLabel_4.setObjectName(u"lyricLabel_4")
        self.lyricLabel_4.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 16px;\n"
"color: rgb(242, 255, 245)")

        self.verticalLayout.addWidget(self.lyricLabel_4)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(60, 0, 251, 111))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayoutWidget_2 = QWidget(self.frame_3)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 0, 231, 111))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.docTitleInput = QLineEdit(self.verticalLayoutWidget_2)
        self.docTitleInput.setObjectName(u"docTitleInput")
        self.docTitleInput.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 16px;\n"
"border: 0.5px solid rgb(70, 70, 70);\n"
"background:rgba(186, 223, 225, 175);\n"
"border-radius: 10px;\n"
"padding: 2px;\n"
"color: rgb(242, 255, 245)")
        self.docTitleInput.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.docTitleInput)

        self.docKeyInput = QLineEdit(self.verticalLayoutWidget_2)
        self.docKeyInput.setObjectName(u"docKeyInput")
        self.docKeyInput.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"border: 0.5px solid rgb(70, 70, 70);\n"
"background:rgba(186, 223, 225, 150);\n"
"border-radius: 10px;\n"
"padding: 2px;\n"
"color: rgb(242, 255, 245);")
        self.docKeyInput.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.docKeyInput)

        self.docTimeInput = QLineEdit(self.verticalLayoutWidget_2)
        self.docTimeInput.setObjectName(u"docTimeInput")
        self.docTimeInput.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"border: 0.5px solid rgb(70, 70, 70);\n"
"background:rgba(186, 223, 225, 150);\n"
"border-radius: 10px;\n"
"padding: 2px;\n"
"color: rgb(242, 255, 245)")
        self.docTimeInput.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.docTimeInput)

        self.workspaceNameInput = QLineEdit(self.frame)
        self.workspaceNameInput.setObjectName(u"workspaceNameInput")
        self.workspaceNameInput.setGeometry(QRect(118, 60, 221, 31))
        self.workspaceNameInput.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 16px;\n"
"border: 0.5px solid rgb(70, 70, 70);\n"
"background:rgba(186, 223, 225, 175);\n"
"border-radius: 10px;\n"
"padding: 2px;\n"
"color: rgb(242, 255, 245)")
        self.workspaceNameInput.setAlignment(Qt.AlignCenter)
        self.lyricLabel_2 = QLabel(self.frame)
        self.lyricLabel_2.setObjectName(u"lyricLabel_2")
        self.lyricLabel_2.setGeometry(QRect(50, 60, 49, 32))
        self.lyricLabel_2.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 16px;\n"
"color: rgb(242, 255, 245)")
        self.lyricLabel_5 = QLabel(self.frame)
        self.lyricLabel_5.setObjectName(u"lyricLabel_5")
        self.lyricLabel_5.setGeometry(QRect(170, 10, 111, 32))
        self.lyricLabel_5.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 17px;\n"
"color: rgb(242, 255, 245)")
        self.lyricLabel_6 = QLabel(self.frame)
        self.lyricLabel_6.setObjectName(u"lyricLabel_6")
        self.lyricLabel_6.setGeometry(QRect(160, 190, 131, 32))
        self.lyricLabel_6.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 17px;\n"
"color: rgb(242, 255, 245)")
        self.workspaceOKBtn = QToolButton(self.frame)
        self.workspaceOKBtn.setObjectName(u"workspaceOKBtn")
        self.workspaceOKBtn.setGeometry(QRect(290, 110, 51, 41))
        self.workspaceOKBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.workspaceOKBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 16px;\n"
"border: 0.5px solid rgb(70, 70, 70);\n"
"background:rgba(186, 223, 225, 150);\n"
"border-radius: 10px;\n"
"color: rgb(242, 255, 245)")
        self.docOKBtn = QToolButton(self.frame)
        self.docOKBtn.setObjectName(u"docOKBtn")
        self.docOKBtn.setGeometry(QRect(290, 360, 51, 41))
        self.docOKBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.docOKBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 16px;\n"
"border: 0.5px solid rgb(70, 70, 70);\n"
"background:rgba(186, 223, 225, 150);\n"
"border-radius: 10px;\n"
"color: rgb(242, 255, 245)")
        self.frame_4 = QFrame(WorkspacePanelWindow)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setEnabled(True)
        self.frame_4.setGeometry(QRect(0, 0, 261, 471))
        self.frame_4.setStyleSheet(u"background-image: url(\"./img/s-noah-silliman-_k9dCeh5Ca0-unsplash.jpg\")")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(0, 0, 261, 471))
        self.frame_5.setStyleSheet(u"")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.graphicsView = QGraphicsView(self.frame_5)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(30, 60, 201, 191))
        self.graphicsView.setStyleSheet(u"background-image: url('./img/s-logo.png');\n"
"background-repeat: norepeat;\n"
"border: 0px solid black;\n"
"background-color: transparent;")
        self.openBtn = QToolButton(self.frame_5)
        self.openBtn.setObjectName(u"openBtn")
        self.openBtn.setGeometry(QRect(80, 270, 121, 41))
        self.openBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.openBtn.setFocusPolicy(Qt.NoFocus)
        self.openBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 20px;\n"
"border: 0.5px solid rgb(53, 75, 98);\n"
"background: rgba(206, 227, 232, 50);\n"
"border-radius: 10px;\n"
"color: black;\n"
"background: rgba(199, 230, 245, 100)\n"
"")
        self.frame_4.raise_()
        self.frame.raise_()

        self.retranslateUi(WorkspacePanelWindow)

        QMetaObject.connectSlotsByName(WorkspacePanelWindow)
    # setupUi

    def retranslateUi(self, WorkspacePanelWindow):
        WorkspacePanelWindow.setWindowTitle(QCoreApplication.translate("WorkspacePanelWindow", u"Form", None))
        self.createXMLDocBtn.setText(QCoreApplication.translate("WorkspacePanelWindow", u"New XML", None))
        self.createWorkspaceBtn.setText(QCoreApplication.translate("WorkspacePanelWindow", u"Create", None))
        self.lyricLabel.setText(QCoreApplication.translate("WorkspacePanelWindow", u"Title", None))
        self.lyricLabel_3.setText(QCoreApplication.translate("WorkspacePanelWindow", u"Key", None))
        self.lyricLabel_4.setText(QCoreApplication.translate("WorkspacePanelWindow", u"Time", None))
        self.docTitleInput.setText("")
        self.docKeyInput.setText("")
        self.docTimeInput.setText("")
        self.workspaceNameInput.setText("")
        self.lyricLabel_2.setText(QCoreApplication.translate("WorkspacePanelWindow", u"Name", None))
        self.lyricLabel_5.setText(QCoreApplication.translate("WorkspacePanelWindow", u"Workspace", None))
        self.lyricLabel_6.setText(QCoreApplication.translate("WorkspacePanelWindow", u"XML Document", None))
        self.workspaceOKBtn.setText(QCoreApplication.translate("WorkspacePanelWindow", u"OK", None))
        self.docOKBtn.setText(QCoreApplication.translate("WorkspacePanelWindow", u"OK", None))
        self.openBtn.setText(QCoreApplication.translate("WorkspacePanelWindow", u"Open", None))
    # retranslateUi

