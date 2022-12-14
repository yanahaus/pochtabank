import allure

from application import Application
import pytest
from selenium.webdriver.common.by import By
from request import Request


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


#Позитивный тест
@allure.title("Sending form")
def test_send_form(app):
    with allure.step('Feeling form'):
        app.open_feedback_page()
        app.filled_form(Request(fio="Jon Snow", phone="+7 (111) 111-11-11", email="test@gmail.com", message="test"))
        app.screen_shot('Form feeling')
    with allure.step('Sending form'):
        app.send_form()
        assert app.wd.find_element(By.CSS_SELECTOR, "div.style_title__OJJny").text == "Заявка отправлена"
        app.screen_shot('Form sending')


#Негативный тест
@allure.title('Отправка формы обратной связи')
def test_send_empty_form(app):
    with allure.step('Отправка формы'):
        app.open_feedback_page()
        app.filled_form(Request(fio="", phone="", email="", message=""))
        app.screen_shot('Форма заполнена')
        app.send_form()
        assert app.wd.find_element(By.CSS_SELECTOR, "div.style_title__OJJny").text == "Заявка отправлена"

