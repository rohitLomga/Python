import cv2

img = cv2.imread('Photos/tiger-image.jpg', 0)

edges1 = cv2.Canny(img, 50, 150)
edges2 = cv2.Canny(img, 100, 200)

cv2.imshow("Edges 50-150", edges1)
cv2.imshow("Edges 100-200", edges2)

cv2.waitKey(0)
cv2.destroyAllWindows()