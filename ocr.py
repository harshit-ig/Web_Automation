import cv2
import pytesseract
def decode(url):
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    img = cv2.imread(url)
    text = pytesseract.image_to_string(img)
    return text
print(decode("screenshot.jpg"))