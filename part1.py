import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('1.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

kernel = -np.ones((3,3),np.float32) # create a 3x3 filter matrix with all -1s
kernel[1][1] = 8; # middle index of the filter is an 8
dst = cv2.filter2D(img,-1,kernel) # convolutes the image with the kernel, given the source image, depth of the destination image, and the 3x3 matrix

alpha = 0.5 # weight of the first image
beta = 1.0 - alpha # weight of the second image
added_img = cv2.addWeighted(img, alpha, dst, beta, 0)

plt.subplot(221),plt.imshow(img, 'gray'),plt.title('Original')
plt.subplot(222),plt.imshow(dst, 'gray'),plt.title('Averaging')
plt.subplot(223),plt.imshow(added_img, 'gray'),plt.title('Added Image')
plt.show()
