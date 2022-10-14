# make int8 depth map & save as single channel
import numpy as np
from PIL import Image

depth_map = np.zeros([270,270])

# top-left corner shold be around the middle of the first
# @TODO use python's builtin slice() to make fx of cube
# face involving top-left corner, line width, and edge length.
offset = 83

backgn = 0
low = 255 # 50
high = 255 # 50

# Note: hard coded for 45 degree line!
p1x = 25
p1y = 25
p2x = 10+offset
width = 12
# draw a line of 1 px width between two points
dx = abs(p1x - p2x)

for i in range(dx + 15):
  color = round(high - i / dx * abs(high-low))
  color = max(color, low)
  depth_map[175+i,10+i:10+i+21] = color
  
for i in range(dx + 15):
  color = round(high - i / dx * abs(high-low))
  color = max(color, 50)
  depth_map[10+i,155+i:155+i+21] = color

# top line
depth_map[10+offset:175+offset,10+offset:25+offset] = low
# right side
depth_map[160+offset:175+offset,10+offset:175+offset] = low
# bottom side
depth_map[10+offset:175+offset,160+offset:175+offset] = low
# left side
depth_map[10+offset:25+offset,10+offset:175+offset] = low

# draw explicit front face
# top line
depth_map[10:175,10:25] = high
# right side
depth_map[160:175,10:175] = high
# bottom side
depth_map[10:175,160:175] = high
# left side
depth_map[10:25,10:175] = high

for i in range(dx):
  color = round(high - i / dx * abs(high-low))
  depth_map[p1x+i:p1x+i+width,p1y+i] = color
  depth_map[p1x+i,p1y+i:p1y+i+width] = color
  depth_map[p1x+i+150-width-1:p1x+i+150,p1y+i+150] = color
  depth_map[p1x+i+150,p1y+i+150-width:p1y+i+150+1] = color

depth_png = Image.fromarray(depth_map)
depth_png = depth_png.convert("L")
depth_png.save("cube.png", "PNG")
