import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
grid = []
for i in range(11):
    for i in range (11):
        grid.append(rg.Point3d(i,j,0))
 
a = grid