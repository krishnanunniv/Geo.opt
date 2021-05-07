import Rhino.Geometry as rg
import math

##create sphere for sun vectors
origin =rg.Point3d(0,0,0)
sphere = rg.Sphere(origin,1)
a = sphere

##point on sphere
pt = math.pi
b = sphere.PointAt(1.5*pt,2.2*pt)

##vector from origin to point 
pt1 = rg.Point3d(0,0,0)
pt2 = b
vec1 = pt2-pt1

##reversing vector
sunvec = rg.Vector3d.Negate(vec1)

##output sun vector
c = sunvec