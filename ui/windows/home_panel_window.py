from PySide2 import QtWidgets
from PySide2.QtGui import QIcon
import os

from ui.ui_windows.ui_home_panel_window import Ui_WorkspacePanelWindow

from xml_utils.doc_structure import Workspace, XMLDoc


class WorkspacePanelWindow(QtWidgets.QWidget, Ui_WorkspacePanelWindow):
    def __init__(self):
        super(WorkspacePanelWindow, self).__init__()
        self.setupUi(self)
        self.move(600, 260)
        self.setWindowIcon(QIcon('../img/logo.png'))

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
                                            self, 'Open File', '../../', 
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
            from ui.windows.main_window_facade import MainWindow

            self.main_window = MainWindow()
            self.main_window.doc = self.doc
            self.main_window.show()
            self.close()



