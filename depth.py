# make int8 depth map & save as single channel
import numpy as np
from PIL import Image

depth_map = np.zeros([350,350])

# back face first. Ie painter's algo for depth
# top-left corner shold be around the middle of the first
# @TODO use python's builtin slice() to make fx of cube
# face involving top-left corner, line width, and edge length.
offset = 83
# top line
depth_map[10+offset:175+offset,10+offset:25+offset] = 100
# right side
depth_map[160+offset:175+offset,10+offset:175+offset] = 100
# bottom side
depth_map[10+offset:175+offset,160+offset:175+offset] = 100
# left side
depth_map[10+offset:25+offset,10+offset:175+offset] = 100

# draw explicit front face
# top line
depth_map[10:175,10:25] = 255
# right side
depth_map[160:175,10:175] = 255
# bottom side
depth_map[10:175,160:175] = 255
# left side
depth_map[10:25,10:175] = 255

depth_png = Image.fromarray(depth_map)
depth_png = depth_png.convert("L")
depth_png.save("cube.png", "PNG")
