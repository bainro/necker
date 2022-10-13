# make int8 depth map & save as single channel
import math
import numpy as np
from PIL import Image

depth_map = np.zeros([270,270])

# top-left corner shold be around the middle of the first
# @TODO use python's builtin slice() to make fx of cube
# face involving top-left corner, line width, and edge length.
offset = 83

# Note: hard coded for 45 degree line!
p1x = 25
p1y = 25
p2x = 10+offset
width = 12
# draw a line of 1 px width between two points
dx = abs(p1x - p2x)

for i in range(dx + 15):
  color = round(255 - i / dx * (255-100))
  color = max(color, 100)
  depth_map[175+i,10+i:10+i+21] = color
  depth_map[10+i,160+i:160+i+21] = color

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

for i in range(dx):
  color = round(255 - i / dx * (255-100))
  depth_map[p1x+i:p1x+i+width,p1y+i] = color
  depth_map[p1x+i,p1y+i:p1y+i+width] = color
  depth_map[p1x+i+150-width-1:p1x+i+150,p1y+i+150] = color
  depth_map[p1x+i+150,p1y+i+150-width:p1y+i+150+1] = color

# at each new pixel, extend line horizontally

# was thinking of sniping & modding so color (ie depth) is dynamic
# https://github.com/npinto/opencv/blob/master/modules/core/src/drawing.cpp#L237
# https://github.com/npinto/opencv/blob/master/modules/core/src/drawing.cpp#L151

depth_png = Image.fromarray(depth_map)
depth_png = depth_png.convert("L")
depth_png.save("cube.png", "PNG")
