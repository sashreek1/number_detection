from PIL import Image
import pytesseract
import cv2
import os
x = input("enter image location : ")
image = cv2.imread(x)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, gray)
text = pytesseract.image_to_string(Image.open(filename))
os.remove(filename)
text = text.split("\n")
for i in text:
    if i.isdigit():
        print(i)
    else:
        pass
cv2.imshow("Output", gray)
cv2.waitKey(0)