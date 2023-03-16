import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#PATH = "C:\Program Files (x86)\chromedriver.exe"

class ElgigantenTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
        self.driver.get("https://www.elgiganten.se/")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
    
    def test_kontakta_oss_assert(self):
        try:
            element = WebDriverWait(self.driver,100).until(
                EC.presence_of_element_located((By.CSS_SELECTOR,"#coiPage-1 > div.coi-banner__page-footer > button.coi-banner__accept"))
            )
            element.click()
        except:
            self.driver.quit()
        link = self.driver.find_element(By.XPATH,"/html/body/elk-app/ng-component/elk-base-template/mat-sidenav-container/mat-sidenav-content/div[1]/elk-component-loader-wrapper/elk-header/header/elk-meta-controls/div[1]/a")
        link.click()
        kontakt = self.driver.find_element(By.CSS_SELECTOR,"#main > ng-component > div > elk-component-loader-wrapper > elk-cms-template-component-list > div > elk-cms-shell:nth-child(4) > elk-media-text > div > div.cms-media-text__text-wrapper > elk-wcag-button-link > a") 
        #driver.execute_script("arguments[0].scrollIntoView(true);", kontakt)
        self.driver.execute_script("scrollBy(0,1299)")
        kontakt.click()
        self.driver.execute_script("scrollBy(0,600)")
        info = self.driver.find_element(By.CSS_SELECTOR, "#main > ng-component > div > elk-component-loader-wrapper > elk-cms-template-component-list > div > elk-cms-shell:nth-child(3) > elk-tiles > div > div > elk-content-tile-coremedia:nth-child(1) > a > div:nth-child(2) > div > div > p:nth-child(2)")
        #expected = "(+46) 0771 115 115\\\\nhello@elgiganten.se\\\\nVardagar: 08:30 - 20:00\\\\nHelg: Stängt"
        self.assertTrue(info.is_displayed)

    def test_lediga_jobb_assert(self):
        element = WebDriverWait(self.driver,100).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,"#coiPage-1 > div.coi-banner__page-footer > button.coi-banner__accept"))
        )
        element.click()
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        jobb = self.driver.find_element(By.XPATH,"/html/body/elk-app/ng-component/elk-base-template/mat-sidenav-container/mat-sidenav-content/elk-component-loader-wrapper/elk-footer/footer/div[2]/elk-navigation/div/mat-expansion-panel[4]/div/div/div/ul/li[3]/a")
        jobb.click()
        klicka = self.driver.find_element(By.CSS_SELECTOR,"#main > ng-component > elk-cms-shell > elk-sticky-header > div > elk-wcag-button-link > a")
        klicka.click()
        expected = "https://www.elgiganten.se/om-elgiganten/lediga-jobb#LedigaJobb"
        url = self.driver.current_url
        self.assertEqual(url,expected)

    def test_korgen_assert(self):
        element = WebDriverWait(self.driver,100).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,"#coiPage-1 > div.coi-banner__page-footer > button.coi-banner__accept"))
        )
        element.click()
        search = self.driver.find_element(By.CSS_SELECTOR,"#query-header")
        search.send_keys("Playstation 5")
        search.send_keys(Keys.RETURN)
        self.driver.implicitly_wait(10)
        ps = self.driver.find_element(By.CSS_SELECTOR,"#products > elk-component-loader-wrapper > elk-product-and-content-listing-view > div.product-list__products.ng-star-inserted > elk-product-tile-ff-wc-wrapper:nth-child(1) > elk-product-tile > div > a")
        self.driver.implicitly_wait(10)
        ps.click()
        btn = self.driver.find_element(By.CSS_SELECTOR,"#buy-box > elk-buy-box-delivery-tabs > elk-tab-group > div > div.tab-group__content > elk-buy-box-home-delivery-tab > elk-tab > div > elk-add-to-cart > button")
        btn.click()
        self.driver.find_element(By.CSS_SELECTOR,"#mat-dialog-10 > ng-component > div.buttons.sticky.ng-star-inserted > button.btn.btn--100.btn--3rd.btn--expanded").click()
        
        time.sleep(10)

 