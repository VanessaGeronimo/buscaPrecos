from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_all_elements_located, presence_of_element_located, element_to_be_clickable
from time import sleep

from models.Product import Product


class ProductSearcher:

    target_url = 'https://www.magazineluiza.com.br/'

    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

        self.wait_60 = WebDriverWait(self.driver, 60)
        self.wait_10 = WebDriverWait(self.driver, 10)

    def search(self, product_name):

        self.driver.get(self.target_url)

        self.try_type_search(product_name)

        search_buttom = self.driver.find_element(
            By.XPATH, '//*[@id="btnHeaderSearch"]')
        search_buttom.click()

        try:
            product_results = self.wait_10.until(presence_of_element_located(
                (By.XPATH, '//div[@class="productShowCaseContent"]')))
        except TimeoutException:
            product_results = self.wait_60.until(presence_of_element_located(
                (By.XPATH, '//div[@class="nm-search-results-container"]')))

        self.wait_60.until(presence_of_all_elements_located(
            (By.XPATH, '//li[contains(@class, "product")]')))
        sleep(2)

        products_web_element = product_results.find_elements(
            By.XPATH, './/ul[contains(@class,"neemu-products-container")]//li[contains(@class, "product")]')

        products = list(
            filter(
                lambda product: True if product != None else False,
                map(self.get_product, products_web_element)
            )
        )

        return products

    def get_product(self, product_web_element):

        try:
            product_name = self.get_name_from_web_element(product_web_element)
        except NoSuchElementException:
            product_name = ''

        try:
            product_price = self.get_price_from_web_element(
                product_web_element)
        except NoSuchElementException:
            if 'unavailable product' not in product_web_element.get_attribute('innerHTML'):
                print(product_web_element.get_attribute('innerHTML'))
                input('espera')

            product_price = 0

        try:
            product_old_price = self.get_old_price_from_web_element(
                product_web_element)
        except NoSuchElementException:
            product_old_price = 0

        return Product(product_name, product_price, product_old_price)

    def get_name_from_web_element(self, web_element):
        return web_element.find_element(
            By.XPATH,
            './/h2[@class="nm-product-name"]'
        ).get_attribute("textContent").strip()

    def get_price_from_web_element(self, web_element):
        price = web_element.find_element(
            By.XPATH,
            './/div[@class="nm-price-container"]'
        ).get_attribute("textContent").strip()

        clean_text = price.replace(u'\xa0', u' ')
        splited_text = clean_text.split(' ')
        return float(splited_text[1].replace('.', '').replace(',', '.'))

    def get_old_price_from_web_element(self, web_element):
        price = web_element.find_element(
            By.XPATH,
            './/div[@class="nm-old-price-container"]'
        ).get_attribute("textContent").strip()

        clean_text = price.replace(u'\xa0', u' ')
        splited_text = clean_text.split(' ')
        return float(splited_text[2].replace('.', '').replace(',', '.'))

    def try_type_search(self, text):
        for attemps in range(5):
            search_field = self.wait_60.until(element_to_be_clickable(
                (By.XPATH, '//input[@id="inpHeaderSearch"]')))
            try:
                search_field.send_keys(text)
                break
            except:
                sleep(3)
