import subprocess
import json

bpy = r"C:\Users\wh.RENO-STUDIOS\Desktop\PycharmProfect\hou_bpy\dist\test\test.exe"
blend = r"C:\Users\wh.RENO-STUDIOS\Desktop\test.blend"
r = subprocess.run([bpy, '-f', blend], capture_output=True, text=True)
data = json.loads(r.stdout)

poly_point_indices = [list(reversed(point_indices)) for point_indices in data['poly_point_indices']]
print(data)
