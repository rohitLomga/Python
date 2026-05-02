import cv2
import numpy as np

img = cv2.imread('Photos/tiger-image.jpg')

pts1 = np.float32([[100,100], [400,100], [100,400], [400,400]])
pts2 = np.float32([[0,0], [300,0], [0,300], [300,300]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)
output = cv2.warpPerspective(img, matrix, (300, 300))

cv2.imshow("Perspective Transform", output)
cv2.waitKey(0)
cv2.destroyAllWindows()