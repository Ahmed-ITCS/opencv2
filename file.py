import cv2

img = cv2.imread("GreenScreen.jpg")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_green = (36, 25, 25)
upper_green = (70, 255, 255)
mask = cv2.inRange(hsv, lower_green, upper_green)

inv_mask = cv2.bitwise_not(mask)

green_screen = cv2.bitwise_and(img, img, mask=inv_mask)

cv2.imwrite("output.jpg", green_screen)
