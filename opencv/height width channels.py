import cv2

img = cv2.imread('Photos/tiger-image.jpg')

height, width, channels = img.shape

print("Width:", width)
print("Height:", height)
print("Channels:", channels)