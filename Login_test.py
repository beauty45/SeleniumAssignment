from datetime import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core import driver

def login1():

        service = Service(ChromeDriverManager().install())

        browser = webdriver.Chrome(service=service)

        browser.get("https://www.saucedemo.com/")

        username = 'standard_user'
        password = 'secret_sauce'

        usernameField = browser.find_element(By.ID,"user-name")
        usernameField.send_keys(username)

        passwordField = browser.find_element(By.ID,"password")
        #passwordField = browser.find_element(By.XPATH,'//*[@id="password"]')
        passwordField.send_keys(password)
        #sleep(5)

        loginButton = browser.find_element(By.ID,"login-button")
        loginButton.click()
        sleep(5)
        browser.quit()

login1()

def login2():
        service = Service(ChromeDriverManager().install())
        browser = webdriver.Chrome(service=service)
        browser.get("https://www.saucedemo.com/")

        username = 'standard_user'
        password = 'secret_sauce'

        usernameField1 = browser.find_element(By.XPATH,'//*[@id="user-name"]')
        usernameField1.send_keys(username)

        passwordField1 = browser.find_element(By.XPATH, "//input[@type='password']")
        passwordField1.send_keys(password)
        #sleep(5)

        loginButton1 = browser.find_element(By.XPATH,"//input[contains(@value,'Login')]")
        loginButton1.click()
        sleep(5)
        browser.quit()

login2()