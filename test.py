import bpy
import argparse
import json
import numpy as np


parser = argparse.ArgumentParser()
file = parser.add_argument('-f')

args = parser.parse_args()
file_path = args.f

# file_path = r"C:\Users\wh.RENO-STUDIOS\Desktop\test.blend"

# clean initial file meshes,objects
for obj in bpy.data.objects:
    bpy.data.objects.remove(obj)

for mesh in bpy.data.meshes:
    bpy.data.meshes.remove(mesh)

# append objects from input file
with bpy.data.libraries.load(file_path) as (data_src, data_dst):
    data_dst.objects = data_src.objects

mesh = bpy.data.meshes['Sphere']

objects_name = [obj.name for obj in bpy.data.objects]
meshes_name = [mesh.name for mesh in bpy.data.meshes]
vertices = [vertex.co.to_tuple() for vertex in mesh.vertices]


def poly_point_indices():
    poly_points = []
    for f in mesh.polygons:
        poly_points.append([v for v in f.vertices])
    poly_points_reverse = [tuple(reversed(point_indices)) for point_indices in poly_points]
    return poly_points_reverse

poly_point_indices = poly_point_indices()

'''
def attrib_uv():
    uv_points_vector = [uv.vector.to_3d().to_tuple() for uv in mesh.uv_layers['UVMap'].uv]
    uv = list(zip(*[iter(uv_points_vector)]*4))
    uv_reverse = [tuple(reversed(vecter)) for vecter in uv]
    uv_array = np.array(uv_reverse)
    uvw =[float(n) for n in uv_array.ravel()]
    return uvw
'''

def attrib_uv():
    uv = mesh.uv_layers['UVMap'].uv
    uvw = []
    for poly in mesh.polygons:
        uv_vector = [uv[index].vector.to_3d().to_tuple() for index in poly.loop_indices]
        uvw.append(tuple(reversed(uv_vector)))
    uvw = [vector for poly_indices in uvw for point in poly_indices for vector in point]
    return uvw


data = {"objects_name": objects_name,
        "meshes_name": meshes_name,
        "vertices": vertices,
        "poly_point_indices": poly_point_indices,
        "UV": attrib_uv()
        }

json_data = json.dumps(data)
print(json_data)
