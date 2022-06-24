# playing with the necker cube illusion
import os
import numpy as np
import cv2
import matplotlib.pyplot as plt

img_path = os.path.join(os.getcwd(), "dust.png")
img = cv2.imread(img_path)[...,::-1]/255.0
noise =  np.random.normal(loc=0, scale=1, size=img.shape)

# noise overlaid over image
noisy = np.clip((img + noise*0.2),0,1)
noisy2 = np.clip((img + noise*0.4),0,1)

# noise multiplied by image:
# whites can go to black but blacks cannot go to white
noisy2mul = np.clip((img*(1 + noise*0.2)),0,1)
noisy4mul = np.clip((img*(1 + noise*0.4)),0,1)

noisy2mul = np.clip((img*(1 + noise*0.2)),0,1)
noisy4mul = np.clip((img*(1 + noise*0.4)),0,1)

# noise multiplied by bottom and top half images,
# whites stay white blacks black, noise is added to center
img2 = img*2
n2 = np.clip(np.where(img2 <= 1, (img2*(1 + noise*0.2)), (1-img2+1)*(1 + noise*0.2)*-1 + 2)/2, 0,1)
n4 = np.clip(np.where(img2 <= 1, (img2*(1 + noise*0.4)), (1-img2+1)*(1 + noise*0.4)*-1 + 2)/2, 0,1)

# norm noise for viz only
noise2 = (noise - noise.min())/(noise.max()-noise.min())
plt.figure(figsize=(20,20))
noise = noise[:200,:200,0]
n_min = noise.min()
n_max = noise.max()
n_avg = (n_max + n_min) / 2

noise_og = np.copy(noise)
noise[noise > n_avg] = n_max
noise[noise_og < n_avg] = n_min

plt.imshow(noise, cmap='gray', vmin=n_min, vmax=n_max)
'''
plt.show()
plt.imshow(np.vstack((np.hstack((img, noise)),
                      np.hstack((noisy, noisy2)),
                      np.hstack((noisy2mul, noisy4mul)),
                      np.hstack((n2, n4)))))
'''
plt.show()
plt.hist(noise.ravel(), bins=100)
plt.show()
