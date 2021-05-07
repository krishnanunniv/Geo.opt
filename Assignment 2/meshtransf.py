import Rhino.Geometry as rg
import ghpythonlib.treehelpers as th
import math

#creating 1st set of points

pts1 =[]
for i in range(int(x)):
    pt = rg.Point3d(i,0,0)
    pts1.append(pt)
pt1 = pts1

#creating 2nd set of points

pts2 = []
for i in range(x):
    pt = rg.Point3d(i,y,0)
    pts2.append(pt)
pt2 = pts2




#creating list of lines
linelist = []
for i in range(len(pts1)):
    l1 = rg.Line(pt1[i],pt2[i])
    linelist.append(l1)
l= linelist


#dividing curve
cnt =9
alldivpt = []
for i in linelist:
    divpts = []
    nurbln = i.ToNurbsCurve()
    params = nurbln.DivideByCount(cnt,True)
    for p in params:
        divpt = i.PointAt(p)
        divpts.append(divpt)
    alldivpt.append(divpts)

div = th.list_to_tree(alldivpt)

#applying sine function

allmvdpts = []
for list in alldivpt:
    mvdpts = []
    for pt in list:
        vec = rg.Vector3d(pt)
        vlen = vec.Length
        mag = math.sin(vlen)
        zvec = rg.Vector3d(0,0,mag)
        newpt = pt-zvec
        mvdpts.append(newpt)
    allmvdpts.append(mvdpts)

mpt = th.list_to_tree(allmvdpts)


#making curve from a list of points
curvelist = []
for mp in allmvdpts:
    crv = rg.Curve.CreateInterpolatedCurve(mp,3)
    curvelist.append(crv)
    crv = curvelist

#creating loft
srf = rg.Brep.CreateFromLoft(crv,rg.Point3d.Unset,rg.Point3d.Unset,0,False)
srf = srf[0]
srf1 = srf.Faces[0]



srf1.SetDomain(0,rg.Interval(0,U))
srf1.SetDomain(1,rg.Interval(0,V))

uvpt = []
for i in range(U+1):
    uvpt1 = []
    for j in range(V+1):
        pt = rg.Surface.PointAt(srf1,i,j)
        uvpt1.append(pt)
    uvpt.append(uvpt1)


uvpoints =th.list_to_tree(uvpt)

mesh = rg.Mesh()

for i in range(len(uvpt)-1):
    for j in range(len(uvpt[i])-1):
        v1 = uvpt[i][j]
        v2 = uvpt[i+1][j]
        v3 = uvpt[i+1][j+1]
        v4 = uvpt[i][j+1]
        m = rg.Mesh()
        m.Vertices.Add(v1)
        m.Vertices.Add(v2)
        m.Vertices.Add(v3)
        m.Vertices.Add(v4)
        m.Faces.AddFace(0,1,2,3)
        mesh.Append(m)

mesh1 = mesh

cleanmesh = mesh
#methods to clean a mesh
cleanmesh.Normals.ComputeNormals()
cleanmesh.Vertices.CombineIdentical(True, True)
cleanmesh.Vertices.CullUnused()
cleanmesh.Weld(3.14159265358979)
cleanmesh.UnifyNormals()

##---------------------------ASSIGNMENT 2----------------------------

clmesh = cleanmesh
#outputting meshfacenormals
cleanmesh.FaceNormals.ComputeFaceNormals()
a = cleanmesh.FaceNormals

##getting centerpoint of mesh faces
centers = []
for i in range(cleanmesh.Faces.Count):
    cntr = cleanmesh.Faces.GetFaceCenter(i)
    centers.append(cntr)
b = centers

##angle between sunvector and meshfaces
anglelist = []
for i in range(len(b)):
    vecang = rg.Vector3d.VectorAngle(rg.Vector3d(b[i]),s)
    anglelist.append(vecang)
c = anglelist




##duplicating mesh
meshdup = rg.Mesh.Duplicate(cleanmesh)

##exploding the mesh

exploded = []
for i in range(meshdup.Faces.Count):
    meshf = meshdup.Faces.ExtractFaces([0])
    exploded.append(meshf)

d = exploded


##transformation based on sunvector angle
##Selecting diagonal Mesh Vertices
srpt = []
for i in range(len(exploded)):
    v = []
    v1 =  exploded[i].Vertices
    v.append(v1[0])
    v.append(v1[3])

##moving diagonal points based on vector angle difference
    mvdpoints = []
    for pt in v:
        vec = rg.Vector3d(pt)
        mag = anglelist[i]*-0.8
        zvec = rg.Vector3d(0,0,mag)
        mvdp = rg.Point3d(vec - zvec)
        mvdpoints.append(mvdp)
    srpt.append(mvdpoints)

##Creating Transformed Mesh
m1 =rg.Mesh()
for i in range(len(exploded)):
    m2 = rg.Mesh()
    v1 =  exploded[i].Vertices
    m2.Vertices.Add(v1[1])
    m2.Vertices.Add(v1[2])

    m2.Vertices.Add(rg.Point3d(srpt[i][0]))
    m2.Vertices.Add(rg.Point3d(srpt[i][1]))
    m2.Faces.AddFace(0,1,2,3)
    m1.Append(m2)


e = th.list_to_tree(v)
f = th.list_to_tree(srpt)

##exploding new mesh 

meshdup1 = rg.Mesh.Duplicate(m1)
explodednew = []
for i in range(meshdup1.Faces.Count):
    meshf1 = meshdup1.Faces.ExtractFaces([0])
    explodednew.append(meshf1)

##Outputing Transformed Mesh
g = explodednew







