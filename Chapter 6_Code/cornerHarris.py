import cv2
import numpy as np
#检测角点特征
img = cv2.imread('../Images/ruler.512.tiff')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cv2.imshow("gray",gray)
gray = np.float32(gray)
dst = cv2.cornerHarris(gray,2,1,0.04)
img[dst>0.01*dst.max()] = [0,0,255]
while (True):
    cv2.imshow('corner',img)
    if cv2.waitKey(100) & 0xff ==ord("q"):
        break
cv2.destroyAllWindows()
