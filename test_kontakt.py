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
        self.driver.implicitly_wait(1000)
        self.driver.maximize_window()
        element = WebDriverWait(self.driver,100).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,"#coiPage-1 > div.coi-banner__page-footer > button.coi-banner__accept"))
        )
        element.click()


    def test_kontakta_oss_assert(self):
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
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        jobb = self.driver.find_element(By.XPATH,"/html/body/elk-app/ng-component/elk-base-template/mat-sidenav-container/mat-sidenav-content/elk-component-loader-wrapper/elk-footer/footer/div[2]/elk-navigation/div/mat-expansion-panel[4]/div/div/div/ul/li[3]/a")
        jobb.click()
        klicka = self.driver.find_element(By.CSS_SELECTOR,"#main > ng-component > elk-cms-shell > elk-sticky-header > div > elk-wcag-button-link > a")
        klicka.click()
        expected = "https://www.elgiganten.se/om-elgiganten/lediga-jobb#LedigaJobb"
        url = self.driver.current_url
        self.assertEqual(url,expected)

    def test_korgen_assert(self):
        search = self.driver.find_element(By.CSS_SELECTOR,"#query-header")
        search.send_keys("Elden Ring")
        search.send_keys(Keys.RETURN)
        self.driver.find_element(By.CSS_SELECTOR,"#products > elk-component-loader-wrapper > elk-product-and-content-listing-view > div.product-list__products.ng-star-inserted > elk-product-tile-ff-wc-wrapper:nth-child(1) > elk-product-tile > div > a").click()
        self.driver.find_element(By.CSS_SELECTOR,"#buy-box > elk-buy-box-delivery-tabs > elk-tab-group > div > div.tab-group__content > elk-buy-box-home-delivery-tab > elk-tab > div > elk-add-to-cart > button").click()
        btn = WebDriverWait(self.driver,1000).until(
           EC.presence_of_element_located((By.XPATH,"/html/body/div[7]/div[2]/div/mat-dialog-container/ng-component/div[4]/button[1]/span"))
        )
        btn.click()
        expected_element = self.driver.find_element(By.CSS_SELECTOR,"#main > div.l-constraint.l-constraint--50 > main > elk-checkout-main > div > div.checkout-main__order-summary-wrapper > elk-order-summary > div > div.order-summary__products.ng-star-inserted > elk-order-summary-product > elk-product-item > div.ng-star-inserted > a > div > div.product-item__info > div.product-item__title").text
        expected_title = "Elden Ring (PS4) inkl. PS5-version"
        self.assertEqual(expected_element,expected_title)
        
    def test_filter_assert(self):
        self.driver.find_element(By.CSS_SELECTOR,"#main > ng-component > div.l-default-indentation.ng-star-inserted > elk-component-loader-wrapper > elk-cms-template-component-list > div > elk-cms-shell.cms-indentation__no-component-separation-indentation--bottom.cms-indentation__default-bottom.cms-indentation__category-carousel--homepage.cms-layout__stretch-to-max.ng-star-inserted > elk-category-carousel > elk-image-slider > elk-carousel > div > swiper > div > div.swiper-slide.ng-star-inserted.swiper-slide-active > elk-image-title-element > a > elk-cms-img > picture > img").click()
        self.driver.find_element(By.CSS_SELECTOR,"#main > ng-component > div > elk-component-loader-wrapper > elk-cms-template-component-list > div > elk-cms-shell.content-divider.content-divider__default.cms-indentation__default-bottom.cms-indentation__category-carousel--small.ng-star-inserted > elk-category-collection > nav > ul > li:nth-child(3) > a > elk-cms-img > picture > img").click()
        #self.driver.execute_script("scrollBy(0,800)")
        actual = self.driver.find_element(By.CSS_SELECTOR,"#products > elk-component-loader-wrapper > elk-product-and-content-listing-view > div.product-list__products.ng-star-inserted > elk-product-tile-ff-wc-wrapper:nth-child(1) > elk-product-tile > div > div.product-tile__information.information > elk-price > span > span").text
        expected = "4990.-"
        self.assertEqual(actual,expected)
        self.driver.find_element(By.CSS_SELECTOR,"#sorting").click()
        self.driver.find_element(By.CSS_SELECTOR,"#sorting > option:nth-child(3)").click()
        time.sleep(2)
        s_actual = self.driver.find_element(By.CSS_SELECTOR,"#products > elk-component-loader-wrapper > elk-product-and-content-listing-view > div.product-list__products.ng-star-inserted > elk-product-tile-ff-wc-wrapper:nth-child(1) > elk-product-tile > div > div.product-tile__information.information > elk-price > span > span").text
        s_expected = "99996.-"
        self.assertEqual(s_actual,s_expected)
        
    def test_jamfora_assert(self):
        search1 = self.driver.find_element(By.CSS_SELECTOR,"#query-header")
        search1.send_keys("Playstation 5")
        search1.send_keys(Keys.RETURN)
        #time.sleep(10)
        self.driver.find_element(By.CSS_SELECTOR,"#products > elk-component-loader-wrapper > elk-product-and-content-listing-view > div.product-list__products.ng-star-inserted > elk-product-tile-ff-wc-wrapper:nth-child(2) > elk-product-tile > div > div.lift-above-gradient.product-tile__actions.ng-star-inserted > elk-product-actions > div > div > span").click()
        self.driver.find_element(By.CSS_SELECTOR,"#query-header").clear()
        search2 = self.driver.find_element(By.CSS_SELECTOR,"#query-header")
        search2.send_keys("Xbox Series S")
        search2.send_keys(Keys.RETURN)
        self.driver.find_element(By.CSS_SELECTOR,"#products > elk-component-loader-wrapper > elk-product-and-content-listing-view > div.product-list__products.ng-star-inserted > elk-product-tile-ff-wc-wrapper:nth-child(1) > elk-product-tile > div > div.lift-above-gradient.product-tile__actions.ng-star-inserted > elk-product-actions > div > div > div").click()
        self.driver.find_element(By.XPATH,"/html/body/elk-app/ng-component/elk-base-template/mat-sidenav-container/mat-sidenav-content/div[2]/elk-component-loader-wrapper/elk-compare-banner/elk-desktop-compare-banner/div/button").click()
        name1 = self.driver.find_element(By.XPATH,"/html/body/div[7]/div[2]/div/mat-dialog-container/elk-compare-overlay/div/div/div/elk-compare-scroller-group/div[1]/elk-compare-header/div/div/elk-compare-scroller/div/div/div/div[3]").text
        n_expected1 = "PlayStation 5 (2022)"
        self.assertEqual(name1,n_expected1)
        price1 = self.driver.find_element(By.XPATH,"/html/body/div[7]/div[2]/div/mat-dialog-container/elk-compare-overlay/div/div/div/elk-compare-scroller-group/div[1]/elk-compare-header/div/div/elk-compare-scroller/div/div/div/div[4]/elk-price/span/span").text
        p_expected1 = "6990.-"
        self.assertEqual(price1,p_expected1)
        name2 = self.driver.find_element(By.XPATH,"/html/body/div[7]/div[2]/div/mat-dialog-container/elk-compare-overlay/div/div/div/elk-compare-scroller-group/div[1]/elk-compare-header/div/div/elk-compare-scroller/div/div/div/div[8]").text
        n_expected2 = "Xbox Series S 512GB (vit)"
        self.assertEqual(name2,n_expected2)
        price2 = self.driver.find_element(By.XPATH,"/html/body/div[7]/div[2]/div/mat-dialog-container/elk-compare-overlay/div/div/div/elk-compare-scroller-group/div[1]/elk-compare-header/div/div/elk-compare-scroller/div/div/div/div[9]/elk-price/span/span").text
        p_expected2 = "3895.-"
        self.assertEqual(price2,p_expected2)
        time.sleep(2)

    def tearDown(self):
        self.driver.delete_all_cookies()
        self.driver.close()
        

