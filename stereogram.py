# playing with the necker cube illusion
import os
import numpy as np
import cv2
import matplotlib.pyplot as plt

# img_path = os.path.join(os.getcwd(), "dust.png")
# img = cv2.imread(img_path)[...,::-1]/255.0
# noise =  np.random.normal(loc=0, scale=1, size=img.shape)
noise =  np.random.normal(loc=0, scale=1, size=(100,100,1))
# noisy_img = np.clip((img + noise*0.2),0,1)

plt.figure(figsize=(20,20))
noise = noise[:,:,0]
n_min = noise.min()
n_max = noise.max()
n_avg = (n_max + n_min) / 2

side_len = np.shape(noise)[0] // 3

# left_offset = 1

noise_og = np.copy(noise)
for i in range(side_len):
  for j in range(side_len):
    # noise[height, width]
    noise[side_len + i, side_len + j - 3] = noise[side_len + i, side_len + j]
  noise[side_len + i, side_len + side_len - 1] = np.random.normal(loc=0, scale=1, size=(1))
  noise[side_len + i, side_len + side_len - 2] = np.random.normal(loc=0, scale=1, size=(1))
  noise[side_len + i, side_len + side_len - 3] = np.random.normal(loc=0, scale=1, size=(1))

noise_tmp = np.copy(noise_og)
noise_og[noise_og > n_avg] = n_max
noise_og[noise_tmp < n_avg] = n_min  

noise_tmp = np.copy(noise)
noise[noise > n_avg] = n_max
noise[noise_tmp < n_avg] = n_min

#plt.imshow(noise_og, cmap='gray', vmin=n_min, vmax=n_max)
spacer = np.ones((np.shape(noise)[0], 30))
spacer[:,:] = n_min
plt.imshow(np.hstack((noise_og, spacer, noise)), cmap='gray', vmin=n_min, vmax=n_max)
# plt.imshow(np.hstack((noise_og, noise)), cmap='gray', vmin=n_min, vmax=n_max)
plt.show()
#plt.imshow(noise, cmap='gray', vmin=n_min, vmax=n_max)
#plt.show()
