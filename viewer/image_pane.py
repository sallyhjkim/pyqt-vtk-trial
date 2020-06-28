import vtk

from PyQt5.QtGui import QKeyEvent, QPixmap
from PyQt5.QtCore import QEvent, QSettings, QPointF, QSizeF, Qt
from PyQt5.QtWidgets import QMainWindow, QWidget, QGridLayout, QVBoxLayout, QHBoxLayout, QDesktopWidget, QApplication, QFrame, QPushButton, QLabel
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor 

class ImagePane():
    def __init__(self, type='default'):
        self.ren_widget = QWidget()
        self.vtk_ren_window =  QVTKRenderWindowInteractor(self.ren_widget)
        
        self.vtk_renderer = vtk.vtkRenderer()
        self.vtk_ren_window.GetRenderWindow().AddRenderer(self.vtk_renderer)
        self.vtk_interactor = self.vtk_ren_window.GetRenderWindow().GetInteractor()
        # Create source
        source_dict = {
            "cylinder": vtk.vtkCylinderSource(),
            "sphere": vtk.vtkSphereSource(),
            "arrow": vtk.vtkArrowSource(),
            "cube": vtk.vtkCubeSource(),
            "default": vtk.vtkConeSource()
        }
        source = source_dict.get(type)
        
        # Create a mapper
        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputConnection(source.GetOutputPort())
        
        # Create an actor
        actor = vtk.vtkActor()
        actor.SetMapper(mapper)

        self.vtk_renderer.AddActor(actor)
        self.vtk_renderer.ResetCamera()
        
    def get_widget(self):
        return self.ren_widget
    
    def intial(self):
        self.vtk_interactor.Initialize()