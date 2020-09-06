# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 20:57:14 2020

@author: Venisha Dias
"""
import math
from PIL import Image,ImageDraw,ImageFont
import cv2
import numpy as np

scaling = 0.5
width = 10
height = 25
image = Image.open("Me.jpg")
w,h = image.size
image = image.resize((int(scaling*w),int(scaling*h*(width/height))),Image.NEAREST)
w,h = image.size
p = image.load()

font = ImageFont.truetype('C:\\Windows\\Fonts\\lucon.ttf',15)
outputImage = Image.new('RGB',(width*w,height*h),color=(0,0,0))
draw = ImageDraw.Draw(outputImage)
def getChar(h):
	chars  = "venishadias!@#$%^&*()"[::-1]
	charArr = list(chars)
	l = len(charArr)
	mul = l/256
	return charArr[math.floor(h*mul)]

for i in range(h):
    for j in range(w):
        r,g,b = p[j,i]
        gray = int((r/3+g/3+b/3))
        p[j,i] = (gray,gray,gray)
        draw.text((j*width,i*height),getChar(gray),
        font=font,fill = (r,g,b))
		
outputImage.save("Ascii_Image.png")		
img = cv2.imread("Me.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 3)
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 13, 10)
color = cv2.bilateralFilter(img, 9, 255, 255)
cartoon = cv2.bitwise_and(color, color, mask=edges)



cv2.imshow("Cartoonized Image", cartoon)

cv2.waitKey(0)
		
		