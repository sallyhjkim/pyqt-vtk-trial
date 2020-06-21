import sys
import vtk
from PyQt5 import QtCore, QtWidgets

#https://vtk.org/doc/nightly/html/classvtkRenderWindowInteractor.html
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor 

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)

        # make frame
        self.frame = QtWidgets.QFrame()

        # make vertical layout
        self.vl = QtWidgets.QVBoxLayout()
        
        # make vtk widget
        self.vtk_widtget = QVTKRenderWindowInteractor(self.frame)
        self.vl.addWidget(self.vtk_widtget)

        self.renderer = vtk.vtkRenderer()
        self.vtk_widtget.GetRenderWindow().AddRenderer(self.renderer)
        self.iren = self.vtk_widtget.GetRenderWindow().GetInteractor()
        
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
 
        self.frame.setLayout(self.vl)
        self.setCentralWidget(self.frame)
 
        self.show()
        self.iren.Initialize()
        
if __name__ == "__main__":
    # 1. we need qt widget app
    app = QtWidgets.QApplication(sys.argv)
    # 2. pop the main window
    window = MainWindow()
    # 3. close event
    sys.exit(app.exec_())