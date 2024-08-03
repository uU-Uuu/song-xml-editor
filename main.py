from PySide2 import QtWidgets
from functools import partial

from ui.ui_xml_editor import Ui_MainWindow


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
       
        for pitchBtn in self._pitchBtns:
            pitchBtn.clicked.connect(partial(self.write_to_input, 
                                             pitchBtn.objectName(), 
                                             self.syllablePitch,
                                             self._pitches))
        for octaveBtn in self._octaveBtns:
            octaveBtn.clicked.connect(partial(self.append_to_input,
                                           octaveBtn.objectName(),
                                           self.syllablePitch,
                                           self._octaves))
        
        for modBtn in self._pitchModifierBtns:
            modBtn.clicked.connect(partial(self.append_to_input,
                                           modBtn.objectName(),
                                           self.syllablePitch,
                                           self._pitch_mod))
            
        for durBtn in self._syllableDurationBtns:
            durBtn.clicked.connect(partial(self.write_to_input,
                                           durBtn.objectName(),
                                           self.syllableDuration,
                                           self._durations))
            
        self.syllableDottedBtn.clicked.connect(partial(self.append_to_input,
                                           self.syllableDottedBtn.objectName(),
                                           self.syllableDuration,
                                           self._dotted))
            
        
        for durBtn in self._restDurationBtns:
            durBtn.clicked.connect(partial(self.write_to_input,
                                           durBtn.objectName(),
                                           self.restDuration,
                                           self._durations))
        
        self.restDottedBtn.clicked.connect(partial(self.append_to_input,
                                           self.restDottedBtn.objectName(),
                                           self.restDuration,
                                           self._dotted))
            
            
       
            
    def write_to_input(self, btn_name, input_el, reference):
        input_el.setText(reference[btn_name])
    
    def append_to_input(self, btn_name, input_el, reference):  
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