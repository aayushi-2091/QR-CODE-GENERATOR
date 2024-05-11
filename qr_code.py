#To create and get qrcode in your desired folder.
import qrcode
img=qrcode.make("https://www.aayushighosh.great-site.net/")
img.save("Portfolio.jpg")
#To get the same qrcode in the terminal
import cv2
image=cv2.imread(r'Portfolio.jpg')
window_name='QRcode'
cv2.imshow(window_name,image)
cv2.waitKey(0)
cv2.destroyAllWindows()