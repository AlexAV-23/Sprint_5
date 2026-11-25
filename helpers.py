from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators
from constants import BASE_URL, TIMEOUT


def open_login_form(driver):
    # Открыть главную страницу и форму входа
    driver.get(BASE_URL)
    driver.find_element(*Locators.LOGIN_AND_REGISTRATION_BUTTON).click()


def login(driver, email, password):
    # Заполнить форму входа и отправить её
    WebDriverWait(driver, TIMEOUT).until(
        EC.visibility_of_element_located(Locators.EMAIL_INPUT_FIELD)).send_keys(email)
    driver.find_element(*Locators.PASSWORD_INPUT_FIELD).send_keys(password)
    WebDriverWait(driver, TIMEOUT).until(
        EC.element_to_be_clickable(Locators.LOGIN_BUTTON)).click()
    WebDriverWait(driver, TIMEOUT).until(
        EC.visibility_of_element_located(Locators.EXIT_BUTTON))


def open_registration_form(driver):
    # Открыть форму регистрации через кнопку «Нет аккаунта»
    driver.get(BASE_URL)
    driver.find_element(*Locators.LOGIN_AND_REGISTRATION_BUTTON).click()
    WebDriverWait(driver, TIMEOUT).until(
        EC.element_to_be_clickable(Locators.NO_ACCOUNT_BUTTON)).click()


def register(driver, email, password):
    # Заполнить форму регистрации
    WebDriverWait(driver, TIMEOUT).until(
        EC.visibility_of_element_located(Locators.EMAIL_INPUT_FIELD)).send_keys(email)
    driver.find_element(*Locators.PASSWORD_INPUT_FIELD).send_keys(password)
    driver.find_element(*Locators.PASSWORD_REPEAT_INPUT_FIELD).send_keys(password)
    driver.find_element(*Locators.CREATE_ACCOUNT_BUTTON).click()
