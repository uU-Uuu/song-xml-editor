from PySide2 import QtWidgets
from PySide2.QtCore import Qt
from PySide2.QtGui import QCursor, QIcon

from ui.ui_windows.ui_dialog_windows import Ui_XMLWindow, Ui_LilyPondWindow, Ui_MessageBoxStyled

from xml_utils.xml_parser import TagNames, validate_xml


class XMLWindow(QtWidgets.QDialog, Ui_XMLWindow):
    def __init__(self):
        super(XMLWindow, self).__init__()
        self.setupUi(self)
        
        self.setWindowIcon(QIcon('ui/img/logo.png'))

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
                self.msg_box = SaveDocMessageBox()
                self.msg_box.setText('Store edited version separately?')
                self.msg_box.setWindowTitle('Saving document')
                for btn in self.msg_box.buttons():
                    btn.setCursor(QCursor(Qt.PointingHandCursor))
                reply = self.msg_box.exec_()
                if reply == QtWidgets.QMessageBox.Cancel:
                    self.XMLInfoLabel.setText('Edit mode')
                    return
                else:
                    if reply == QtWidgets.QMessageBox.Yes:
                        save_separately = True
                    elif reply == QtWidgets.QMessageBox.No:
                        save_separately = False
                    else:
                        self.XMLInfoLabel.setText('Edit mode')
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
            
   
class SaveDocMessageBox(QtWidgets.QMessageBox, Ui_MessageBoxStyled):
    def __init__(self):
        super(SaveDocMessageBox, self).__init__()
        self.setupUi(self)   
        self.setStandardButtons( QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Cancel)
        self.setDefaultButton(QtWidgets.QMessageBox.Cancel)     
        self.setWindowIcon(QIcon('ui/img/logo.png'))
        
class LilyPondWindow(QtWidgets.QDialog, Ui_LilyPondWindow):
    def __init__(self):
        super(LilyPondWindow, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('ui/img/logo.png'))
