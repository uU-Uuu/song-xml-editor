from PySide2 import QtWidgets

from ui.windows.splash_window import SplashWindow
from ui.windows.home_panel_window import WorkspacePanelWindow
    

if __name__ == '__main__':
    import ctypes
    myappid = 'mycompany.myproduct.subproduct.version'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    app = QtWidgets.QApplication([])

    splash = SplashWindow()
    splash.show()

    import time
    time.sleep(3)
    splash.close()

    workspace_panel = WorkspacePanelWindow()
    workspace_panel.show()

    app.exec_()