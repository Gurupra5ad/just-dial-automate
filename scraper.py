import requests
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#assigning the browser and getting the site
browser = webdriver.Chrome('/home/disciple/chromedriver')
wait = WebDriverWait(browser,60)
browser.get("https://www.justdial.com/")

# Login automation ----------------------------------------------------------------------------------------

time.sleep(3)
#click login button on top nav bar
wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/header/section/div/div[2]/ul/li[4]/ul/li[1]/a'))).click() 
time.sleep(3)
#sending in name and phone number keys for login automation
#sending in the username 
login_name = browser.find_element_by_xpath('//*[@id="lgn_name"]')
login_name.send_keys("shreedhar")
time.sleep(3)
#sending in the phone number
login_number = browser.find_element_by_xpath('//*[@id="lgn_mob"]')
login_number.send_keys("9994987315") 
#clicking get otp button
wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="lgn_smtn"]'))).click() 
#going inside otp page
otp = input("-------------------Enter your 6 digit OTP--------------------- ")
for i in range(6):
    #targetting each otp input dash
    login_otp = browser.find_element_by_xpath(f'//*[@id="pin_{i}"]')
    login_otp.send_keys(otp[i]) 
#click otp submit button
wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="otp_submit"]'))).click() 

#going to home after login
wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/header/div[1]/div/div/div[1]/aside/a'))).click() 

