import sys
import vtk

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
        self.viewer_left_top = QWidget()
        self.viewer_left_btm = QWidget()
        self.viewer_right_top = QWidget()
        self.viewer_right_btm = QWidget()
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

        # make vtk widget
        self.vtk_left_top = QVTKRenderWindowInteractor(self.viewer_left_top)
        self.vtk_left_btm = QVTKRenderWindowInteractor(self.viewer_left_btm)
        self.vtk_right_top = QVTKRenderWindowInteractor(self.viewer_right_top)
        self.vtk_right_btm = QVTKRenderWindowInteractor(self.viewer_right_btm)

        self.left_top_panel.addWidget(self.viewer_left_top)
        self.left_btm_panel.addWidget(self.viewer_left_btm)
        self.right_top_panel.addWidget(self.viewer_right_top)
        self.right_btm_panel.addWidget(self.viewer_right_btm)
        
        self.centralWidget.setLayout(gridlayout)

        self.renderer = vtk.vtkRenderer()
        self.vtk_left_top.GetRenderWindow().AddRenderer(self.renderer)
        self.vtk_left_btm.GetRenderWindow().AddRenderer(self.renderer)
        self.vtk_right_top.GetRenderWindow().AddRenderer(self.renderer)
        self.vtk_right_btm.GetRenderWindow().AddRenderer(self.renderer)
        self.vtk_left_top_ren = self.vtk_left_top.GetRenderWindow().GetInteractor()
        self.vtk_left_btm_ren = self.vtk_left_btm.GetRenderWindow().GetInteractor()
        self.vtk_right_top_ren = self.vtk_right_top.GetRenderWindow().GetInteractor()
        self.vtk_right_btm_ren = self.vtk_right_btm.GetRenderWindow().GetInteractor()

        # Create source
        source = vtk.vtkCylinderSource()
        source.SetCenter(0, 0, 0)
        source.SetRadius(5.0)
        
        # Create a mapper
        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputConnection(source.GetOutputPort())
        
        # Create an actor
        actor = vtk.vtkActor()
        actor.SetMapper(mapper)

        self.renderer.AddActor(actor)

        self.renderer.ResetCamera()

        desktop = QDesktopWidget()
        screen_width = desktop.screenGeometry().width()
        screen_height = desktop.screenGeometry().height()
        self.resize((QSizeF(screen_width, screen_height)).toSize())
        self.setWindowTitle('pyqt-vtk-practice')
        self.show()

        self.vtk_left_top_ren.Initialize()
        self.vtk_left_btm_ren.Initialize()
        self.vtk_right_top_ren.Initialize()
        self.vtk_right_btm_ren.Initialize()
        
if __name__ == "__main__":
    # 1. we need qt widget app
    app = QApplication(sys.argv)
    # 2. pop the main window
    window = MainWindow()
    # 3. close event
    sys.exit(app.exec_())