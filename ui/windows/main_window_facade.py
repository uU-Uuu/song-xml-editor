from PySide2 import QtWidgets
from regex import F

from ui.windows.main_window import MainWindowGen
from ui.windows.home_panel_window import WorkspacePanelWindow

        
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
        self.save_doc_btn_action()
        self.music_sheet_btn_action()
        self.delete_node_btn_action()
        self.edit_node_btn_action()
        self.back_to_panel_btn_action()