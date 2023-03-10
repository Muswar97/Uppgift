from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.elgiganten.se/")
driver.maximize_window()
try:
    element = WebDriverWait(driver,100).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,"#coiPage-1 > div.coi-banner__page-footer > button.coi-banner__accept"))
    )
    element.click()
except:
    driver.quit()
link = driver.find_element(By.XPATH,"/html/body/elk-app/ng-component/elk-base-template/mat-sidenav-container/mat-sidenav-content/div[1]/elk-component-loader-wrapper/elk-header/header/elk-meta-controls/div[1]/a")
link.click()
kontakt = driver.find_element(By.CSS_SELECTOR,"#main > ng-component > div > elk-component-loader-wrapper > elk-cms-template-component-list > div > elk-cms-shell:nth-child(4) > elk-media-text > div > div.cms-media-text__text-wrapper > elk-wcag-button-link > a") 
#driver.execute_script("arguments[0].scrollIntoView(true);", kontakt)
driver.execute_script("scrollBy(0,1699)")
time.sleep(1)
kontakt.click()
driver.execute_script("scrollBy(0,600)")
time.sleep(10)