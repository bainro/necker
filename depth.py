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

depth_png = PIL.Image.fromarray(depth_map)
depth_png.save("cube.png", "PNG")
