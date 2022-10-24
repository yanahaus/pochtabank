from application import Application
import pytest
from selenium.webdriver.common.by import By


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

#Позитивный тест
def test_send_form(app):
    app.open_feedback_page()
    app.filled_form()
    app.send_form()
    assert app.wd.find_element(By.CSS_SELECTOR, "div.style_title__OJJny").text == 'Заявка отправлена'
