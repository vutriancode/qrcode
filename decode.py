# import cv2
# from pdf2image import convert_from_path
# pages =convert_from_path("CamScanner.pdf")
# pages[0].save('out.jpg', 'JPEG')
# image = cv2.imread("MM.JPG")
# cv2.imshow("a",image)
# cv2.waitKey()
# qrCodeDetector = cv2.QRCodeDetector()
# decodedText, points, _ = qrCodeDetector.detectAndDecode(image)
# print(decodedText)
import qrtools
qr = qrtools.QR()
qr.decode("horn.png")
