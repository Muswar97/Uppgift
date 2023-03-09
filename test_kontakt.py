from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.elgiganten.se/")
driver.maximize_window()
link = driver.find_element(By.XPATH,"/html/body/elk-app/ng-component/elk-base-template/mat-sidenav-container/mat-sidenav-content/div[1]/elk-component-loader-wrapper/elk-header/header/elk-meta-controls/div[1]/a")
link.click()
time.sleep(4)