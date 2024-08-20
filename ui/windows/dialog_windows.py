from PySide2 import QtWidgets
from PySide2.QtCore import Qt
from PySide2.QtGui import QCursor

from ui.ui_windows.ui_dialog_windows import Ui_XMLWindow, Ui_LilyPondWindow, Ui_MessageBoxStyled

from xml_utils.xml_parser import TagNames, validate_xml


class XMLWindow(QtWidgets.QDialog, Ui_XMLWindow):
    def __init__(self):
        super(XMLWindow, self).__init__()
        self.setupUi(self)
        
        self.xmlEdit.setReadOnly(True)
        self.edited = False

        self.editXMLFileBtn.clicked.connect(self.edit_xml_file)
        self.saveXMLFIleBtn.clicked.connect(self.save_xml_file)
    
    def edit_xml_file(self):
        self.xmlEdit.setReadOnly(False)
        self.XMLInfoLabel.setText('Edit mode')
        self.edited = True

    def save_xml_file(self):
        data = self.xmlEdit.toPlainText()
        try:
            validate_xml(tag_name=TagNames.doc, xml_str=data)
        except Exception:
            self.XMLInfoLabel.setText('* Invalid XML')
        else:
            if self.edited:       
                self.msg_box = MessageBox()
                self.msg_box.setWindowTitle('Saving File')
                self.msg_box.setStandardButtons( QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Cancel)
                self.msg_box.setDefaultButton(QtWidgets.QMessageBox.Cancel)
                self.msg_box.setText('Store edited version separately?')
                for btn in self.msg_box.buttons():
                    btn.setCursor(QCursor(Qt.PointingHandCursor))
                
                reply = self.msg_box.exec_()
                if reply == QtWidgets.QMessageBox.Cancel:
                    return
                else:
                    if reply == QtWidgets.QMessageBox.Yes:
                        save_separately = True
                    elif reply == QtWidgets.QMessageBox.No:
                        save_separately = False
                    else:
                        return
                    save_method = [self.doc.save_file, self.doc.save_edited_file][save_separately]
            else:
                save_method = self.doc.save_file
            try:
                save_method(data)
            except:
                self.XMLInfoLabel.setText('* Could not save the file')
            else:
                self.XMLInfoLabel.setText(f'Saved')
            
   
class MessageBox(QtWidgets.QMessageBox, Ui_MessageBoxStyled):
    def __init__(self):
        super(MessageBox, self).__init__()
        self.setupUi(self)
            

class LilyPondWindow(QtWidgets.QDialog, Ui_LilyPondWindow):
    def __init__(self):
        super(LilyPondWindow, self).__init__()
        self.setupUi(self)
