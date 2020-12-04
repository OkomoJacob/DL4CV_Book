# Load the CV pakg to read and load the image
import cv2
image = cv2.imread("jp.png")
print(image.shape)
cv2.imshow("Jurris Park", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
