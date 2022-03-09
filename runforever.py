import time
import os

formtimes = int(input("Enter the numbers of form you want: "))
def numofline():
    with open(r"users.txt", 'r') as fp:
        x = len(fp.readlines())
        return x

with open('runforever.txt') as f:
    text = f.read()

while True:
    time.sleep(10)
    if formtimes <= int(numofline()):
        break
    with open('runforever.txt') as f:
        text_new = f.read()
    if text_new == text:
        os.system("TASKKILL /F /IM chrome.exe")
        time.sleep(5)
        os.system('python web_automation.py')
        time.sleep(50)
        with open('runforever.txt') as f:
            text_new = f.read()
        text = text_new
    else:
        text = text_new
os.system('shutdown -s')