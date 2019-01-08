import cv2
import numpy as np
from scipy import ndimage

kernel_3x3 = np.array([[-1,-1,-1],
                       [-1,8,-1],
                       [-1,-1,-1]])

kernel_5x5 = np.array([[-1,-1,-1,-1,-1],
                       [-1,1,2,1,-1],
                       [-1,2,4,3,-1],
                       [-1,1,2,1,-1],
                       [-1,-1,-1,-1,-1]])
img = cv2.imread('../Images/opera.tif',0)
k3 = ndimage.convolve(img,kernel_3x3)
k5 = ndimage.convolve(img,kernel_5x5)
blur =cv2.GaussianBlur(img,(11,11),0)
g_hpf = img - blur
cv2.imshow("3X3",k3)
cv2.imshow("5X5",k5)
cv2.imshow("g_hpf",g_hpf)
cv2.imshow("blur",blur)
cv2.waitKey()
cv2.destroyAllWindows()