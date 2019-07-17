# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 14:37:56 2014
@author: duan
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('H:\\prj\\py\\opencv\\1.jpg',0)
edges = cv2.Canny(img,100,200)

plt.subplot(121),plt.imshow(img, cmap=None)
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()