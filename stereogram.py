# playing with the necker cube illusion
import os
import numpy as np
import cv2
import matplotlib.pyplot as plt

  
n = 100
img_path = os.path.join(os.getcwd(), "bg.png")
bg = cv2.imread(img_path)[...,::-1]/255.0
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

bg_og = np.copy(bg)
  
noise_tmp = np.copy(noise_og)
noise_og[noise_og > n_avg] = 666
noise_og[noise_tmp < n_avg] = n_min  

bg_og_2 = np.copy(bg_og)
bg_2 = np.copy(bg)

for i in range(n):
  for j in range(n):
    if noise_og[i, j] != 666:
        #bg_og[i, j, :] = 0
        bg_og_2[i, j, :] = 0
    elif i > side_len and j > side_len:
      if i < side_len*2 and j < side_len*2:
        bg_og[i, j, :] = 255

noise_tmp = np.copy(noise)
noise[noise > n_avg] = 666
noise[noise_tmp < n_avg] = n_min
 
for i in range(n):
  for j in range(n):
    if noise[i, j] != 666:
        #bg[i, j, :] = 0
        bg_2[i, j, :] = 0
    elif i > side_len and j > side_len:
      if i < side_len*2 and j < side_len*2:
        bg[i, j, :] = 255

#plt.imshow(noise_og, cmap='gray', vmin=n_min, vmax=n_max)
spacer = np.ones((np.shape(noise)[0], 5, 3))
spacer[:,:] = n_min
x = np.hstack((bg_og, spacer, bg))
plt.imshow(np.vstack((x, np.hstack((bg_og_2, spacer, bg_2)))))
# plt.imshow(np.hstack((noise_og, spacer, noise)), cmap='gray', vmin=n_min, vmax=n_max)
# plt.imshow(np.hstack((noise_og, noise)), cmap='gray', vmin=n_min, vmax=n_max)
plt.show()
#plt.imshow(noise, cmap='gray', vmin=n_min, vmax=n_max)
#plt.show()
