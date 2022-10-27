from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from request import Request
import allure
from selenium.webdriver.support.wait import WebDriverWait
from allure_commons.types import AttachmentType

class Application:
    def __init__(self):
        options = Options()
        options.headless = False
        self.wd = webdriver.Chrome(options=options)
        #self.wd.maximize_window()
        self.wd.set_window_size(1920, 1080)
        self.wd.implicitly_wait(25)

    def send_form(self):
        wd = self.wd
        wd.find_element(By.CSS_SELECTOR, ".style_button__xe2AP").click()
        wd.find_element(By.CSS_SELECTOR, ".style_button__UfDSA").click()

    def filled_form(self, request):
        wd = self.wd
        wd.find_element(By.NAME, "fio").click()
        wd.find_element(By.NAME, "fio").send_keys(request.fio)
        wd.find_element(By.NAME, "phone").click()
        wd.find_element(By.NAME, "phone").send_keys(request.phone)
        wd.find_element(By.NAME, "email").click()
        wd.find_element(By.NAME, "email").send_keys(request.email)
        wd.find_element(By.NAME, "message").click()
        wd.find_element(By.NAME, "message").send_keys(request.message)
        wd.find_element(By.CSS_SELECTOR, ".style_checkmark___GZe2").click()


    def open_feedback_page(self):
        wd = self.wd
        wd.get("https://www.pochtabank.ru/")
        wd.find_element(By.LINK_TEXT, "Задать вопрос").click()

    def destroy(self):
        self.wd.quit()


    def screen_shot(self, name):
        wait = WebDriverWait(self.wd, 50)
        wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
        allure.attach(self.wd.get_screenshot_as_png(), name=name, attachment_type=AttachmentType.PNG)
