import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('damaged_cameraman.jpg') # original image
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY) # convert to grayscale

mask = cv2.imread('damage_mask.jpg') # mask image
mask = cv2.cvtColor(mask, cv2.COLOR_RGB2GRAY) # convert to grayscale

row, column = img.shape # obtain height(row) and width (column)

final_pic = np.zeros((row,column)) # initiate the matrix size to dimensions of the original image

for a in range(0,row):
  for b in range(0,column):
    img_pix = img[b][a]
    mask_pix = mask[b][a]
    if mask_pix == 255:
        final_pic[b][a] = img_pix
    else:
        final_pic[b][a] = final_pic[b-1][a-1]
        gaussian = cv2.GaussianBlur(final_pic,(3,3),0)

plt.subplot(121),plt.imshow(img, 'gray'),plt.title('Damaged Picture')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(final_pic, 'gray'),plt.title('Fixed Picture')
plt.xticks([]), plt.yticks([])
plt.show()
