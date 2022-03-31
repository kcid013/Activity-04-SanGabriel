import cv2

filePath = 'cat.jpg'
windowTitle = 'picture of cat'
readCVimg = cv2.imread(filePath, -1)

cv2.imshow(windowTitle, readCVimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
