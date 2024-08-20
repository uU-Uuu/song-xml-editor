# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'song-xml_editorMITQws.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import QCoreApplication, QMetaObject, QRect, QSize, Qt
from PySide2.QtGui import QCursor, QFont
from PySide2.QtWidgets import *

class Ui_MainWindow(object):
    def setupUi(self, mainWindow):
        if mainWindow.objectName():
            mainWindow.setObjectName(u"MainWindow")
        mainWindow.resize(1192, 859)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        mainWindow.setMaximumSize(QSize(1192, 859))
        mainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(33, 38, 42);\n"
"background-image: url('ui/img/b-noah-silliman-_k9dCeh5Ca0-unsplash.jpg');\n"
"")
        self.previewInput = QPlainTextEdit(self.centralwidget)
        self.previewInput.setObjectName(u"previewInput")
        self.previewInput.setGeometry(QRect(880, 70, 281, 161))
        font = QFont()
        font.setFamily(u"Yu Mincho Demibold")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.previewInput.setFont(font)
        self.previewInput.setStyleSheet(u"background: rgba(206, 227, 232, 120);\n"
"font: 63 9pt \"Yu Mincho Demibold\";\n"
"border: 0.5px solid rgb(70, 70, 70);\n"
"border-radius: 10px\n"
"")
        self.treeView = QTreeView(self.centralwidget)
        self.treeView.setObjectName(u"treeView")
        self.treeView.setGeometry(QRect(30, 50, 381, 781))
        font1 = QFont()
        font1.setFamily(u"Yu Mincho Light")
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(3)
        self.treeView.setFont(font1)
        self.treeView.setStyleSheet(u"background: rgba(206, 227, 232, 120);\n"
"font: 25 9.5pt \"Yu Mincho Light\";\n"
"border: 0.5px solid rgb(70, 70, 70);\n"
"border-radius: 10px;\n"
"padding: 5px;\n"
"")
        self.treeView.setTabKeyNavigation(True)
        self.sectionFrame = QFrame(self.centralwidget)
        self.sectionFrame.setObjectName(u"sectionFrame")
        self.sectionFrame.setGeometry(QRect(460, 40, 351, 91))
        self.sectionFrame.setStyleSheet(u"background: transparent;\n"
"")
        self.sectionFrame.setFrameShape(QFrame.StyledPanel)
        self.sectionFrame.setFrameShadow(QFrame.Raised)
        self.sectionName = QLineEdit(self.sectionFrame)
        self.sectionName.setObjectName(u"sectionName")
        self.sectionName.setGeometry(QRect(220, 30, 81, 41))
        self.sectionName.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"border: 0.5px solid rgb(70, 70, 70);\n"
"background: rgba(206, 227, 232, 100);\n"
"border-radius: 10px")
        self.newSectionOKBtn = QToolButton(self.sectionFrame)
        self.newSectionOKBtn.setObjectName(u"newSectionOKBtn")
        self.newSectionOKBtn.setGeometry(QRect(150, 30, 51, 41))
        self.newSectionOKBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.newSectionOKBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"border: 0.5px solid rgb(70, 70, 70);\n"
"background: rgba(206, 227, 232, 120);\n"
"border-radius: 10px")
        self.newSectionBtn = QToolButton(self.sectionFrame)
        self.newSectionBtn.setObjectName(u"newSectionBtn")
        self.newSectionBtn.setGeometry(QRect(10, 30, 121, 41))
        self.newSectionBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.newSectionBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"border: 0.5px solid rgb(70, 70, 70);\n"
"background: rgba(206, 227, 232, 120);\n"
"border-radius: 10px")
        self.sectionNameLabel = QLabel(self.sectionFrame)
        self.sectionNameLabel.setObjectName(u"sectionNameLabel")
        self.sectionNameLabel.setGeometry(QRect(230, 0, 71, 21))
        self.sectionNameLabel.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;")
        self.melPhraseFrame = QFrame(self.centralwidget)
        self.melPhraseFrame.setObjectName(u"melPhraseFrame")
        self.melPhraseFrame.setGeometry(QRect(460, 130, 351, 91))
        self.melPhraseFrame.setStyleSheet(u"background: transparent;\n"
"")
        self.melPhraseFrame.setFrameShape(QFrame.StyledPanel)
        self.melPhraseFrame.setFrameShadow(QFrame.Raised)
        self.newMelPhraseOKBtn = QToolButton(self.melPhraseFrame)
        self.newMelPhraseOKBtn.setObjectName(u"newMelPhraseOKBtn")
        self.newMelPhraseOKBtn.setGeometry(QRect(150, 30, 51, 41))
        self.newMelPhraseOKBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.newMelPhraseOKBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"border: 0.5px solid rgb(70, 70, 70);\n"
"background: rgba(206, 227, 232, 120);\n"
"border-radius: 10px")
        self.newMelPhraseBtn = QToolButton(self.melPhraseFrame)
        self.newMelPhraseBtn.setObjectName(u"newMelPhraseBtn")
        self.newMelPhraseBtn.setGeometry(QRect(10, 30, 121, 41))
        self.newMelPhraseBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.newMelPhraseBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"border: 0.5px solid rgb(70, 70, 70);\n"
"background: rgba(206, 227, 232, 120);\n"
"border-radius: 10px")
        self.lexPhraseFrame = QFrame(self.centralwidget)
        self.lexPhraseFrame.setObjectName(u"lexPhraseFrame")
        self.lexPhraseFrame.setGeometry(QRect(460, 220, 351, 91))
        self.lexPhraseFrame.setStyleSheet(u"background: transparent;\n"
"")
        self.lexPhraseFrame.setFrameShape(QFrame.StyledPanel)
        self.lexPhraseFrame.setFrameShadow(QFrame.Raised)
        self.newLexPhraseOKBtn = QToolButton(self.lexPhraseFrame)
        self.newLexPhraseOKBtn.setObjectName(u"newLexPhraseOKBtn")
        self.newLexPhraseOKBtn.setGeometry(QRect(150, 30, 51, 41))
        self.newLexPhraseOKBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.newLexPhraseOKBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"border: 0.5px solid rgb(70, 70, 70);\n"
"background: rgba(206, 227, 232, 120);\n"
"border-radius: 10px")
        self.newLexPhraseBtn = QToolButton(self.lexPhraseFrame)
        self.newLexPhraseBtn.setObjectName(u"newLexPhraseBtn")
        self.newLexPhraseBtn.setGeometry(QRect(10, 30, 121, 41))
        self.newLexPhraseBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.newLexPhraseBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"border: 0.5px solid rgb(70, 70, 70);\n"
"background: rgba(206, 227, 232, 120);\n"
"border-radius: 10px")
        self.syllableFrame = QFrame(self.centralwidget)
        self.syllableFrame.setObjectName(u"syllableFrame")
        self.syllableFrame.setGeometry(QRect(460, 310, 701, 251))
        self.syllableFrame.setStyleSheet(u"background: transparent;\n"
"")
        self.syllableFrame.setFrameShape(QFrame.StyledPanel)
        self.syllableFrame.setFrameShadow(QFrame.Raised)
        self.newSyllableBtn = QToolButton(self.syllableFrame)
        self.newSyllableBtn.setObjectName(u"newSyllableBtn")
        self.newSyllableBtn.setGeometry(QRect(10, 30, 121, 41))
        self.newSyllableBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.newSyllableBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"border: 0.5px solid rgb(70, 70, 70);\n"
"background: rgba(206, 227, 232, 120);\n"
"border-radius: 10px")
        self.newSyllableOKBtn = QToolButton(self.syllableFrame)
        self.newSyllableOKBtn.setObjectName(u"newSyllableOKBtn")
        self.newSyllableOKBtn.setGeometry(QRect(150, 30, 51, 41))
        self.newSyllableOKBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.newSyllableOKBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"border: 0.5px solid rgb(70, 70, 70);\n"
"background: rgba(206, 227, 232, 120);\n"
"border-radius: 10px")
        self.syllableLyric = QLineEdit(self.syllableFrame)
        self.syllableLyric.setObjectName(u"syllableLyric")
        self.syllableLyric.setGeometry(QRect(220, 30, 51, 41))
        self.syllableLyric.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"border: 0.5px solid rgb(70, 70, 70);\n"
"background: rgba(206, 227, 232, 100);\n"
"border-radius: 10px")
        self.syllableDottedBtn = QToolButton(self.syllableFrame)
        self.syllableDottedBtn.setObjectName(u"syllableDottedBtn")
        self.syllableDottedBtn.setGeometry(QRect(600, 190, 41, 41))
        self.syllableDottedBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.syllableDottedBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"border: 0.5px solid rgb(70, 70, 70);\n"
"background: rgba(206, 227, 232, 160);\n"
"border-radius: 10px")
        self.sharpBtn = QToolButton(self.syllableFrame)
        self.sharpBtn.setObjectName(u"sharpBtn")
        self.sharpBtn.setGeometry(QRect(600, 90, 41, 41))
        self.sharpBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.sharpBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"border: 0.5px solid rgb(70, 70, 70);\n"
"background: rgba(206, 227, 232, 160);\n"
"border-radius: 10px")
        self.flatBtn = QToolButton(self.syllableFrame)
        self.flatBtn.setObjectName(u"flatBtn")
        self.flatBtn.setGeometry(QRect(650, 90, 41, 41))
        self.flatBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.flatBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"border: 0.5px solid rgb(70, 70, 70);\n"
"background: rgba(206, 227, 232, 160);\n"
"border-radius: 10px")
        self.syllableDur16Btn = QToolButton(self.syllableFrame)
        self.syllableDur16Btn.setObjectName(u"syllableDur16Btn")
        self.syllableDur16Btn.setGeometry(QRect(420, 190, 41, 41))
        self.syllableDur16Btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.syllableDur16Btn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"border: 0.5px solid rgb(70, 70, 70);\n"
"background: rgba(206, 227, 232, 160);\n"
"border-radius: 10px")
        self.syllableDur8Btn = QToolButton(self.syllableFrame)
        self.syllableDur8Btn.setObjectName(u"syllableDur8Btn")
        self.syllableDur8Btn.setGeometry(QRect(370, 190, 41, 41))
        self.syllableDur8Btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.syllableDur8Btn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"border: 0.5px solid rgb(70, 70, 70);\n"
"background: rgba(206, 227, 232, 160);\n"
"border-radius: 10px")
        self.syllableDur4Btn = QToolButton(self.syllableFrame)
        self.syllableDur4Btn.setObjectName(u"syllableDur4Btn")
        self.syllableDur4Btn.setGeometry(QRect(320, 190, 41, 41))
        self.syllableDur4Btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.syllableDur4Btn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"border: 0.5px solid rgb(70, 70, 70);\n"
"background: rgba(206, 227, 232, 160);\n"
"border-radius: 10px")
        self.syllableDur2Btn = QToolButton(self.syllableFrame)
        self.syllableDur2Btn.setObjectName(u"syllableDur2Btn")
        self.syllableDur2Btn.setGeometry(QRect(270, 190, 41, 41))
        self.syllableDur2Btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.syllableDur2Btn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"border: 0.5px solid rgb(70, 70, 70);\n"
"background: rgba(206, 227, 232, 160);\n"
"border-radius: 10px")
        self.syllableDur1Btn = QToolButton(self.syllableFrame)
        self.syllableDur1Btn.setObjectName(u"syllableDur1Btn")
        self.syllableDur1Btn.setGeometry(QRect(220, 190, 41, 41))
        self.syllableDur1Btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.syllableDur1Btn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"border: 0.5px solid rgb(70, 70, 70);\n"
"background: rgba(206, 227, 232, 160);\n"
"border-radius: 10px")
        self.octave3Btn = QToolButton(self.syllableFrame)
        self.octave3Btn.setObjectName(u"octave3Btn")
        self.octave3Btn.setGeometry(QRect(220, 140, 41, 41))
        self.octave3Btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.octave3Btn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"border: 0.5px solid rgb(70, 70, 70);\n"
"background: rgba(206, 227, 232, 160);\n"
"border-radius: 10px")
        self.octave4Btn = QToolButton(self.syllableFrame)
        self.octave4Btn.setObjectName(u"octave4Btn")
        self.octave4Btn.setGeometry(QRect(270, 140, 41, 41))
        self.octave4Btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.octave4Btn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"border: 0.5px solid rgb(70, 70, 70);\n"
"background: rgba(206, 227, 232, 160);\n"
"border-radius: 10px")
        self.octave5Btn = QToolButton(self.syllableFrame)
        self.octave5Btn.setObjectName(u"octave5Btn")
        self.octave5Btn.setEnabled(True)
        self.octave5Btn.setGeometry(QRect(320, 140, 41, 41))
        self.octave5Btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.octave5Btn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"border: 0.5px solid rgb(70, 70, 70);\n"
"background: rgba(206, 227, 232, 160);\n"
"border-radius: 10px")
        self.octave6Btn = QToolButton(self.syllableFrame)
        self.octave6Btn.setObjectName(u"octave6Btn")
        self.octave6Btn.setGeometry(QRect(370, 140, 41, 41))
        self.octave6Btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.octave6Btn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"border: 0.5px solid rgb(70, 70, 70);\n"
"background: rgba(206, 227, 232, 160);\n"
"border-radius: 10px")
        self.CBtn = QToolButton(self.syllableFrame)
        self.CBtn.setObjectName(u"CBtn")
        self.CBtn.setGeometry(QRect(220, 90, 41, 41))
        self.CBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.CBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"border: 0.5px solid rgb(70, 70, 70);\n"
"background: rgba(206, 227, 232, 160);\n"
"border-radius: 10px")
        self.DBtn = QToolButton(self.syllableFrame)
        self.DBtn.setObjectName(u"DBtn")
        self.DBtn.setGeometry(QRect(270, 90, 41, 41))
        self.DBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.DBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"border: 0.5px solid rgb(70, 70, 70);\n"
"background: rgba(206, 227, 232, 160);\n"
"border-radius: 10px")
        self.EBtn = QToolButton(self.syllableFrame)
        self.EBtn.setObjectName(u"EBtn")
        self.EBtn.setGeometry(QRect(320, 90, 41, 41))
        self.EBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.EBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"border: 0.5px solid rgb(70, 70, 70);\n"
"background: rgba(206, 227, 232, 160);\n"
"border-radius: 10px")
        self.FBtn = QToolButton(self.syllableFrame)
        self.FBtn.setObjectName(u"FBtn")
        self.FBtn.setGeometry(QRect(370, 90, 41, 41))
        self.FBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.FBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"border: 0.5px solid rgb(70, 70, 70);\n"
"background: rgba(206, 227, 232, 160);\n"
"border-radius: 10px")
        self.GBtn = QToolButton(self.syllableFrame)
        self.GBtn.setObjectName(u"GBtn")
        self.GBtn.setGeometry(QRect(420, 90, 41, 41))
        self.GBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.GBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"border: 0.5px solid rgb(70, 70, 70);\n"
"background: rgba(206, 227, 232, 160);\n"
"border-radius: 10px")
        self.ABtn = QToolButton(self.syllableFrame)
        self.ABtn.setObjectName(u"ABtn")
        self.ABtn.setGeometry(QRect(470, 90, 41, 41))
        self.ABtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.ABtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"border: 0.5px solid rgb(70, 70, 70);\n"
"background: rgba(206, 227, 232, 160);\n"
"border-radius: 10px")
        self.BBtn = QToolButton(self.syllableFrame)
        self.BBtn.setObjectName(u"BBtn")
        self.BBtn.setGeometry(QRect(520, 90, 41, 41))
        self.BBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.BBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"border: 0.5px solid rgb(70, 70, 70);\n"
"background: rgba(206, 227, 232, 160);\n"
"border-radius: 10px")
        self.syllableDuration = QLineEdit(self.syllableFrame)
        self.syllableDuration.setObjectName(u"syllableDuration")
        self.syllableDuration.setGeometry(QRect(380, 30, 51, 41))
        self.syllableDuration.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"border: 0.5px solid rgb(70, 70, 70);\n"
"background: rgba(206, 227, 232, 100);\n"
"border-radius: 10px")
        self.syllDurationLabel = QLabel(self.syllableFrame)
        self.syllDurationLabel.setObjectName(u"syllDurationLabel")
        self.syllDurationLabel.setGeometry(QRect(370, 0, 71, 21))
        self.syllDurationLabel.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;")
        self.addSyllableNoteBtn = QToolButton(self.syllableFrame)
        self.addSyllableNoteBtn.setObjectName(u"addSyllableNoteBtn")
        self.addSyllableNoteBtn.setGeometry(QRect(440, 30, 21, 41))
        self.addSyllableNoteBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.addSyllableNoteBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"border: 0.5px solid rgb(70, 70, 70);\n"
"background: rgba(206, 227, 232, 120);\n"
"border-radius: 10px")
        self.syllablePitch = QLineEdit(self.syllableFrame)
        self.syllablePitch.setObjectName(u"syllablePitch")
        self.syllablePitch.setGeometry(QRect(320, 30, 51, 41))
        self.syllablePitch.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"border: 0.5px solid rgb(70, 70, 70);\n"
"background: rgba(206, 227, 232, 100);\n"
"border-radius: 10px")
        self.pitchLabel = QLabel(self.syllableFrame)
        self.pitchLabel.setObjectName(u"pitchLabel")
        self.pitchLabel.setGeometry(QRect(320, 0, 41, 21))
        self.pitchLabel.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;")
        self.addSyllableLyricBtn = QToolButton(self.syllableFrame)
        self.addSyllableLyricBtn.setObjectName(u"addSyllableLyricBtn")
        self.addSyllableLyricBtn.setGeometry(QRect(280, 30, 21, 41))
        self.addSyllableLyricBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.addSyllableLyricBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"border: 0.5px solid rgb(70, 70, 70);\n"
"background: rgba(206, 227, 232, 120);\n"
"border-radius: 10px")
        self.lyricLabel = QLabel(self.syllableFrame)
        self.lyricLabel.setObjectName(u"lyricLabel")
        self.lyricLabel.setGeometry(QRect(230, 0, 41, 21))
        self.lyricLabel.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;")
        self.restFrame = QFrame(self.centralwidget)
        self.restFrame.setObjectName(u"restFrame")
        self.restFrame.setGeometry(QRect(460, 560, 701, 151))
        self.restFrame.setStyleSheet(u"background: transparent;\n"
"")
        self.restFrame.setFrameShape(QFrame.StyledPanel)
        self.restFrame.setFrameShadow(QFrame.Raised)
        self.newRestBtn = QToolButton(self.restFrame)
        self.newRestBtn.setObjectName(u"newRestBtn")
        self.newRestBtn.setGeometry(QRect(10, 30, 121, 41))
        self.newRestBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.newRestBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"border: 0.5px solid rgb(70, 70, 70);\n"
"background: rgba(206, 227, 232, 120);\n"
"border-radius: 10px")
        self.newRestOKBtn = QToolButton(self.restFrame)
        self.newRestOKBtn.setObjectName(u"newRestOKBtn")
        self.newRestOKBtn.setGeometry(QRect(150, 30, 51, 41))
        self.newRestOKBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.newRestOKBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"border: 0.5px solid rgb(70, 70, 70);\n"
"background: rgba(206, 227, 232, 120);\n"
"border-radius: 10px")
        self.restDuration = QLineEdit(self.restFrame)
        self.restDuration.setObjectName(u"restDuration")
        self.restDuration.setGeometry(QRect(220, 30, 51, 41))
        self.restDuration.setCursor(QCursor(Qt.PointingHandCursor))
        self.restDuration.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"border: 0.5px solid rgb(70, 70, 70);\n"
"background: rgba(206, 227, 232, 100);\n"
"border-radius: 10px")
        self.addRestDurationBtn = QToolButton(self.restFrame)
        self.addRestDurationBtn.setObjectName(u"addRestDurationBtn")
        self.addRestDurationBtn.setGeometry(QRect(280, 30, 21, 41))
        self.addRestDurationBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.addRestDurationBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"border: 0.5px solid rgb(70, 70, 70);\n"
"background: rgba(206, 227, 232, 120);\n"
"border-radius: 10px")
        self.restDurationLabel = QLabel(self.restFrame)
        self.restDurationLabel.setObjectName(u"restDurationLabel")
        self.restDurationLabel.setGeometry(QRect(210, 0, 71, 21))
        self.restDurationLabel.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"color: black;\n"
"")
        self.restDur1Btn = QToolButton(self.restFrame)
        self.restDur1Btn.setObjectName(u"restDur1Btn")
        self.restDur1Btn.setGeometry(QRect(220, 90, 41, 41))
        self.restDur1Btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.restDur1Btn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"border: 0.5px solid rgb(70, 70, 70);\n"
"background: rgba(206, 227, 232, 160);\n"
"border-radius: 10px")
        self.restDur2Btn = QToolButton(self.restFrame)
        self.restDur2Btn.setObjectName(u"restDur2Btn")
        self.restDur2Btn.setGeometry(QRect(270, 90, 41, 41))
        self.restDur2Btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.restDur2Btn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"border: 0.5px solid rgb(70, 70, 70);\n"
"background: rgba(206, 227, 232, 160);\n"
"border-radius: 10px")
        self.restDur4Btn = QToolButton(self.restFrame)
        self.restDur4Btn.setObjectName(u"restDur4Btn")
        self.restDur4Btn.setGeometry(QRect(320, 90, 41, 41))
        self.restDur4Btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.restDur4Btn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"border: 0.5px solid rgb(70, 70, 70);\n"
"background: rgba(206, 227, 232, 160);\n"
"border-radius: 10px")
        self.restDur8Btn = QToolButton(self.restFrame)
        self.restDur8Btn.setObjectName(u"restDur8Btn")
        self.restDur8Btn.setGeometry(QRect(370, 90, 41, 41))
        self.restDur8Btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.restDur8Btn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"border: 0.5px solid rgb(70, 70, 70);\n"
"background: rgba(206, 227, 232, 160);\n"
"border-radius: 10px")
        self.restDur16Btn = QToolButton(self.restFrame)
        self.restDur16Btn.setObjectName(u"restDur16Btn")
        self.restDur16Btn.setGeometry(QRect(420, 90, 41, 41))
        self.restDur16Btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.restDur16Btn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"border: 0.5px solid rgb(70, 70, 70);\n"
"background: rgba(206, 227, 232, 160);\n"
"border-radius: 10px")
        self.restDottedBtn = QToolButton(self.restFrame)
        self.restDottedBtn.setObjectName(u"restDottedBtn")
        self.restDottedBtn.setGeometry(QRect(600, 90, 41, 41))
        self.restDottedBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.restDottedBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 16px;\n"
"border: 0.5px solid rgb(70, 70, 70);\n"
"background: rgba(206, 227, 232, 160);\n"
"border-radius: 10px")
        self.actionBtnsFrame = QFrame(self.centralwidget)
        self.actionBtnsFrame.setObjectName(u"actionBtnsFrame")
        self.actionBtnsFrame.setGeometry(QRect(660, 750, 461, 81))
        self.actionBtnsFrame.setStyleSheet(u"background: transparent;\n"
"")
        self.actionBtnsFrame.setFrameShape(QFrame.StyledPanel)
        self.actionBtnsFrame.setFrameShadow(QFrame.Raised)
        self.musicSheetBtn = QToolButton(self.actionBtnsFrame)
        self.musicSheetBtn.setObjectName(u"musicSheetBtn")
        self.musicSheetBtn.setGeometry(QRect(20, 20, 121, 41))
        self.musicSheetBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.musicSheetBtn.setFocusPolicy(Qt.NoFocus)
        self.musicSheetBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 16px;\n"
"border: 0.5px solid rgb(70, 70, 70);\n"
"background: rgba(206, 227, 232, 120);\n"
"border-radius: 10px")
        self.XMLBtn = QToolButton(self.actionBtnsFrame)
        self.XMLBtn.setObjectName(u"XMLBtn")
        self.XMLBtn.setGeometry(QRect(170, 20, 121, 41))
        self.XMLBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.XMLBtn.setFocusPolicy(Qt.NoFocus)
        self.XMLBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 16px;\n"
"border: 0.5px solid rgb(70, 70, 70);\n"
"background: rgba(206, 227, 232, 120);\n"
"border-radius: 10px")
        self.saveFileBtn = QToolButton(self.actionBtnsFrame)
        self.saveFileBtn.setObjectName(u"saveFileBtn")
        self.saveFileBtn.setGeometry(QRect(320, 20, 121, 41))
        self.saveFileBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.saveFileBtn.setMouseTracking(False)
        self.saveFileBtn.setTabletTracking(False)
        self.saveFileBtn.setFocusPolicy(Qt.NoFocus)
        self.saveFileBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 16px;\n"
"border: 0.5px solid rgb(70, 70, 70);\n"
"background: rgba(206, 227, 232, 120);\n"
"border-radius: 10px")
        self.overwriteBtn = QToolButton(self.centralwidget)
        self.overwriteBtn.setObjectName(u"overwriteBtn")
        self.overwriteBtn.setGeometry(QRect(880, 250, 121, 41))
        self.overwriteBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.overwriteBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"border: 0.5px solid rgb(70, 70, 70);\n"
"background: rgba(206, 227, 232, 120);\n"
"border-radius: 10px")
        self.saveXMLBtn = QToolButton(self.centralwidget)
        self.saveXMLBtn.setObjectName(u"saveXMLBtn")
        self.saveXMLBtn.setGeometry(QRect(1020, 250, 61, 41))
        self.saveXMLBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.saveXMLBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"border: 0.5px solid rgb(70, 70, 70);\n"
"background: rgba(206, 227, 232, 120);\n"
"border-radius: 10px")
        self.cancelXMLBtn = QToolButton(self.centralwidget)
        self.cancelXMLBtn.setObjectName(u"cancelXMLBtn")
        self.cancelXMLBtn.setGeometry(QRect(1100, 250, 61, 41))
        self.cancelXMLBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.cancelXMLBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"border: 0.5px solid rgb(70, 70, 70);\n"
"background: rgba(206, 227, 232, 120);\n"
"border-radius: 10px")
        self.deleteNodeBtn = QToolButton(self.centralwidget)
        self.deleteNodeBtn.setObjectName(u"deleteNodeBtn")
        self.deleteNodeBtn.setGeometry(QRect(380, 10, 31, 31))
        self.deleteNodeBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.deleteNodeBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 16px;\n"
"border: 0.5px solid rgb(70, 70, 70);\n"
"background: rgba(206, 227, 232, 120);\n"
"border-radius: 10px")
        self.editNodeBtn = QToolButton(self.centralwidget)
        self.editNodeBtn.setObjectName(u"editNodeBtn")
        self.editNodeBtn.setGeometry(QRect(340, 10, 31, 31))
        self.editNodeBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.editNodeBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 16px;\n"
"border: 0.5px solid rgb(70, 70, 70);\n"
"background: rgba(206, 227, 232, 120);\n"
"border-radius: 10px")
        self.backToPanelBtn = QToolButton(self.centralwidget)
        self.backToPanelBtn.setObjectName(u"backToPanelBtn")
        self.backToPanelBtn.setGeometry(QRect(30, 10, 31, 31))
        self.backToPanelBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.backToPanelBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 16px;\n"
"border: 0.5px solid rgb(70, 70, 70);\n"
"background: rgba(206, 227, 232, 120);\n"
"border-radius: 10px")
        mainWindow.setCentralWidget(self.centralwidget)
        self.actionBtnsFrame.raise_()
        self.restFrame.raise_()
        self.syllableFrame.raise_()
        self.lexPhraseFrame.raise_()
        self.melPhraseFrame.raise_()
        self.sectionFrame.raise_()
        self.treeView.raise_()
        self.previewInput.raise_()
        self.overwriteBtn.raise_()
        self.saveXMLBtn.raise_()
        self.cancelXMLBtn.raise_()
        self.deleteNodeBtn.raise_()
        self.editNodeBtn.raise_()
        self.backToPanelBtn.raise_()

        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"Song XML Editor", None))
        self.previewInput.setPlainText("")
        self.sectionName.setText("")
        self.newSectionOKBtn.setText(QCoreApplication.translate("mainWindow", u"OK", None))
        self.newSectionBtn.setText(QCoreApplication.translate("mainWindow", u"Section", None))
        self.sectionNameLabel.setText(QCoreApplication.translate("mainWindow", u" Name", None))
        self.newMelPhraseOKBtn.setText(QCoreApplication.translate("mainWindow", u"OK", None))
        self.newMelPhraseBtn.setText(QCoreApplication.translate("mainWindow", u"Melodic phrase", None))
        self.newLexPhraseOKBtn.setText(QCoreApplication.translate("mainWindow", u"OK", None))
        self.newLexPhraseBtn.setText(QCoreApplication.translate("mainWindow", u"Lexical phrase", None))
        self.newSyllableBtn.setText(QCoreApplication.translate("mainWindow", u"Syllable", None))
        self.newSyllableOKBtn.setText(QCoreApplication.translate("mainWindow", u"OK", None))
        self.syllableLyric.setText("")
        self.syllableDottedBtn.setText(QCoreApplication.translate("mainWindow", u".", None))
        self.sharpBtn.setText(QCoreApplication.translate("mainWindow", u"#", None))
        self.flatBtn.setText(QCoreApplication.translate("mainWindow", u"b", None))
        self.syllableDur16Btn.setText(QCoreApplication.translate("mainWindow", u"1/16", None))
        self.syllableDur8Btn.setText(QCoreApplication.translate("mainWindow", u"1/8", None))
        self.syllableDur4Btn.setText(QCoreApplication.translate("mainWindow", u"1/4", None))
        self.syllableDur2Btn.setText(QCoreApplication.translate("mainWindow", u"1/2", None))
        self.syllableDur1Btn.setText(QCoreApplication.translate("mainWindow", u"1/1", None))
        self.octave3Btn.setText(QCoreApplication.translate("mainWindow", u"3", None))
        self.octave4Btn.setText(QCoreApplication.translate("mainWindow", u"4", None))
        self.octave5Btn.setText(QCoreApplication.translate("mainWindow", u"5", None))
        self.octave6Btn.setText(QCoreApplication.translate("mainWindow", u"6", None))
        self.CBtn.setText(QCoreApplication.translate("mainWindow", u"C", None))
        self.DBtn.setText(QCoreApplication.translate("mainWindow", u"D", None))
        self.EBtn.setText(QCoreApplication.translate("mainWindow", u"E", None))
        self.FBtn.setText(QCoreApplication.translate("mainWindow", u"F", None))
        self.GBtn.setText(QCoreApplication.translate("mainWindow", u"G", None))
        self.ABtn.setText(QCoreApplication.translate("mainWindow", u"A", None))
        self.BBtn.setText(QCoreApplication.translate("mainWindow", u"B", None))
        self.syllableDuration.setText("")
        self.syllDurationLabel.setText(QCoreApplication.translate("mainWindow", u" Duration", None))
        self.addSyllableNoteBtn.setText(QCoreApplication.translate("mainWindow", u"+", None))
        self.syllablePitch.setText("")
        self.pitchLabel.setText(QCoreApplication.translate("mainWindow", u" Pitch", None))
        self.addSyllableLyricBtn.setText(QCoreApplication.translate("mainWindow", u"+", None))
        self.lyricLabel.setText(QCoreApplication.translate("mainWindow", u"Lyric", None))
        self.newRestBtn.setText(QCoreApplication.translate("mainWindow", u"Rest  ", None))
        self.newRestOKBtn.setText(QCoreApplication.translate("mainWindow", u"OK", None))
        self.restDuration.setText("")
        self.addRestDurationBtn.setText(QCoreApplication.translate("mainWindow", u"+", None))
        self.restDurationLabel.setText(QCoreApplication.translate("mainWindow", u" Duration", None))
        self.restDur1Btn.setText(QCoreApplication.translate("mainWindow", u"1/1", None))
        self.restDur2Btn.setText(QCoreApplication.translate("mainWindow", u"1/2", None))
        self.restDur4Btn.setText(QCoreApplication.translate("mainWindow", u"1/4", None))
        self.restDur8Btn.setText(QCoreApplication.translate("mainWindow", u"1/8", None))
        self.restDur16Btn.setText(QCoreApplication.translate("mainWindow", u"1/16", None))
        self.restDottedBtn.setText(QCoreApplication.translate("mainWindow", u".", None))
        self.musicSheetBtn.setText(QCoreApplication.translate("mainWindow", u"MusicSheet", None))
        self.XMLBtn.setText(QCoreApplication.translate("mainWindow", u"XML", None))
        self.saveFileBtn.setText(QCoreApplication.translate("mainWindow", u"Save", None))
        self.overwriteBtn.setText(QCoreApplication.translate("mainWindow", u"Overwrite", None))
        self.saveXMLBtn.setText(QCoreApplication.translate("mainWindow", u"Save", None))
        self.cancelXMLBtn.setText(QCoreApplication.translate("mainWindow", u"Cancel", None))
        self.deleteNodeBtn.setText(QCoreApplication.translate("mainWindow", u"\u2014", None))
        self.editNodeBtn.setText(QCoreApplication.translate("mainWindow", u"...", None))
        self.backToPanelBtn.setText(QCoreApplication.translate("MainWindow", u"<", None))
    # retranslateUi

