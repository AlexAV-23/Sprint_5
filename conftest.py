import uuid
import pytest
import requests
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from constants import TEST_PASSWORD, BASE_URL


DRIVER_PATH = Path(__file__).resolve().parent / 'drivers' / 'yandexdriver'


@pytest.fixture
def driver():
    # setup до yield 
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--headless=new")
    service = Service(executable_path=str(DRIVER_PATH))
    driver = webdriver.Chrome(service=service, options=options)
    yield driver

    # teardown после yield
    driver.quit()


@pytest.fixture
def mail_generation():
    # генерация рандомной почты
    return f"uid_{uuid.uuid4().hex[:10]}@yandex.ru"


@pytest.fixture
def wrong_mail_generation():
    # генерация неправильной рандомной почты
    return f"uid_{uuid.uuid4().hex[:10]}@yandex"


@pytest.fixture
def registered_user(mail_generation):
    email = mail_generation
    password = TEST_PASSWORD

    response = requests.post(
        f"{BASE_URL}/api/signup",
        json={
            "email": email,
            "password": password,
            "submitPassword": password,
        })

    assert response.status_code == 201, \
        f"Precondition: пользователь не создан, код {response.status_code}, ответ: {response.text}"

    return email



