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
def test_send_form(app):
    app.open_feedback_page()
    app.filled_form(Request(fio="Jon Snow", phone="+7 (111) 111-11-11", email="test@gmail.com", message="test"))
    app.send_form()
    assert app.wd.find_element(By.CSS_SELECTOR, "div.style_title__OJJny").text == "Заявка отправлена"


#Негативный тест
def test_send_empty_form(app):
    app.open_feedback_page()
    app.filled_form(Request(fio="", phone="", email="", message=""))
    app.send_form()
    assert app.wd.find_element(By.CSS_SELECTOR, "div.style_title__OJJny").text == "Заявка отправлена"