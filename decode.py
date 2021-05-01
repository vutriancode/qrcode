import cv2
image = cv2.imread('mn.JPG')
cv2.imshow("a", image)
cv2.waitKey()
qrCodeDetector = cv2.QRCodeDetector()
decodedText, points, _ = qrCodeDetector.detectAndDecode(image)
print(decodedText)