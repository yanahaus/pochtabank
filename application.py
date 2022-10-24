from selenium import webdriver
from selenium.webdriver.common.by import By

class Application:

    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.maximize_window()
        self.wd.implicitly_wait(5)

    def send_form(self):
        wd = self.wd
        wd.find_element(By.CSS_SELECTOR, ".style_button__xe2AP").click()
        wd.find_element(By.CSS_SELECTOR, ".style_button__UfDSA").click()

    def filled_form(self):
        wd = self.wd
        wd.find_element(By.NAME, "fio").click()
        wd.find_element(By.NAME, "fio").send_keys("тест")
        wd.find_element(By.NAME, "phone").click()
        wd.find_element(By.NAME, "phone").send_keys("+7 (111) 111-11-11")
        wd.find_element(By.NAME, "email").click()
        wd.find_element(By.NAME, "email").send_keys("test@gmail.com")
        wd.find_element(By.NAME, "message").click()
        wd.find_element(By.NAME, "message").send_keys("тест")
        wd.find_element(By.CSS_SELECTOR, ".style_checkmark___GZe2").click()

    def open_feedback_page(self):
        wd = self.wd
        wd.get("https://www.pochtabank.ru/feedback")

    def destroy(self):
        self.wd.quit()