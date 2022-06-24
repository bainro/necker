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
n_min = noise.min()
n_max = noise.max()
n_avg = (n_max + n_min) / 2

noise_og = np.copy(noise)
noise[noise > n_avg] = n_max
noise[noise_og < n_avg] = n_min

plt.imshow(noise, cmap='gray', vmin=n_min, vmax=n_max)
plt.show()
plt.hist(noise.ravel(), bins=100)
plt.show()
