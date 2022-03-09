import urllib.request
import undetected_chromedriver as uc
from selenium.common.exceptions import NoSuchElementException , StaleElementReferenceException , ElementNotInteractableException ,ElementClickInterceptedException
from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import cv2
import numpy as np
import pytesseract
options = webdriver.ChromeOptions()

options.add_argument("user-data-dir=C:\\Users\\Elite\\AppData\\Local\\Google\\Chrome\\User Data")
options.add_argument('profile-directory=Profile 4')


options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(chrome_options=options)

 

num_list = [74280, 78270, 78610, 78620, 78630, 80100, 82870, 84670, 84680, 84700, 84710, 85950, 88820, 90150, 93100, 93110, 93120, 93130, 93500, 95550, 74281, 78271, 80101, 82871, 85951, 88821, 90151, 93101, 93111, 93121, 93131, 93501, 95551, 74282, 78272, 80102, 82872, 85952, 88822, 90152, 93102, 93112, 93122, 93132, 93502, 95552, 74283, 78273, 80103, 82873, 85953, 88823, 90153, 93103, 93113, 93123, 93133, 93503, 95553, 74284, 78274, 80104, 82874, 85954, 88824, 90154, 93104, 93114, 93124, 93134, 93504, 95554, 74285, 78275,80105, 82875, 85955, 88825, 90155, 93105, 93115, 93125, 93135, 93505, 95555, 74286, 78276, 80106, 82876, 85956, 88826, 90156, 93106, 93116, 93126, 93136, 93506, 95556, 74287, 78277, 80107, 82877, 85957, 88827, 90157, 93107, 93117, 93127, 93137, 93507, 95557, 74288, 78278, 78598, 78618, 78628, 78638, 80108, 82878, 84678, 84688, 84708, 85958, 88828, 90158, 93108, 93118, 93128, 93138, 93508, 95558, 74289, 78279, 78599, 78619, 78629, 80109, 82879, 84679, 84689, 84709, 85959, 88829, 90159, 93109, 93119, 93129, 93139, 93509, 95559,] #list to help generate valid looking phone numbers

def decode(url): #It uses pytesseract to extract text from a image(to solve basic captcha)
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    img = cv2.imread(url)
    text = pytesseract.image_to_string(img)
    return text

def data(dic): #Maintain a record of all the username and password created by the program
    textfile = open("users.txt","a")
    for x,y in dic.items():
        textfile.write(str(x)+ " : " +str(y) + "\n")
    textfile.close()

def phone_num(numbers):#Generates random genuine looking numbers
    a = str(random.randint(0, 9))
    b = str(random.randint(0, 9))
    c = str(random.randint(0, 9))
    d = str(random.randint(0, 9))
    e = str(random.randint(0, 9))
    start_dig = str(numbers[random.randint(0, len(numbers)-1)])
    phone = start_dig + a + b + c + d + e
    return phone

def randomDigits(digits):#Just used to generate password with random digits 
    lower = 10**(digits-1)
    upper = 10**digits - 1
    return random.randint(lower, upper)

def fillform(driver):# Fills the form and submit it
    with open('runforever.txt', 'w') as f:
        f.write(str(randomDigits(9)))
    accounts = {}
    numb = phone_num(num_list)
    randpass = randomDigits(8)
    accounts[numb] = randpass
    time.sleep(2)
    # while driver.title == 'Please Wait... | Cloudflare':
        # time.sleep(5)
    try:
        captchaimg = driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div/div[2]/div[1]/div[7]/div[3]/div/div/div/img')
        captchasrc = captchaimg.get_attribute('src')
        # print(captchasrc)
        urllib.request.urlretrieve(captchasrc, 'screenshot.jpg')
        captchasol = decode('screenshot.jpg')
    except NoSuchElementException:
        captchasol = ''

    time.sleep(2)
    phone = driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div/input')
    phone.click()
    phone.send_keys(numb)
    passwd = driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div/div[2]/div[1]/div[2]/div[2]/div/input')
    passwd.click()
    passwd.send_keys(randpass)
    cnfpasswd = driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div/div[2]/div[1]/div[3]/div[2]/div/input')
    cnfpasswd.click()
    cnfpasswd.send_keys(randpass)
    question = driver.find_element(By.CSS_SELECTOR,'div.van-cell--clickable')
    question.click()
    time.sleep(1)
    cnfquestion = driver.find_element(By.CSS_SELECTOR, 'button.van-picker__confirm')
    cnfquestion.click()
    ans = driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div/div[2]/div[1]/div[8]/div[2]/div/input')
    ans.click()
    ans.send_keys(str(randomDigits(9)))
    captchafld = driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div/div[2]/div[1]/div[9]/div[3]/div/input')
    captchafld.click()
    captchafld.send_keys(captchasol)
    # time.sleep(1)
    submit = driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div/div[2]/div[3]/button')
    try:
        submit.click()
    except StaleElementReferenceException:
        pass
    try:
        WebDriverWait(driver , 15).until(EC.url_changes('https://app.win-winfinancial.in/#/register?r_code=hp8tel'))
    except TimeoutException:
        pass
    if driver.current_url == 'https://app.win-winfinancial.in/#/main/home':
        data(accounts)
        time.sleep(1)
    


inuser = 1000#int(input("Enter the no of forms you want to fill: "))
driver.get('https://app.win-winfinancial.in/#/register?r_code=hp8tel')
for i in range(0,inuser):
    fillform(driver)
    # time.sleep(1)
    driver.get('https://app.win-winfinancial.in/#/register?r_code=hp8tel')
driver.quit()
with open(r"user.txt", 'r') as fp:
    x = len(fp.readlines())
    print('Total Accounts:', x) 