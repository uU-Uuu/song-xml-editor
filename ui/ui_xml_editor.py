# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'song-xml_editorypnOGI.ui'
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
        MainWindow.resize(1117, 862)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.newRestBtn = QToolButton(self.centralwidget)
        self.newRestBtn.setObjectName(u"newRestBtn")
        self.newRestBtn.setGeometry(QRect(410, 570, 121, 41))
        self.newRestBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"background-color: #d6def9;\n"
"border: 2px solid black;\n"
"")
        self.lexPhraseID = QLineEdit(self.centralwidget)
        self.lexPhraseID.setObjectName(u"lexPhraseID")
        self.lexPhraseID.setGeometry(QRect(620, 230, 51, 41))
        self.lexPhraseID.setStyleSheet(u"border: 2px solid black;")
        self.flatBtn = QToolButton(self.centralwidget)
        self.flatBtn.setObjectName(u"flatBtn")
        self.flatBtn.setGeometry(QRect(1050, 380, 41, 41))
        self.flatBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"background-color:#dee8fd;\n"
"border: 2px solid black;\n"
"")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(610, 540, 71, 21))
        self.label_4.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;")
        self.restDur1Btn = QToolButton(self.centralwidget)
        self.restDur1Btn.setObjectName(u"restDur1Btn")
        self.restDur1Btn.setGeometry(QRect(620, 630, 41, 41))
        self.restDur1Btn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"background-color:#d6def9;\n"
"border: 2px solid black;\n"
"")
        self.syllableDuration = QLineEdit(self.centralwidget)
        self.syllableDuration.setObjectName(u"syllableDuration")
        self.syllableDuration.setGeometry(QRect(820, 320, 51, 41))
        self.syllableDuration.setStyleSheet(u"border: 2px solid black;")
        self.restDur16Btn = QToolButton(self.centralwidget)
        self.restDur16Btn.setObjectName(u"restDur16Btn")
        self.restDur16Btn.setGeometry(QRect(820, 630, 41, 41))
        self.restDur16Btn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"background-color:#d6def9;\n"
"border: 2px solid black;\n"
"")
        self.newSectionOKBtn = QToolButton(self.centralwidget)
        self.newSectionOKBtn.setObjectName(u"newSectionOKBtn")
        self.newSectionOKBtn.setGeometry(QRect(550, 50, 51, 41))
        self.newSectionOKBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"background-color: #fbfaeb;\n"
"border: 2px solid black;\n"
"")
        self.ABtn = QToolButton(self.centralwidget)
        self.ABtn.setObjectName(u"ABtn")
        self.ABtn.setGeometry(QRect(870, 380, 41, 41))
        self.ABtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"background-color:#dee8fd;\n"
"border: 2px solid black;\n"
"")
        self.restDuration = QLineEdit(self.centralwidget)
        self.restDuration.setObjectName(u"restDuration")
        self.restDuration.setGeometry(QRect(620, 570, 51, 41))
        self.restDuration.setStyleSheet(u"border: 2px solid black;")
        self.newLexPhraseBtn = QToolButton(self.centralwidget)
        self.newLexPhraseBtn.setObjectName(u"newLexPhraseBtn")
        self.newLexPhraseBtn.setGeometry(QRect(410, 230, 121, 41))
        self.newLexPhraseBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"background-color: #e7f4f3;\n"
"border: 2px solid black;\n"
"")
        self.FBtn = QToolButton(self.centralwidget)
        self.FBtn.setObjectName(u"FBtn")
        self.FBtn.setGeometry(QRect(770, 380, 41, 41))
        self.FBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"background-color:#dee8fd;\n"
"border: 2px solid black;\n"
"")
        self.newSyllableBtn = QToolButton(self.centralwidget)
        self.newSyllableBtn.setObjectName(u"newSyllableBtn")
        self.newSyllableBtn.setGeometry(QRect(410, 320, 121, 41))
        self.newSyllableBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"background-color:#dee8fd;\n"
"border: 2px solid black;\n"
"")
        self.BBtn = QToolButton(self.centralwidget)
        self.BBtn.setObjectName(u"BBtn")
        self.BBtn.setGeometry(QRect(920, 380, 41, 41))
        self.BBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"background-color:#dee8fd;\n"
"border: 2px solid black;\n"
"")
        self.syllablePitch = QLineEdit(self.centralwidget)
        self.syllablePitch.setObjectName(u"syllablePitch")
        self.syllablePitch.setGeometry(QRect(720, 320, 51, 41))
        self.syllablePitch.setStyleSheet(u"border: 2px solid black;")
        self.syllableDur16Btn = QToolButton(self.centralwidget)
        self.syllableDur16Btn.setObjectName(u"syllableDur16Btn")
        self.syllableDur16Btn.setGeometry(QRect(820, 480, 41, 41))
        self.syllableDur16Btn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"background-color:#dee8fd;\n"
"border: 2px solid black;\n"
"")
        self.restDottedBtn = QToolButton(self.centralwidget)
        self.restDottedBtn.setObjectName(u"restDottedBtn")
        self.restDottedBtn.setGeometry(QRect(1000, 630, 41, 41))
        self.restDottedBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"background-color:#d6def9;\n"
"border: 2px solid black;\n"
"")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(630, 290, 41, 21))
        self.label.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;")
        self.syllableDur4Btn = QToolButton(self.centralwidget)
        self.syllableDur4Btn.setObjectName(u"syllableDur4Btn")
        self.syllableDur4Btn.setGeometry(QRect(720, 480, 41, 41))
        self.syllableDur4Btn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"background-color:#dee8fd;\n"
"border: 2px solid black;\n"
"")
        self.restDur8Btn = QToolButton(self.centralwidget)
        self.restDur8Btn.setObjectName(u"restDur8Btn")
        self.restDur8Btn.setGeometry(QRect(770, 630, 41, 41))
        self.restDur8Btn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"background-color:#d6def9;\n"
"border: 2px solid black;\n"
"")
        self.sharpBtn = QToolButton(self.centralwidget)
        self.sharpBtn.setObjectName(u"sharpBtn")
        self.sharpBtn.setGeometry(QRect(1000, 380, 41, 41))
        self.sharpBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"background-color:#dee8fd;\n"
"border: 2px solid black;\n"
"")
        self.octave5Btn = QToolButton(self.centralwidget)
        self.octave5Btn.setObjectName(u"octave5Btn")
        self.octave5Btn.setEnabled(True)
        self.octave5Btn.setGeometry(QRect(720, 430, 41, 41))
        self.octave5Btn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"background-color:#dee8fd;\n"
"border: 2px solid black;\n"
"")
        self.addSyllableDurationBtn = QToolButton(self.centralwidget)
        self.addSyllableDurationBtn.setObjectName(u"addSyllableDurationBtn")
        self.addSyllableDurationBtn.setGeometry(QRect(880, 320, 21, 41))
        self.addSyllableDurationBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"border: 2px solid black;\n"
"")
        self.newMelPhraseBtn = QToolButton(self.centralwidget)
        self.newMelPhraseBtn.setObjectName(u"newMelPhraseBtn")
        self.newMelPhraseBtn.setGeometry(QRect(410, 140, 121, 41))
        self.newMelPhraseBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"background-color: #fbf8dc;\n"
"border: 2px solid black;\n"
"")
        self.DBtn = QToolButton(self.centralwidget)
        self.DBtn.setObjectName(u"DBtn")
        self.DBtn.setGeometry(QRect(670, 380, 41, 41))
        self.DBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"background-color:#dee8fd;\n"
"border: 2px solid black;\n"
"")
        self.XMLBtn = QToolButton(self.centralwidget)
        self.XMLBtn.setObjectName(u"XMLBtn")
        self.XMLBtn.setGeometry(QRect(770, 750, 121, 41))
        self.XMLBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"border: 2px solid black;\n"
"")
        self.octave6Btn = QToolButton(self.centralwidget)
        self.octave6Btn.setObjectName(u"octave6Btn")
        self.octave6Btn.setGeometry(QRect(770, 430, 41, 41))
        self.octave6Btn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"background-color:#dee8fd;\n"
"border: 2px solid black;\n"
"")
        self.verticalScrollBar = QScrollBar(self.centralwidget)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setGeometry(QRect(330, 60, 20, 761))
        self.verticalScrollBar.setOrientation(Qt.Vertical)
        self.restDur2Btn = QToolButton(self.centralwidget)
        self.restDur2Btn.setObjectName(u"restDur2Btn")
        self.restDur2Btn.setGeometry(QRect(670, 630, 41, 41))
        self.restDur2Btn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"background-color:#d6def9;\n"
"border: 2px solid black;\n"
"")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(810, 290, 71, 21))
        self.label_3.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;")
        self.newMelPhraseOKBtn = QToolButton(self.centralwidget)
        self.newMelPhraseOKBtn.setObjectName(u"newMelPhraseOKBtn")
        self.newMelPhraseOKBtn.setGeometry(QRect(550, 140, 51, 41))
        self.newMelPhraseOKBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"background-color: #fbf8dc;\n"
"border: 2px solid black;\n"
"")
        self.newLexPhraseOKBtn = QToolButton(self.centralwidget)
        self.newLexPhraseOKBtn.setObjectName(u"newLexPhraseOKBtn")
        self.newLexPhraseOKBtn.setGeometry(QRect(550, 230, 51, 41))
        self.newLexPhraseOKBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"background-color: #e7f4f3;\n"
"border: 2px solid black;\n"
"")
        self.restDur4Btn = QToolButton(self.centralwidget)
        self.restDur4Btn.setObjectName(u"restDur4Btn")
        self.restDur4Btn.setGeometry(QRect(720, 630, 41, 41))
        self.restDur4Btn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"background-color:#d6def9;\n"
"border: 2px solid black;\n"
"")
        self.addRestDurationBtn = QToolButton(self.centralwidget)
        self.addRestDurationBtn.setObjectName(u"addRestDurationBtn")
        self.addRestDurationBtn.setGeometry(QRect(680, 570, 21, 41))
        self.addRestDurationBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"border: 2px solid black;\n"
"")
        self.saveBtn = QToolButton(self.centralwidget)
        self.saveBtn.setObjectName(u"saveBtn")
        self.saveBtn.setGeometry(QRect(920, 750, 121, 41))
        self.saveBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"border: 2px solid black;\n"
"")
        self.newSectionBtn = QToolButton(self.centralwidget)
        self.newSectionBtn.setObjectName(u"newSectionBtn")
        self.newSectionBtn.setGeometry(QRect(410, 50, 121, 41))
        self.newSectionBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"background-color: #fbfaeb;\n"
"border: 2px solid black;\n"
"")
        self.addSyllableLyricBtn = QToolButton(self.centralwidget)
        self.addSyllableLyricBtn.setObjectName(u"addSyllableLyricBtn")
        self.addSyllableLyricBtn.setGeometry(QRect(680, 320, 21, 41))
        self.addSyllableLyricBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"border: 2px solid black;\n"
"")
        self.GBtn = QToolButton(self.centralwidget)
        self.GBtn.setObjectName(u"GBtn")
        self.GBtn.setGeometry(QRect(820, 380, 41, 41))
        self.GBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"background-color:#dee8fd;\n"
"border: 2px solid black;\n"
"")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(630, 110, 71, 21))
        self.label_6.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;")
        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(820, 50, 261, 171))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(720, 290, 41, 21))
        self.label_2.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;")
        self.sectionName = QLineEdit(self.centralwidget)
        self.sectionName.setObjectName(u"sectionName")
        self.sectionName.setGeometry(QRect(620, 50, 81, 41))
        self.sectionName.setStyleSheet(u"border: 2px solid black;")
        self.syllableDottedBtn = QToolButton(self.centralwidget)
        self.syllableDottedBtn.setObjectName(u"syllableDottedBtn")
        self.syllableDottedBtn.setGeometry(QRect(1000, 480, 41, 41))
        self.syllableDottedBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"background-color:#dee8fd;\n"
"border: 2px solid black;\n"
"")
        self.CBtn = QToolButton(self.centralwidget)
        self.CBtn.setObjectName(u"CBtn")
        self.CBtn.setGeometry(QRect(620, 380, 41, 41))
        self.CBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"background-color:#dee8fd;\n"
"border: 2px solid black;\n"
"")
        self.addSyllablePitchBtn = QToolButton(self.centralwidget)
        self.addSyllablePitchBtn.setObjectName(u"addSyllablePitchBtn")
        self.addSyllablePitchBtn.setGeometry(QRect(780, 320, 21, 41))
        self.addSyllablePitchBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"border: 2px solid black;\n"
"")
        self.syllableDur2Btn = QToolButton(self.centralwidget)
        self.syllableDur2Btn.setObjectName(u"syllableDur2Btn")
        self.syllableDur2Btn.setGeometry(QRect(670, 480, 41, 41))
        self.syllableDur2Btn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"background-color:#dee8fd;\n"
"border: 2px solid black;\n"
"")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(630, 200, 71, 21))
        self.label_5.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(630, 20, 71, 21))
        self.label_7.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;")
        self.octave3Btn = QToolButton(self.centralwidget)
        self.octave3Btn.setObjectName(u"octave3Btn")
        self.octave3Btn.setGeometry(QRect(620, 430, 41, 41))
        self.octave3Btn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"background-color:#dee8fd;\n"
"border: 2px solid black;\n"
"")
        self.melPhraseID = QLineEdit(self.centralwidget)
        self.melPhraseID.setObjectName(u"melPhraseID")
        self.melPhraseID.setGeometry(QRect(620, 140, 51, 41))
        self.melPhraseID.setStyleSheet(u"border: 2px solid black;")
        self.musicSheetBtn = QToolButton(self.centralwidget)
        self.musicSheetBtn.setObjectName(u"musicSheetBtn")
        self.musicSheetBtn.setGeometry(QRect(620, 750, 121, 41))
        self.musicSheetBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"border: 2px solid black;\n"
"")
        self.newSyllableOKBtn = QToolButton(self.centralwidget)
        self.newSyllableOKBtn.setObjectName(u"newSyllableOKBtn")
        self.newSyllableOKBtn.setGeometry(QRect(550, 320, 51, 41))
        self.newSyllableOKBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"background-color:#dee8fd;\n"
"border: 2px solid black;\n"
"")
        self.treeView = QTreeView(self.centralwidget)
        self.treeView.setObjectName(u"treeView")
        self.treeView.setGeometry(QRect(10, 50, 341, 781))
        self.newRestOKBtn = QToolButton(self.centralwidget)
        self.newRestOKBtn.setObjectName(u"newRestOKBtn")
        self.newRestOKBtn.setGeometry(QRect(550, 570, 51, 41))
        self.newRestOKBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"background-color:#d6def9;\n"
"border: 2px solid black;\n"
"")
        self.EBtn = QToolButton(self.centralwidget)
        self.EBtn.setObjectName(u"EBtn")
        self.EBtn.setGeometry(QRect(720, 380, 41, 41))
        self.EBtn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"background-color:#dee8fd;\n"
"border: 2px solid black;\n"
"")
        self.syllableLyric = QLineEdit(self.centralwidget)
        self.syllableLyric.setObjectName(u"syllableLyric")
        self.syllableLyric.setGeometry(QRect(620, 320, 51, 41))
        self.syllableLyric.setStyleSheet(u"border: 2px solid black;")
        self.syllableDur1Btn = QToolButton(self.centralwidget)
        self.syllableDur1Btn.setObjectName(u"syllableDur1Btn")
        self.syllableDur1Btn.setGeometry(QRect(620, 480, 41, 41))
        self.syllableDur1Btn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"background-color:#dee8fd;\n"
"border: 2px solid black;\n"
"")
        self.syllableDur8Btn = QToolButton(self.centralwidget)
        self.syllableDur8Btn.setObjectName(u"syllableDur8Btn")
        self.syllableDur8Btn.setGeometry(QRect(770, 480, 41, 41))
        self.syllableDur8Btn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"background-color:#dee8fd;\n"
"border: 2px solid black;\n"
"")
        self.octave4Btn = QToolButton(self.centralwidget)
        self.octave4Btn.setObjectName(u"octave4Btn")
        self.octave4Btn.setGeometry(QRect(670, 430, 41, 41))
        self.octave4Btn.setStyleSheet(u"font: 63 8pt \"Yu Mincho Demibold\";\n"
"font-size: 15px;\n"
"background-color:#dee8fd;\n"
"border: 2px solid black;\n"
"")
        self.verticalScrollBar_2 = QScrollBar(self.centralwidget)
        self.verticalScrollBar_2.setObjectName(u"verticalScrollBar_2")
        self.verticalScrollBar_2.setGeometry(QRect(330, 60, 20, 761))
        self.verticalScrollBar_2.setOrientation(Qt.Vertical)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.newRestBtn.setText(QCoreApplication.translate("MainWindow", u"Rest", None))
        self.lexPhraseID.setText("")
        self.flatBtn.setText(QCoreApplication.translate("MainWindow", u"b", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u" Duration", None))
        self.restDur1Btn.setText(QCoreApplication.translate("MainWindow", u"1/1", None))
        self.syllableDuration.setText("")
        self.restDur16Btn.setText(QCoreApplication.translate("MainWindow", u"1/16", None))
        self.newSectionOKBtn.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.ABtn.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.restDuration.setText("")
        self.newLexPhraseBtn.setText(QCoreApplication.translate("MainWindow", u"Lexical phrase", None))
        self.FBtn.setText(QCoreApplication.translate("MainWindow", u"F", None))
        self.newSyllableBtn.setText(QCoreApplication.translate("MainWindow", u"Syllable", None))
        self.BBtn.setText(QCoreApplication.translate("MainWindow", u"B", None))
        self.syllablePitch.setText("")
        self.syllableDur16Btn.setText(QCoreApplication.translate("MainWindow", u"1/16", None))
        self.restDottedBtn.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Lyric", None))
        self.syllableDur4Btn.setText(QCoreApplication.translate("MainWindow", u"1/4", None))
        self.restDur8Btn.setText(QCoreApplication.translate("MainWindow", u"1/8", None))
        self.sharpBtn.setText(QCoreApplication.translate("MainWindow", u"#", None))
        self.octave5Btn.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.addSyllableDurationBtn.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.newMelPhraseBtn.setText(QCoreApplication.translate("MainWindow", u"Melodic phrase", None))
        self.DBtn.setText(QCoreApplication.translate("MainWindow", u"D", None))
        self.XMLBtn.setText(QCoreApplication.translate("MainWindow", u"XML", None))
        self.octave6Btn.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.restDur2Btn.setText(QCoreApplication.translate("MainWindow", u"1/2", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u" Duration", None))
        self.newMelPhraseOKBtn.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.newLexPhraseOKBtn.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.restDur4Btn.setText(QCoreApplication.translate("MainWindow", u"1/4", None))
        self.addRestDurationBtn.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.saveBtn.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.newSectionBtn.setText(QCoreApplication.translate("MainWindow", u"Section", None))
        self.addSyllableLyricBtn.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.GBtn.setText(QCoreApplication.translate("MainWindow", u"G", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u" ID", None))
        self.plainTextEdit.setPlainText(QCoreApplication.translate("MainWindow", u"", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u" Pitch", None))
        self.sectionName.setText("")
        self.syllableDottedBtn.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.CBtn.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.addSyllablePitchBtn.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.syllableDur2Btn.setText(QCoreApplication.translate("MainWindow", u"1/2", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u" ID", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u" Name", None))
        self.octave3Btn.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.melPhraseID.setText("")
        self.musicSheetBtn.setText(QCoreApplication.translate("MainWindow", u"MusicSheet", None))
        self.newSyllableOKBtn.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.newRestOKBtn.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.EBtn.setText(QCoreApplication.translate("MainWindow", u"E", None))
        self.syllableLyric.setText("")
        self.syllableDur1Btn.setText(QCoreApplication.translate("MainWindow", u"1/1", None))
        self.syllableDur8Btn.setText(QCoreApplication.translate("MainWindow", u"1/8", None))
        self.octave4Btn.setText(QCoreApplication.translate("MainWindow", u"4", None))
    # retranslateUi

