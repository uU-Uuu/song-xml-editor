from traceback import print_tb
from PySide2 import QtWidgets
from PySide2.QtCore import Qt
from PySide2.QtGui import (QStandardItemModel, QStandardItem, 
                           QFont, QColor, QCursor, QIcon, QPalette)
from functools import partial
from copy import deepcopy
import os

from ui.main_window import Ui_MainWindow
from ui.dialog_windows import Ui_XMLWindow, Ui_LilyPondWindow
from ui.splash_window import Ui_SplashWindow
from ui.home_panel_window import Ui_WorkspacePanelWindow

from tags import Melody, Section, MelPhrase, LexPhrase, Syllable, Rest
from xml_parser import TagNames, SCHEMAS, validate_xml, XMLValidationError, InvalidXMLInputProvided
from constants import PITCHES, PITCH_MOD, DURATIONS, DOTTED, OCTAVES, TAGS_FACTORY
from doc_structure import Workspace, XMLDoc


class MainWindowGen(QtWidgets.QMainWindow, Ui_MainWindow):
    _pitches = deepcopy(PITCHES)
    _pitch_mod = deepcopy(PITCH_MOD)
    _durations = deepcopy(DURATIONS)
    _dotted = deepcopy(DOTTED)
    _octaves = deepcopy(OCTAVES)
    _tags_factory = deepcopy(TAGS_FACTORY)
    _tags = deepcopy(TagNames)

    def __init__(self):
        super(MainWindowGen, self).__init__()
        self.setupUi(self)

        self.setWindowIcon(QIcon('img/logo.png'))


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
        self._edit_mode = False


        self.previewInput.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.previewInput.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.treeView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.treeView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.doc = None
        self.melody = Melody()



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
        self.overwriteBtn.clicked.connect(self._overwrite_xml)

    def save_xml_btn_action(self):
        self.saveXMLBtn.clicked.connect(self._add_xml_item)

    def cancel_xml_btn_action(self):
        self.cancelXMLBtn.clicked.connect(self._cancel_xml)

    def xml_btn_action(self):
        self.XMLBtn.clicked.connect(self._get_xml_doc)

    def music_sheet_btn_action(self):
        self.musicSheetBtn.clicked.connect(self._get_lilypond_img)

    def delete_node_btn_action(self):
        self.deleteNodeBtn.clicked.connect(self._delete_selected_node)

    def edit_node_btn_action(self):
        self.editNodeBtn.clicked.connect(self._edit_selected_node)

    def _cancel_xml(self):
        self._preview_tag['obj'] = None
        self.previewInput.clear()
        self.set_frames_enabled(self._inputFrames)


    def _overwrite_xml(self, tag_name=''):
        data = self.previewInput.toPlainText()
        try:
            tag_name = self._preview_tag['obj'].tag_name
            validate_xml(tag_name, xml_str=data)
            schema = SCHEMAS[TagNames.by_tag(tag_name)]
            if type(self._preview_tag['obj']) in (Section, MelPhrase, LexPhrase, Syllable, Rest):
                data_dict = schema.to_dict(data)
                if data_dict:
                    if isinstance(self._preview_tag['obj'], Syllable):
                        if data_dict['lyric']:
                            self._preview_tag['obj'].lyric = data_dict['lyric']
                        else:
                            self._preview_tag['obj'].lyric = ''
                        zipped = zip(data_dict['pitch'], data_dict['duration'])
                        self._preview_tag['obj'].notes = [
                            {'pitch': pitch, 'duration': duration}
                            if pitch and duration 
                            else {'pitch': '', 'duration': ''} 
                            for pitch, duration in zipped
                        ]
                    else:

                        for key in data_dict.keys():
                            self._preview_tag['obj'].__dict__[key.strip('@')] = data_dict[key]
                    if type(self._preview_tag['obj']) in (MelPhrase, LexPhrase):
                        self._preview_tag['obj'].reset_counter(data_dict[f'@{key}'])

        except Exception as e:
            pass
        self.set_frames_enabled(self._inputFrames)


    def _append_tag_attributes(self, addBtn):
        frame = addBtn.parent()
        if self._preview_tag['obj']:
            if isinstance(self._preview_tag['obj'], Rest):
                data = frame.findChild(QtWidgets.QLineEdit).text()
                if data:
                    self._preview_tag['obj'].add_duration(data)
                note = False

            elif isinstance(self._preview_tag['obj'], Syllable):
                data = [child.text() for child in frame.findChildren(QtWidgets.QLineEdit)]

                if data:
                    lyric, duration, pitch = data
                    if lyric:
                        self._preview_tag['obj'].add_lyric(lyric)
                    note = not(bool(pitch) and bool(duration))
                    if not note:
                        self._preview_tag['obj'].add_note(pitch=pitch, duration=duration)
    
            self.previewInput.setPlainText(self._preview_tag['obj'].write_xml(depth=0))
        
            if not note:
                for inp in frame.findChildren(QtWidgets.QLineEdit):
                    inp.clear()
    

    def _tag_ok_btns_all(self, okBtn='', frame=''):
        frame = okBtn.parent()
        self._preview_input(frame, okBtn.objectName())
        for inp in frame.findChildren(QtWidgets.QLineEdit):
            inp.clear()
        self.set_frames_enabled(self._inputFrames)

    def _preview_input(self, frame, btn_name):
        self._preview_tag['obj'] = self._create_tag_instance(frame, btn_name)
        self._preview_tag['frame'] = frame
        self.previewInput.setPlainText(self._preview_tag['obj'].write_xml(depth=0))
        self.previewInput.setReadOnly(False)

    def _create_tag_instance(self, frame, btn_name):
        if self._tags_factory[btn_name] == Syllable:
            data = [child.text() for child in 
                frame.findChildren(QtWidgets.QLineEdit)]
            tag_obj = self._tags_factory[btn_name](data[0])
            tag_obj.add_note(pitch=data[2], duration=data[1])
        elif self._tags_factory[btn_name] == Rest \
                    or self._tags_factory[btn_name] == Section:
                data = frame.findChild(QtWidgets.QLineEdit).text()
                tag_obj = self._tags_factory[btn_name](data)
        else:
            tag_obj = self._tags_factory[btn_name]()
        return tag_obj


    def _set_frame_enabled(self, frame, enabled=True):
        if frame:
            if not self._edit_mode and self._preview_tag['frame'] != frame:
                self._preview_tag['obj'] = None
            self.set_frames_enabled(self._inputFrames, enabled=not enabled, besides=frame)


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


    def set_up_tree(self):
        self.treeModel = QStandardItemModel()
        self.treeModel.setHorizontalHeaderLabels(['', ''])
        self.treeView.setModel(self.treeModel)
        self.treeView.setColumnWidth(0, 200)
        self.treeView.header().hide()

        rootNode = self.treeModel.invisibleRootItem()
        melodyNode= (StandardItem(obj=self.melody, txt=self.melody.tag_name),
                     StandardItem(obj=self.melody)
        )
        rootNode.appendRow([melodyNode[0], melodyNode[1]])
        self._last_tags = {1: self.melody, 2: None, 3: None, 4: None, 5: None}
        self._last_nodes = {1: melodyNode[0], 2: None, 3: None, 4: None, 5: None}
        self._last_node = melodyNode[0]
        self.treeView.expandAll()


    
    def _add_xml_item(self, obj=None, parent=None):
        if obj is None:
            obj = self._preview_tag['obj']
                
        if obj and not parent:
            curr_node = (StandardItem(obj=obj, txt=obj.tag_name), 
                        StandardItem(obj=obj, txt=obj.values_())
            )
            if not self._edit_mode:

                if obj.depth == self._last_node.obj.depth + 1:
                    parent_node = self._last_node
                    
                elif obj.depth <= self._last_node.obj.depth:
                    parent_node = self._last_nodes[obj.depth-1]
                
                else:
                    return
            
                parent_node.appendRow([curr_node[0], curr_node[1]])
                self._last_tags[obj.depth-1].add_child(obj)
                self._last_tags[obj.depth] = obj
                self._last_nodes[obj.depth] = curr_node[0]
                self._last_node = curr_node[0]
            else:
                self._save_edited_node(curr_node)
                self._edit_mode = False

        self.treeView.expandAll()
        self._cancel_xml()

    

    def _delete_selected_node(self):
        if self._edit_mode:
                self._edit_mode = False
        try:
            selected_node = self.treeView.selectedIndexes()[0]
            item = self.treeModel.itemFromIndex(selected_node)
            parent = self.treeModel.itemFromIndex(selected_node.parent())
            if not isinstance(item.obj, Melody):
                self.treeModel.removeRow(selected_node.row(), selected_node.parent())
                parent.obj.delete_child(item.obj)
        except IndexError:
            pass


    def _edit_selected_node(self):
        try:
            selected_node = self.treeView.selectedIndexes()[0]
            selected_item = self.treeModel.itemFromIndex(selected_node)
            if not isinstance(selected_item.obj, Melody):
                indx = self.treeView.selectedIndexes()[0]
                if indx:
                    self._selected_indx = self.treeView.selectedIndexes()[0]
                    self._preview_tag['obj'] = selected_item.obj
                    self.previewInput.setPlainText(selected_item.obj.write_xml_plain())
                    self._edit_mode = True
        except Exception as e:
            pass

    def _save_edited_node(self, edited_node):
        tag_item = self.treeModel.itemFromIndex(self._selected_indx)
        value_item = self.treeModel.itemFromIndex(self._selected_indx.siblingAtColumn(1))
        if type(tag_item.obj) == type(edited_node[0].obj):
            tag_item.obj = value_item.obj = edited_node[0].obj
            value_item.edit_value()
        self._edit_mode = False

    def _get_xml_doc(self):
        indent='    '
        from_file_str = self.doc.read_file(to_indent=indent) 
        meta, closing, from_scratch = self._handle_loaded_file_xml(from_file_str)
        new_xml_str = self._last_nodes[1].obj.write_xml(indent=indent)

        if from_scratch:
            xml_str = meta + new_xml_str + closing
        else:
            xml_str = meta \
                    + new_xml_str.replace('<melody>', '').replace('</melody>', '').rstrip('\t').rstrip(' ') \
                    + closing
        self.xml_window = XMLWindow()
        self.xml_window.show()
        self.xml_window.doc = self.doc
        self.xml_window.xmlEdit.setPlainText(XMLDoc.delete_empty_lines(xml_str))

    def _handle_loaded_file_xml(self, file_xml):
        from_scratch = 'melody' not in file_xml
        if from_scratch:
            meta, closing = file_xml.split('</doc>')[0], '\n</doc>'
        else:
            meta, doc_closing = file_xml.split('</melody>')
            closing = f'  </melody>\n{doc_closing}'
        return meta, closing, from_scratch

    
    def _get_lilypond_img(self):
        self.lilypond_window = LilyPondWindow()
        self.lilypond_window.show()


        
class MainWindow(MainWindowGen):
     def __init__(self):
        super(MainWindow, self).__init__()

        self.previewInput.setReadOnly(True)
        self.enable_frame_with_click()
        self.set_frames_enabled(self._inputFrames)
        self.input_btns_actions()
        self.tag_btns_actions()
        self.tag_ok_btns_actions()
        self.tag_add_btns_actions()
        self.overwrite_btn_action()
        self.save_xml_btn_action()
        self.cancel_xml_btn_action()
        self.set_up_tree()
        self.xml_btn_action()
        self.music_sheet_btn_action()
        self.delete_node_btn_action()
        self.edit_node_btn_action()


class StandardItem(QStandardItem):
    def __init__(self, obj, txt='', font_size=8, set_bold=False, set_editable=False, color=QColor(0, 0, 0)):
        super().__init__()
        fnt = QFont('Open Sans', font_size)
        fnt.setBold(set_bold)
        self.setFont(fnt)
        self.setForeground(color)
        self.setEditable(True)
        self.setFont(QFont("Yu Mincho Demibold", 8.5))
        self.obj = obj
        self.setText(txt)
        self.setEditable(set_editable)

    def edit_value(self, txt=''):
        if not txt:
            self.setText(self.obj.values_())
        else:
            self.setText(txt)

    def __repr__(self):
        return repr(self.obj)
    

class XMLWindow(QtWidgets.QDialog, Ui_XMLWindow):
    def __init__(self):
        super(XMLWindow, self).__init__()
        self.setupUi(self)
        
        self.xmlEdit.setReadOnly(True)

        self.editXMLFileBtn.clicked.connect(self.edit_xml_file)
        self.saveXMLFIleBtn.clicked.connect(self.save_xml_file)
    
    def edit_xml_file(self):
        self.xmlEdit.setReadOnly(False)
        self.XMLInfoLabel.setText('Edit mode')

    def save_xml_file(self):
        data = self.xmlEdit.toPlainText()
        try:
            validate_xml(tag_name=TagNames.doc, xml_str=data)
        except Exception:
            self.XMLInfoLabel.setText('* Invalid XML')
        else:
            reply = QtWidgets.QMessageBox.question(self, 'Save',
                                                'Store edited version separately?',
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                QtWidgets.QMessageBox.No)
            save_separately = reply == QtWidgets.QMessageBox.Yes
            save_method = [self.doc.save_file, self.doc.save_edited_file][save_separately]
                
            try:
                saved_path = save_method(data)
            except:
                self.XMLInfoLabel.setText('* Could not save the file')
            else:
                self.XMLInfoLabel.setText(f'Saved')
   

class LilyPondWindow(QtWidgets.QDialog, Ui_LilyPondWindow):
    def __init__(self):
        super(LilyPondWindow, self).__init__()
        self.setupUi(self)

class SplashWindow(QtWidgets.QSplashScreen, Ui_SplashWindow):
    def __init__(self):
        super(SplashWindow, self).__init__()
        self.setupUi(self)
        self.move(600, 260)


class WorkspacePanelWindow(QtWidgets.QWidget, Ui_WorkspacePanelWindow):
    def __init__(self):
        super(WorkspacePanelWindow, self).__init__()
        self.setupUi(self)
        self.move(600, 260)
        self.setWindowIcon(QIcon('img/logo.png'))

        self._valid_dir = False
        self._enable_doc_creation(enabled=False)

        self.openBtn.clicked.connect(self._open_file_dialog)

        self.openWorkspaceBtn.clicked.connect(self._open_workspace_dialog)
        self.createWorkspaceBtn.clicked.connect(self._open_directory_dialog)
        self.workspaceOKBtn.clicked.connect(self._confirm_worspace_creation)

        self.createXMLDocBtn.clicked.connect(self._create_xml_doc)
        self.docOKBtn.clicked.connect(self._confirm_doc_creation)



    def _enable_doc_creation(self, enabled=True):
        self.docKeyInput.setEnabled(enabled)
        self.docTitleInput.setEnabled(enabled)
        self.docTimeInput.setEnabled(enabled)
        self.createXMLDocBtn.setEnabled(enabled)
        self.docOKBtn.setEnabled(enabled)

    def _open_file_dialog(self):
        f_path, _ = QtWidgets.QFileDialog.getOpenFileName(
                                            self, 'Open File', '', 
                                            'XML Files (*.xml);; XML Files (*.xml)')
        if f_path:
            name = os.path.basename(f_path)
            self.doc = XMLDoc(filename=name, path=f_path)
            self._open_xml_editor_window()

    def _open_workspace_dialog(self):
        self._directory = QtWidgets.QFileDialog.getExistingDirectory(
                                        self, 'Select Workspace Directory')
        if self._directory:
            self._name, _ = os.path.splitext(os.path.basename(self._directory))
            if self._name:
                self.workspaceNameInput.setText(self._name)
            self._valid_dir = True
        else:
            self.infoLabel.setText('* no directory provided')

    def _open_directory_dialog(self):
        self._valid_dir = False
        self._name = self.workspaceNameInput.text()
        if self._name:
            self._directory = QtWidgets.QFileDialog.getExistingDirectory(
                                        self, 'Select Directory')
            if self._directory:
                self._valid_dir = True
        else:
            self.infoLabel.setText('* no name provided')

    def _confirm_worspace_creation(self):
        if self._valid_dir:
            self.infoLabel.clear()
            self.workspaceNameInput.clear()
            self.workspace = Workspace(self._name, self._directory)
            self._enable_doc_creation()
            self.infoLabel.setText(self._name)
        else:
            self.infoLabel.setText('* no directory provided')


    def _create_xml_doc(self):
        self.infoLabel.clear()
        title, key, time_s = [inp.text() for inp in 
                            (self.docTitleInput, self.docKeyInput, self.docTimeInput)]
        f_path, _ = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File', 
                                                        f'{self.workspace.base_directory}/{title}',
                                                     'All Files (*);; XML Files (*.xml)') 
        name = os.path.basename(f_path)
        self.doc = XMLDoc(filename=name, path=self.workspace.base_directory, title=title, key=key, time_signature=time_s)


    def _confirm_doc_creation(self):
        try:
            self.doc.create()
        except Exception:
            self.infoLabel.setText('* invalid filename or path')
        else:
            self._open_xml_editor_window()
            self.workspace.add_documents(self.doc)

    def _open_xml_editor_window(self):
            self.main_window = MainWindow()
            self.main_window.doc = self.doc
            self.main_window.show()
            self.close()




    

if __name__ == '__main__':
    import ctypes
    myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    app = QtWidgets.QApplication([])

    splash = SplashWindow()
    splash.show()

    import time
    time.sleep(3)
    splash.close()

    workspace_panel = WorkspacePanelWindow()
    workspace_panel.show()

    # window = MainWindow()
    # window.show()
    app.exec_()