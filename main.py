from PySide2 import QtWidgets
from functools import partial

from ui.ui_xml_editor import Ui_MainWindow
from tags import Melody, Section, MelPhrase, LexPhrase, Syllable, Rest


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    _pitches = {
        'CBtn': 'C',
        'DBtn': 'D',
        'EBtn': 'E', 
        'FBtn': 'F', 
        'GBtn': 'G',
        'ABtn': 'A',
        'BBtn': 'B'
    }
    _pitch_mod = {
        'sharpBtn': '#',
        'flatBtn': 'b'
    }
    _durations = {
        'syllableDur1Btn': '1/1',
        'syllableDur2Btn': '1/2',
        'syllableDur4Btn': '1/4',
        'syllableDur8Btn': '1/8',
        'syllableDur16Btn': '1/16',
        'restDur1Btn': '1/1',
        'restDur2Btn': '1/2',
        'restDur4Btn': '1/4',
        'restDur8Btn': '1/8',
        'restDur16Btn': '1/16'
    }
    _dotted = {
        'syllableDottedBtn': '.',
        'restDottedBtn': '.',
    }
    _octaves = {
        'octave3Btn': '3',
        'octave4Btn': '4',
        'octave5Btn': '5',
        'octave6Btn': '6'
    }
    _tags = {
        'newSectionOKBtn': Section, 
        'newMelPhraseOKBtn': MelPhrase,
        'newLexPhraseOKBtn': LexPhrase,
        'newSyllableOKBtn': Syllable, 
        'newRestOKBtn': Rest
    }

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self._pitchBtns = (
            self.CBtn, self.DBtn, self.EBtn, self.FBtn, self.GBtn, 
            self.ABtn, self.BBtn
        )
        self._pitchModifierBtns = (
            self.sharpBtn, self.flatBtn
        )
        self._octaveBtns = (
            self.octave3Btn, self.octave4Btn, self.octave5Btn, self.octave6Btn
        )
        self._syllableDurationBtns = (
            self.syllableDur1Btn, self.syllableDur2Btn, self.syllableDur4Btn, 
            self.syllableDur8Btn, self.syllableDur16Btn
        )
        self._restDurationBtns = (
            self.restDur1Btn, self.restDur2Btn, self.restDur4Btn, 
            self.restDur8Btn, self.restDur16Btn
        )

        self._tagBtns = (self.newSectionBtn, self.newMelPhraseBtn, self.newLexPhraseBtn,
                    self.newSyllableBtn, self.newRestBtn)
        self._inputFrames = (self.sectionFrame, self.melPhraseFrame, self.lexPhraseFrame,
                             self.syllableFrame, self.restFrame)
        self._tagOKBtns = (self.newSectionOKBtn, self.newMelPhraseOKBtn, self.newLexPhraseOKBtn,
                           self.newSyllableOKBtn, self.newRestOKBtn)
        self._tagAddBtns = (self.addSyllableLyricBtn, self.addSyllableNoteBtn, self.addRestDurationBtn)

        self._preview_tag = {'obj': None, 'frame': None}

        self.previewInput.setReadOnly(True)
        self.enable_frame_with_click()
        self.set_frames_enabled(self._inputFrames)
        self.input_btns_actions()
        self.tag_btns_actions()
        self.tag_ok_btns_actions()
        self.tag_add_btns_actions()
        self.overwrite_btn_action()


    def input_btns_actions(self):
       
        for pitchBtn in self._pitchBtns:
            pitchBtn.clicked.connect(partial(self._write_to_input, 
                                             pitchBtn.objectName(), 
                                             self.syllablePitch,
                                             self._pitches))
        for octaveBtn in self._octaveBtns:
            octaveBtn.clicked.connect(partial(self._append_to_input,
                                           octaveBtn.objectName(),
                                           self.syllablePitch,
                                           self._octaves))
        
        for modBtn in self._pitchModifierBtns:
            modBtn.clicked.connect(partial(self._append_to_input,
                                           modBtn.objectName(),
                                           self.syllablePitch,
                                           self._pitch_mod))
            
        for durBtn in self._syllableDurationBtns:
            durBtn.clicked.connect(partial(self._write_to_input,
                                           durBtn.objectName(),
                                           self.syllableDuration,
                                           self._durations))
            
        self.syllableDottedBtn.clicked.connect(partial(self._append_to_input,
                                           self.syllableDottedBtn.objectName(),
                                           self.syllableDuration,
                                           self._dotted))
        
        for durBtn in self._restDurationBtns:
            durBtn.clicked.connect(partial(self._write_to_input,
                                           durBtn.objectName(),
                                           self.restDuration,
                                           self._durations))
        
        self.restDottedBtn.clicked.connect(partial(self._append_to_input,
                                           self.restDottedBtn.objectName(),
                                           self.restDuration,
                                           self._dotted))
    
    def tag_btns_actions(self):
        for tagBtn in self._tagBtns:
            tagBtn.clicked.connect(partial(self._set_frame_enabled,
                                           tagBtn.parent(),
                                           True))

    def tag_ok_btns_actions(self):
        for okBtn in self._tagOKBtns:
            okBtn.clicked.connect(partial(self._tag_ok_btns_all, okBtn))

    def tag_add_btns_actions(self):
        for addBtn in self._tagAddBtns:
            addBtn.clicked.connect(partial(self._append_tag_attributes, addBtn))

    def enable_frame_with_click(self):
        for frame in self._inputFrames:
            for childBtn in frame.findChildren(QtWidgets.QToolButton):
                childBtn.clicked.connect(partial(self._set_frame_enabled,
                                                frame))
            for childInp in frame.findChildren(QtWidgets.QLineEdit):
                childInp.textChanged.connect(partial(self._set_frame_enabled,
                                                 frame))

    def overwrite_btn_action(self):
        self.overwriteBtn.clicked.connect(self._overwrite_XML)
        

    def _overwrite_XML(self):
        data = self.previewInput.toPlainText()
        print(data)


    def _append_tag_attributes(self, addBtn):
        frame = addBtn.parent()
        if self._preview_tag['obj']:
            if isinstance(self._preview_tag['obj'], Rest):
                data = frame.findChild(QtWidgets.QLineEdit).text()
                if data:
                    self._preview_tag['obj'].add_duration(data)

            elif isinstance(self._preview_tag['obj'], Syllable):
                data = [child.text() for child in frame.findChildren(QtWidgets.QLineEdit)]
                if data:
                    lyric, pitch, duration = data
                    if lyric:
                        self._preview_tag['obj'].add_lyric(lyric)
                    if pitch and duration:
                        self._preview_tag['obj'].add_note(pitch, duration)
    
            self.previewInput.setPlainText(self._preview_tag['obj'].write_xml(depth=0))
        
        for inp in frame.findChildren(QtWidgets.QLineEdit):
            inp.clear()
    


    def _tag_ok_btns_all(self, okBtn):
        frame = okBtn.parent()
        self._preview_input(frame, okBtn.objectName())
        for inp in frame.findChildren(QtWidgets.QLineEdit):
            inp.clear()
        self.set_frames_enabled(self._inputFrames)

    def _preview_input(self, frame, btn_name):
        if self._preview_tag['obj'] is None:
            self._preview_tag['obj'] = self._create_tag_instance(frame, btn_name)
            self._preview_tag['frame'] = frame
        self.previewInput.setPlainText(self._preview_tag['obj'].write_xml(depth=0))
        self.previewInput.setReadOnly(False)

    def _create_tag_instance(self, frame, btn_name):
        if self._tags[btn_name] == Syllable:
            data = [child.text() for child in 
                frame.findChildren(QtWidgets.QLineEdit)]
            tag_obj = self._tags[btn_name](data[0])
            tag_obj.add_note(pitch=data[2], duration=data[1])
        elif self._tags[btn_name] == Rest \
                    or self._tags[btn_name] == Section:
                data = frame.findChild(QtWidgets.QLineEdit).text()
                tag_obj = self._tags[btn_name](data)
        else:
            tag_obj = self._tags[btn_name]()
        return tag_obj


    def _set_frame_enabled(self, frame, enabled=True):
        if frame:
            if self._preview_tag['frame'] != frame:
                self._preview_tag['obj'] = None

            # if not frame.isEnabled():
            #     frame.setEnabled(enabled)
            #     for child in frame.findChildren(QtWidgets.QWidget):
            #         child.setEnabled(enabled)
            self.set_frames_enabled(self._inputFrames, False, besides=frame)


    def set_frames_enabled(self, frames=(), enabled=True, besides=None):
        if frames:
            for frame in frames:
               if frame and frame != besides:
                    frame.setEnabled(enabled)
                    for child in frame.findChildren(QtWidgets.QWidget):
                        child.setEnabled(enabled)

            
    def _write_to_input(self, btn_name, input_el, reference):
        input_el.setText(reference[btn_name])
    
    def _append_to_input(self, btn_name, input_el, reference):  
        curr_value = input_el.text()
        mods = ''
        if not curr_value:
            return None
        
        if reference is self._octaves:
            condition = int(curr_value[-1].isnumeric())
            if curr_value[-1] in ('#', 'b'):
                mods = curr_value[-1] 
                condition += 1
            try:
                condition += int(curr_value[-2].isnumeric())
            except IndexError:
                pass
                    
        elif reference is self._pitch_mod:
            condition = int(curr_value[-1] in ('#', 'b'))
        else:
            condition = int(not curr_value[-1].isnumeric())

        if condition:
            input_el.setText(curr_value[:-condition] + reference[btn_name] + mods)
        else:
            input_el.insert(reference[btn_name])
    





if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()