import cv2
import pytesseract
from pytesseract import Output

img = cv2.imread('IMG_6751.jpeg')

d = pytesseract.image_to_data(img, output_type=Output.DICT)
print(d.keys())

n_boxes = len(d['text'])
for i in range(n_boxes):
    if int(d['conf'][i]) > 50:
        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        print(d['text'][i])

cv2.imshow('img', img)
cv2.waitKey(0)