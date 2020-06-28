import sys
import vtk

from image_pane import ImagePane
from PyQt5.QtGui import QKeyEvent, QPixmap
from PyQt5.QtCore import QEvent, QSettings, QPointF, QSizeF, Qt
from PyQt5.QtWidgets import QMainWindow, QWidget, QGridLayout, QVBoxLayout, QHBoxLayout, QDesktopWidget, QApplication, QFrame, QPushButton, QLabel

#https://vtk.org/doc/nightly/html/classvtkRenderWindowInteractor.html
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor 

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)

        # make frame
        self.frame = QFrame()

        self.centralWidget = QWidget(self)

        gridlayout = QGridLayout(self.centralWidget)
        gridlayout.setContentsMargins(0, 0, 0, 0)
        gridlayout.setHorizontalSpacing(0)
        gridlayout.setVerticalSpacing(0)

        self.setCentralWidget(self.centralWidget)
        self.left_top_panel = QVBoxLayout()
        self.left_btm_panel = QVBoxLayout()
        self.right_top_panel = QVBoxLayout()
        self.right_btm_panel = QVBoxLayout()

        gridlayout.addLayout(self.left_top_panel, 0, 0, 1, 1)
        gridlayout.addLayout(self.left_btm_panel, 0, 1, 1, 1)
        gridlayout.addLayout(self.right_top_panel, 1, 0, 1, 1)
        gridlayout.addLayout(self.right_btm_panel, 1, 1, 1, 1)

        lt_pane = ImagePane()
        lb_pane = ImagePane('arrow')
        rt_pane = ImagePane('cube')
        rb_pane = ImagePane('sphere')

        self.left_top_panel.addWidget(lt_pane.get_widget())
        self.left_btm_panel.addWidget(lb_pane.get_widget())
        self.right_top_panel.addWidget(rt_pane.get_widget())
        self.right_btm_panel.addWidget(rb_pane.get_widget())

        desktop = QDesktopWidget()
        screen_width = desktop.screenGeometry().width()
        screen_height = desktop.screenGeometry().height()
        self.resize((QSizeF(screen_width, screen_height)).toSize())
        self.setWindowTitle('pyqt-vtk-practice')
        self.show()
        lt_pane.intial()
        lb_pane.intial()
        rt_pane.intial()
        rb_pane.intial()
        self.centralWidget.setLayout(gridlayout)
        
if __name__ == "__main__":
    # 1. we need qt widget app
    app = QApplication(sys.argv)
    # 2. pop the main window
    window = MainWindow()
    # 3. close event
    sys.exit(app.exec_())