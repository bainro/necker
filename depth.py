# make int8 depth map & save as single channel
import numpy as np
from PIL import Image

depth_map = np.zeros([350,350])
# draw explicit front face
# top line
depth_map[10:175,10:25] = 255
# right side
depth_map[160:175,10:175] = 255
# bottom side
depth_map[10:175,160:175] = 255
# left side
depth_map[10:25,10:175] = 255

# back face
# top-left corner shold be around the middle of the first
offset = 83
# top line
depth_map[10+offset:175+offset,10+offset:25+offset] = 100
# right side
depth_map[160+offset:175+offset,10+offset:175+offset] = 100
# bottom side
depth_map[10+offset:175+offset,160+offset:175+offset] = 100
# left side
depth_map[10+offset:25+offset,10+offset:175+offset] = 100

depth_png = Image.fromarray(depth_map)
depth_png = depth_png.convert("L")
depth_png.save("cube.png", "PNG")
