# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'song-xml_editorStkmhR.ui'
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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1192, 859)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalScrollBar = QScrollBar(self.centralwidget)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setGeometry(QRect(290, 60, 20, 761))
        self.verticalScrollBar.setOrientation(Qt.Vertical)
        self.previewInput = QPlainTextEdit(self.centralwidget)
        self.previewInput.setObjectName(u"previewInput")
        self.previewInput.setGeometry(QRect(880, 70, 261, 161))
        self.treeView = QTreeView(self.centralwidget)
        self.treeView.setObjectName(u"treeView")
        self.treeView.setGeometry(QRect(20, 50, 381, 781))
        self.sectionFrame = QFrame(self.centralwidget)
        self.sectionFrame.setObjectName(u"sectionFrame")
        self.sectionFrame.setGeometry(QRect(460, 40, 351, 91))
        self.sectionFrame.setFrameShape(QFrame.StyledPanel)
        self.sectionFrame.setFrameShadow(QFrame.Raised)
        self.sectionName = QLineEdit(self.sectionFrame)
        self.sectionName.setObjectName(u"sectionName")
        self.sectionName.setGeometry(QRect(220, 30, 81, 41))
        self.sectionName.setStyleSheet(u"border: 2px solid black;")
        self.newSectionOKBtn = QToolButton(self.sectionFrame)
        self.newSectionOKBtn.setObjectName(u"newSectionOKBtn")
        self.newSectionOKBtn.setGeometry(QRect(150, 30, 51, 41))
        self.newSectionOKBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"background-color: #fbfaeb;\n"
"border: 2px solid black;\n"
"")
        self.newSectionBtn = QToolButton(self.sectionFrame)
        self.newSectionBtn.setObjectName(u"newSectionBtn")
        self.newSectionBtn.setGeometry(QRect(10, 30, 121, 41))
        self.newSectionBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"background-color: #fbfaeb;\n"
"border: 2px solid black;\n"
"")
        self.sectionNameLabel = QLabel(self.sectionFrame)
        self.sectionNameLabel.setObjectName(u"sectionNameLabel")
        self.sectionNameLabel.setGeometry(QRect(230, 0, 71, 21))
        self.sectionNameLabel.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;")
        self.melPhraseFrame = QFrame(self.centralwidget)
        self.melPhraseFrame.setObjectName(u"melPhraseFrame")
        self.melPhraseFrame.setGeometry(QRect(460, 130, 351, 91))
        self.melPhraseFrame.setFrameShape(QFrame.StyledPanel)
        self.melPhraseFrame.setFrameShadow(QFrame.Raised)
        self.newMelPhraseOKBtn = QToolButton(self.melPhraseFrame)
        self.newMelPhraseOKBtn.setObjectName(u"newMelPhraseOKBtn")
        self.newMelPhraseOKBtn.setGeometry(QRect(150, 30, 51, 41))
        self.newMelPhraseOKBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"background-color: #fbf8dc;\n"
"border: 2px solid black;\n"
"")
        self.newMelPhraseBtn = QToolButton(self.melPhraseFrame)
        self.newMelPhraseBtn.setObjectName(u"newMelPhraseBtn")
        self.newMelPhraseBtn.setGeometry(QRect(10, 30, 121, 41))
        self.newMelPhraseBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"background-color: #fbf8dc;\n"
"border: 2px solid black;\n"
"")
        self.lexPhraseFrame = QFrame(self.centralwidget)
        self.lexPhraseFrame.setObjectName(u"lexPhraseFrame")
        self.lexPhraseFrame.setGeometry(QRect(460, 220, 351, 91))
        self.lexPhraseFrame.setFrameShape(QFrame.StyledPanel)
        self.lexPhraseFrame.setFrameShadow(QFrame.Raised)
        self.newLexPhraseOKBtn = QToolButton(self.lexPhraseFrame)
        self.newLexPhraseOKBtn.setObjectName(u"newLexPhraseOKBtn")
        self.newLexPhraseOKBtn.setGeometry(QRect(150, 30, 51, 41))
        self.newLexPhraseOKBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"background-color: #e7f4f3;\n"
"border: 2px solid black;\n"
"")
        self.newLexPhraseBtn = QToolButton(self.lexPhraseFrame)
        self.newLexPhraseBtn.setObjectName(u"newLexPhraseBtn")
        self.newLexPhraseBtn.setGeometry(QRect(10, 30, 121, 41))
        self.newLexPhraseBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"background-color: #e7f4f3;\n"
"border: 2px solid black;\n"
"")
        self.syllableFrame = QFrame(self.centralwidget)
        self.syllableFrame.setObjectName(u"syllableFrame")
        self.syllableFrame.setGeometry(QRect(460, 310, 701, 251))
        self.syllableFrame.setFrameShape(QFrame.StyledPanel)
        self.syllableFrame.setFrameShadow(QFrame.Raised)
        self.newSyllableBtn = QToolButton(self.syllableFrame)
        self.newSyllableBtn.setObjectName(u"newSyllableBtn")
        self.newSyllableBtn.setGeometry(QRect(10, 30, 121, 41))
        self.newSyllableBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"background-color:#dee8fd;\n"
"border: 2px solid black;\n"
"")
        self.newSyllableOKBtn = QToolButton(self.syllableFrame)
        self.newSyllableOKBtn.setObjectName(u"newSyllableOKBtn")
        self.newSyllableOKBtn.setGeometry(QRect(150, 30, 51, 41))
        self.newSyllableOKBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"background-color:#dee8fd;\n"
"border: 2px solid black;\n"
"")
        self.syllableLyric = QLineEdit(self.syllableFrame)
        self.syllableLyric.setObjectName(u"syllableLyric")
        self.syllableLyric.setGeometry(QRect(220, 30, 51, 41))
        self.syllableLyric.setStyleSheet(u"border: 2px solid black;")
        self.syllableDottedBtn = QToolButton(self.syllableFrame)
        self.syllableDottedBtn.setObjectName(u"syllableDottedBtn")
        self.syllableDottedBtn.setGeometry(QRect(600, 190, 41, 41))
        self.syllableDottedBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"background-color:#dee8fd;\n"
"border: 2px solid black;\n"
"")
        self.sharpBtn = QToolButton(self.syllableFrame)
        self.sharpBtn.setObjectName(u"sharpBtn")
        self.sharpBtn.setGeometry(QRect(600, 90, 41, 41))
        self.sharpBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"background-color:#dee8fd;\n"
"border: 2px solid black;\n"
"")
        self.flatBtn = QToolButton(self.syllableFrame)
        self.flatBtn.setObjectName(u"flatBtn")
        self.flatBtn.setGeometry(QRect(650, 90, 41, 41))
        self.flatBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"background-color:#dee8fd;\n"
"border: 2px solid black;\n"
"")
        self.syllableDur16Btn = QToolButton(self.syllableFrame)
        self.syllableDur16Btn.setObjectName(u"syllableDur16Btn")
        self.syllableDur16Btn.setGeometry(QRect(420, 190, 41, 41))
        self.syllableDur16Btn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"background-color:#dee8fd;\n"
"border: 2px solid black;\n"
"")
        self.syllableDur8Btn = QToolButton(self.syllableFrame)
        self.syllableDur8Btn.setObjectName(u"syllableDur8Btn")
        self.syllableDur8Btn.setGeometry(QRect(370, 190, 41, 41))
        self.syllableDur8Btn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"background-color:#dee8fd;\n"
"border: 2px solid black;\n"
"")
        self.syllableDur4Btn = QToolButton(self.syllableFrame)
        self.syllableDur4Btn.setObjectName(u"syllableDur4Btn")
        self.syllableDur4Btn.setGeometry(QRect(320, 190, 41, 41))
        self.syllableDur4Btn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"background-color:#dee8fd;\n"
"border: 2px solid black;\n"
"")
        self.syllableDur2Btn = QToolButton(self.syllableFrame)
        self.syllableDur2Btn.setObjectName(u"syllableDur2Btn")
        self.syllableDur2Btn.setGeometry(QRect(270, 190, 41, 41))
        self.syllableDur2Btn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"background-color:#dee8fd;\n"
"border: 2px solid black;\n"
"")
        self.syllableDur1Btn = QToolButton(self.syllableFrame)
        self.syllableDur1Btn.setObjectName(u"syllableDur1Btn")
        self.syllableDur1Btn.setGeometry(QRect(220, 190, 41, 41))
        self.syllableDur1Btn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"background-color:#dee8fd;\n"
"border: 2px solid black;\n"
"")
        self.octave3Btn = QToolButton(self.syllableFrame)
        self.octave3Btn.setObjectName(u"octave3Btn")
        self.octave3Btn.setGeometry(QRect(220, 140, 41, 41))
        self.octave3Btn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"background-color:#dee8fd;\n"
"border: 2px solid black;\n"
"")
        self.octave4Btn = QToolButton(self.syllableFrame)
        self.octave4Btn.setObjectName(u"octave4Btn")
        self.octave4Btn.setGeometry(QRect(270, 140, 41, 41))
        self.octave4Btn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"background-color:#dee8fd;\n"
"border: 2px solid black;\n"
"")
        self.octave5Btn = QToolButton(self.syllableFrame)
        self.octave5Btn.setObjectName(u"octave5Btn")
        self.octave5Btn.setEnabled(True)
        self.octave5Btn.setGeometry(QRect(320, 140, 41, 41))
        self.octave5Btn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"background-color:#dee8fd;\n"
"border: 2px solid black;\n"
"")
        self.octave6Btn = QToolButton(self.syllableFrame)
        self.octave6Btn.setObjectName(u"octave6Btn")
        self.octave6Btn.setGeometry(QRect(370, 140, 41, 41))
        self.octave6Btn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"background-color:#dee8fd;\n"
"border: 2px solid black;\n"
"")
        self.CBtn = QToolButton(self.syllableFrame)
        self.CBtn.setObjectName(u"CBtn")
        self.CBtn.setGeometry(QRect(220, 90, 41, 41))
        self.CBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"background-color:#dee8fd;\n"
"border: 2px solid black;\n"
"")
        self.DBtn = QToolButton(self.syllableFrame)
        self.DBtn.setObjectName(u"DBtn")
        self.DBtn.setGeometry(QRect(270, 90, 41, 41))
        self.DBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"background-color:#dee8fd;\n"
"border: 2px solid black;\n"
"")
        self.EBtn = QToolButton(self.syllableFrame)
        self.EBtn.setObjectName(u"EBtn")
        self.EBtn.setGeometry(QRect(320, 90, 41, 41))
        self.EBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"background-color:#dee8fd;\n"
"border: 2px solid black;\n"
"")
        self.FBtn = QToolButton(self.syllableFrame)
        self.FBtn.setObjectName(u"FBtn")
        self.FBtn.setGeometry(QRect(370, 90, 41, 41))
        self.FBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"background-color:#dee8fd;\n"
"border: 2px solid black;\n"
"")
        self.GBtn = QToolButton(self.syllableFrame)
        self.GBtn.setObjectName(u"GBtn")
        self.GBtn.setGeometry(QRect(420, 90, 41, 41))
        self.GBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"background-color:#dee8fd;\n"
"border: 2px solid black;\n"
"")
        self.ABtn = QToolButton(self.syllableFrame)
        self.ABtn.setObjectName(u"ABtn")
        self.ABtn.setGeometry(QRect(470, 90, 41, 41))
        self.ABtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"background-color:#dee8fd;\n"
"border: 2px solid black;\n"
"")
        self.BBtn = QToolButton(self.syllableFrame)
        self.BBtn.setObjectName(u"BBtn")
        self.BBtn.setGeometry(QRect(520, 90, 41, 41))
        self.BBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"background-color:#dee8fd;\n"
"border: 2px solid black;\n"
"")
        self.syllableDuration = QLineEdit(self.syllableFrame)
        self.syllableDuration.setObjectName(u"syllableDuration")
        self.syllableDuration.setGeometry(QRect(380, 30, 51, 41))
        self.syllableDuration.setStyleSheet(u"border: 2px solid black;")
        self.syllDurationLabel = QLabel(self.syllableFrame)
        self.syllDurationLabel.setObjectName(u"syllDurationLabel")
        self.syllDurationLabel.setGeometry(QRect(370, 0, 71, 21))
        self.syllDurationLabel.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;")
        self.addSyllableNoteBtn = QToolButton(self.syllableFrame)
        self.addSyllableNoteBtn.setObjectName(u"addSyllableNoteBtn")
        self.addSyllableNoteBtn.setGeometry(QRect(440, 30, 21, 41))
        self.addSyllableNoteBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"border: 2px solid black;\n"
"")
        self.syllablePitch = QLineEdit(self.syllableFrame)
        self.syllablePitch.setObjectName(u"syllablePitch")
        self.syllablePitch.setGeometry(QRect(320, 30, 51, 41))
        self.syllablePitch.setStyleSheet(u"border: 2px solid black;")
        self.pitchLabel = QLabel(self.syllableFrame)
        self.pitchLabel.setObjectName(u"pitchLabel")
        self.pitchLabel.setGeometry(QRect(320, 0, 41, 21))
        self.pitchLabel.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;")
        self.addSyllableLyricBtn = QToolButton(self.syllableFrame)
        self.addSyllableLyricBtn.setObjectName(u"addSyllableLyricBtn")
        self.addSyllableLyricBtn.setGeometry(QRect(280, 30, 21, 41))
        self.addSyllableLyricBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"border: 2px solid black;\n"
"")
        self.lyricLabel = QLabel(self.syllableFrame)
        self.lyricLabel.setObjectName(u"lyricLabel")
        self.lyricLabel.setGeometry(QRect(230, 0, 41, 21))
        self.lyricLabel.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;")
        self.restFrame = QFrame(self.centralwidget)
        self.restFrame.setObjectName(u"restFrame")
        self.restFrame.setGeometry(QRect(460, 560, 701, 151))
        self.restFrame.setFrameShape(QFrame.StyledPanel)
        self.restFrame.setFrameShadow(QFrame.Raised)
        self.newRestBtn = QToolButton(self.restFrame)
        self.newRestBtn.setObjectName(u"newRestBtn")
        self.newRestBtn.setGeometry(QRect(10, 30, 121, 41))
        self.newRestBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"background-color: #d6def9;\n"
"border: 2px solid black;\n"
"")
        self.newRestOKBtn = QToolButton(self.restFrame)
        self.newRestOKBtn.setObjectName(u"newRestOKBtn")
        self.newRestOKBtn.setGeometry(QRect(150, 30, 51, 41))
        self.newRestOKBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"background-color:#d6def9;\n"
"border: 2px solid black;\n"
"")
        self.restDuration = QLineEdit(self.restFrame)
        self.restDuration.setObjectName(u"restDuration")
        self.restDuration.setGeometry(QRect(220, 30, 51, 41))
        self.restDuration.setStyleSheet(u"border: 2px solid black;")
        self.addRestDurationBtn = QToolButton(self.restFrame)
        self.addRestDurationBtn.setObjectName(u"addRestDurationBtn")
        self.addRestDurationBtn.setGeometry(QRect(280, 30, 21, 41))
        self.addRestDurationBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"border: 2px solid black;\n"
"")
        self.restDurationLabel = QLabel(self.restFrame)
        self.restDurationLabel.setObjectName(u"restDurationLabel")
        self.restDurationLabel.setGeometry(QRect(220, 0, 71, 21))
        self.restDurationLabel.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;")
        self.restDur1Btn = QToolButton(self.restFrame)
        self.restDur1Btn.setObjectName(u"restDur1Btn")
        self.restDur1Btn.setGeometry(QRect(220, 90, 41, 41))
        self.restDur1Btn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"background-color:#d6def9;\n"
"border: 2px solid black;\n"
"")
        self.restDur2Btn = QToolButton(self.restFrame)
        self.restDur2Btn.setObjectName(u"restDur2Btn")
        self.restDur2Btn.setGeometry(QRect(270, 90, 41, 41))
        self.restDur2Btn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"background-color:#d6def9;\n"
"border: 2px solid black;\n"
"")
        self.restDur4Btn = QToolButton(self.restFrame)
        self.restDur4Btn.setObjectName(u"restDur4Btn")
        self.restDur4Btn.setGeometry(QRect(320, 90, 41, 41))
        self.restDur4Btn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"background-color:#d6def9;\n"
"border: 2px solid black;\n"
"")
        self.restDur8Btn = QToolButton(self.restFrame)
        self.restDur8Btn.setObjectName(u"restDur8Btn")
        self.restDur8Btn.setGeometry(QRect(370, 90, 41, 41))
        self.restDur8Btn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"background-color:#d6def9;\n"
"border: 2px solid black;\n"
"")
        self.restDur16Btn = QToolButton(self.restFrame)
        self.restDur16Btn.setObjectName(u"restDur16Btn")
        self.restDur16Btn.setGeometry(QRect(420, 90, 41, 41))
        self.restDur16Btn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"background-color:#d6def9;\n"
"border: 2px solid black;\n"
"")
        self.restDottedBtn = QToolButton(self.restFrame)
        self.restDottedBtn.setObjectName(u"restDottedBtn")
        self.restDottedBtn.setGeometry(QRect(600, 90, 41, 41))
        self.restDottedBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"background-color:#d6def9;\n"
"border: 2px solid black;\n"
"")
        self.actionBtnsFrame = QFrame(self.centralwidget)
        self.actionBtnsFrame.setObjectName(u"actionBtnsFrame")
        self.actionBtnsFrame.setGeometry(QRect(660, 750, 461, 81))
        self.actionBtnsFrame.setFrameShape(QFrame.StyledPanel)
        self.actionBtnsFrame.setFrameShadow(QFrame.Raised)
        self.musicSheetBtn = QToolButton(self.actionBtnsFrame)
        self.musicSheetBtn.setObjectName(u"musicSheetBtn")
        self.musicSheetBtn.setGeometry(QRect(20, 20, 121, 41))
        self.musicSheetBtn.setFocusPolicy(Qt.NoFocus)
        self.musicSheetBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"border: 2px solid black;\n"
"")
        self.XMLBtn = QToolButton(self.actionBtnsFrame)
        self.XMLBtn.setObjectName(u"XMLBtn")
        self.XMLBtn.setGeometry(QRect(170, 20, 121, 41))
        self.XMLBtn.setFocusPolicy(Qt.NoFocus)
        self.XMLBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"border: 2px solid black;\n"
"")
        self.saveFileBtn = QToolButton(self.actionBtnsFrame)
        self.saveFileBtn.setObjectName(u"saveFileBtn")
        self.saveFileBtn.setGeometry(QRect(320, 20, 121, 41))
        self.saveFileBtn.setMouseTracking(False)
        self.saveFileBtn.setTabletTracking(False)
        self.saveFileBtn.setFocusPolicy(Qt.NoFocus)
        self.saveFileBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"border: 2px solid black;\n"
"")
        self.overwriteBtn = QToolButton(self.centralwidget)
        self.overwriteBtn.setObjectName(u"overwriteBtn")
        self.overwriteBtn.setGeometry(QRect(880, 250, 121, 41))
        self.overwriteBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"border: 2px solid black;\n"
"")
        self.saveXMLBtn = QToolButton(self.centralwidget)
        self.saveXMLBtn.setObjectName(u"saveXMLBtn")
        self.saveXMLBtn.setGeometry(QRect(1020, 250, 51, 41))
        self.saveXMLBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"background-color: ;\n"
"border: 2px solid black;\n"
"")
        self.cancelXMLBtn = QToolButton(self.centralwidget)
        self.cancelXMLBtn.setObjectName(u"cancelXMLBtn")
        self.cancelXMLBtn.setGeometry(QRect(1090, 250, 51, 41))
        self.cancelXMLBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"background-color: ;\n"
"border: 2px solid black;\n"
"")
        self.deleteNodeBtn = QToolButton(self.centralwidget)
        self.deleteNodeBtn.setObjectName(u"deleteNodeBtn")
        self.deleteNodeBtn.setGeometry(QRect(370, 10, 31, 31))
        self.deleteNodeBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"border: 2px solid black;\n"
"")
        self.editNodeBtn = QToolButton(self.centralwidget)
        self.editNodeBtn.setObjectName(u"editNodeBtn")
        self.editNodeBtn.setGeometry(QRect(330, 10, 31, 31))
        self.editNodeBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 16px;\n"
"border: 2px solid black;\n"
"")
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionBtnsFrame.raise_()
        self.restFrame.raise_()
        self.syllableFrame.raise_()
        self.lexPhraseFrame.raise_()
        self.melPhraseFrame.raise_()
        self.sectionFrame.raise_()
        self.verticalScrollBar.raise_()
        self.treeView.raise_()
        self.previewInput.raise_()
        self.overwriteBtn.raise_()
        self.saveXMLBtn.raise_()
        self.cancelXMLBtn.raise_()
        self.deleteNodeBtn.raise_()
        self.editNodeBtn.raise_()
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.previewInput.setPlainText("")
        self.sectionName.setText("")
        self.newSectionOKBtn.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.newSectionBtn.setText(QCoreApplication.translate("MainWindow", u"Section", None))
        self.sectionNameLabel.setText(QCoreApplication.translate("MainWindow", u" Name", None))
        self.newMelPhraseOKBtn.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.newMelPhraseBtn.setText(QCoreApplication.translate("MainWindow", u"Melodic phrase", None))
        self.newLexPhraseOKBtn.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.newLexPhraseBtn.setText(QCoreApplication.translate("MainWindow", u"Lexical phrase", None))
        self.newSyllableBtn.setText(QCoreApplication.translate("MainWindow", u"Syllable", None))
        self.newSyllableOKBtn.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.syllableLyric.setText("")
        self.syllableDottedBtn.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.sharpBtn.setText(QCoreApplication.translate("MainWindow", u"#", None))
        self.flatBtn.setText(QCoreApplication.translate("MainWindow", u"b", None))
        self.syllableDur16Btn.setText(QCoreApplication.translate("MainWindow", u"1/16", None))
        self.syllableDur8Btn.setText(QCoreApplication.translate("MainWindow", u"1/8", None))
        self.syllableDur4Btn.setText(QCoreApplication.translate("MainWindow", u"1/4", None))
        self.syllableDur2Btn.setText(QCoreApplication.translate("MainWindow", u"1/2", None))
        self.syllableDur1Btn.setText(QCoreApplication.translate("MainWindow", u"1/1", None))
        self.octave3Btn.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.octave4Btn.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.octave5Btn.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.octave6Btn.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.CBtn.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.DBtn.setText(QCoreApplication.translate("MainWindow", u"D", None))
        self.EBtn.setText(QCoreApplication.translate("MainWindow", u"E", None))
        self.FBtn.setText(QCoreApplication.translate("MainWindow", u"F", None))
        self.GBtn.setText(QCoreApplication.translate("MainWindow", u"G", None))
        self.ABtn.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.BBtn.setText(QCoreApplication.translate("MainWindow", u"B", None))
        self.syllableDuration.setText("")
        self.syllDurationLabel.setText(QCoreApplication.translate("MainWindow", u" Duration", None))
        self.addSyllableNoteBtn.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.syllablePitch.setText("")
        self.pitchLabel.setText(QCoreApplication.translate("MainWindow", u" Pitch", None))
        self.addSyllableLyricBtn.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.lyricLabel.setText(QCoreApplication.translate("MainWindow", u"Lyric", None))
        self.newRestBtn.setText(QCoreApplication.translate("MainWindow", u"Rest", None))
        self.newRestOKBtn.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.restDuration.setText("")
        self.addRestDurationBtn.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.restDurationLabel.setText(QCoreApplication.translate("MainWindow", u" Duration", None))
        self.restDur1Btn.setText(QCoreApplication.translate("MainWindow", u"1/1", None))
        self.restDur2Btn.setText(QCoreApplication.translate("MainWindow", u"1/2", None))
        self.restDur4Btn.setText(QCoreApplication.translate("MainWindow", u"1/4", None))
        self.restDur8Btn.setText(QCoreApplication.translate("MainWindow", u"1/8", None))
        self.restDur16Btn.setText(QCoreApplication.translate("MainWindow", u"1/16", None))
        self.restDottedBtn.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.musicSheetBtn.setText(QCoreApplication.translate("MainWindow", u"MusicSheet", None))
        self.XMLBtn.setText(QCoreApplication.translate("MainWindow", u"XML", None))
        self.saveFileBtn.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.overwriteBtn.setText(QCoreApplication.translate("MainWindow", u"Overwrite", None))
        self.saveXMLBtn.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.cancelXMLBtn.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.deleteNodeBtn.setText(QCoreApplication.translate("MainWindow", u"\u2014", None))
        self.editNodeBtn.setText(QCoreApplication.translate("MainWindow", u"...", None))
    # retranslateUi


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


# import img_rc

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
        self.frame.setStyleSheet(u"background-image: url('./img/noah-silliman-_k9dCeh5Ca0-unsplash.jpg');\n"
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

