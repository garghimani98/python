from selenium import webdriver 

from PIL import Image,ImageFilter
import pytesseract  



import urllib.request

#download and install pytesseract as per system's requirements

##install pytesseract and pillow modules  using command pip install pytesseract and pip install pillow

##edit environment variables

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
               
# image path
img_path ="path of the image  to be processed"

###opening image
img1=Image.open(img_path)


print("hii")

##text will be extracted from image 
print(pytesseract.image_to_string(img1,lang='eng'))
