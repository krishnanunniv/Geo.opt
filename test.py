import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
grid = []
for i in range(11):
    for j in range (11):
        grid.append(rg.Point3d(i,j,0))
 
a = grid
b= rg.Line(grid[4],grid[16])