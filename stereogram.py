# playing with the necker cube illusion
import os
import colorsys
import numpy as np
import cv2
import matplotlib.pyplot as plt

def spectrum(n : int):
    hsv = [(h, 1, 1) for h in np.linspace(0, 240/360, n)]
    rgb = [colorsys.hsv_to_rgb(*tup) for tup in hsv]
    defloat = lambda x: tuple((int(255 * i) for i in x))
    return [defloat(x) for x in rgb]
  
n = 100
# img_path = os.path.join(os.getcwd(), "dust.png")
# img = cv2.imread(img_path)[...,::-1]/255.0
# noise =  np.random.normal(loc=0, scale=1, size=img.shape)
noise =  np.random.normal(loc=0, scale=1, size=(n,n))
# noisy_img = np.clip((img + noise*0.2),0,1)

plt.figure(figsize=(20,20))
n_min = noise.min()
n_max = noise.max()
n_avg = (n_max + n_min) / 2

side_len = np.shape(noise)[0] // 3

# left_offset = 1

noise_og = np.copy(noise)
for i in range(side_len):
  for j in range(side_len):
    # noise[height, width]
    noise[side_len + i, side_len + j - 1] = noise[side_len + i, side_len + j]
  noise[side_len + i, side_len + side_len - 1] = np.random.normal(loc=0, scale=1, size=(1))
  #noise[side_len + i, side_len + side_len - 2] = np.random.normal(loc=0, scale=1, size=(1))
  #noise[side_len + i, side_len + side_len - 3] = np.random.normal(loc=0, scale=1, size=(1))  

color_grad = np.array(spectrum(n))
color_grad = color_grad.reshape((1, n, 3))
color_grad = np.tile(color_grad, (n, 1, 1))
color_og = np.copy(color_grad)
  
noise_tmp = np.copy(noise_og)
noise_og[noise_og > n_avg] = 666
noise_og[noise_tmp < n_avg] = n_min  

for i in range(n):
  for j in range(n):
    if noise_og[i, j] != 666:
        color_og[i, j, :] = 0

noise_tmp = np.copy(noise)
noise[noise > n_avg] = 666
noise[noise_tmp < n_avg] = n_min

for i in range(n):
  for j in range(n):
    if noise[i, j] != 666:
        color_grad[i, j, :] = 0

#plt.imshow(noise_og, cmap='gray', vmin=n_min, vmax=n_max)
spacer = np.ones((np.shape(noise)[0], 30))
spacer[:,:] = n_min
plt.imshow(np.hstack((color_og, spacer, color_grad)))
# plt.imshow(np.hstack((noise_og, spacer, noise)), cmap='gray', vmin=n_min, vmax=n_max)
# plt.imshow(np.hstack((noise_og, noise)), cmap='gray', vmin=n_min, vmax=n_max)
plt.show()
#plt.imshow(noise, cmap='gray', vmin=n_min, vmax=n_max)
#plt.show()
