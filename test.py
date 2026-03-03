import bpy
import argparse
import json


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
    return poly_points


def attrib_uv():
    uv_vectors = [uv.vector.to_tuple() for uv in mesh.uv_layers['UVMap'].uv]
    return uv_vectors



data = {"objects_name": objects_name,
        "meshes_name": meshes_name,
        "vertices": vertices,
        "poly_point_indices": poly_point_indices(),
        "UV": attrib_uv()
        }

json_data = json.dumps(data)
print(json_data)
