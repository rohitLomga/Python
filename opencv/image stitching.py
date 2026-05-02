import cv2

img1 = cv2.imread('Photos/nature.jpg')
img2 = cv2.imread('Photos/tiger-image.jpg')

stitcher = cv2.Stitcher_create()
status, stitched = stitcher.stitch([img1, img2])

if img1 is None or img2 is None:
    print("Image not loaded properly")

if status == 0:
    cv2.imshow("Stitched Image", stitched)
else:
    print("Stitching Failed")

cv2.waitKey(0)
cv2.destroyAllWindows()