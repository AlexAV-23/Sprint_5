from constants import TEST_PASSWORD,TIMEOUT
from locators import Locators
from helpers import open_login_form, login
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class TestUsersLoginLogout:

    def test_user_login_success(self, driver, registered_user):
        email = registered_user
        open_login_form(driver)
        login(driver, email, TEST_PASSWORD)
        
        user_name = driver.find_element(*Locators.PROFILE_TEXT_NAME).text
        assert driver.find_element(*Locators.AVATAR_PLACEHOLDER).is_displayed(), \
            "Не отображается блок аватара (заглушка)"
        assert user_name.strip() == 'User.', f"Ожидалось имя 'User.', получено: '{user_name}'"


    def test_user_logout_success(self, driver, registered_user):
        email = registered_user
        open_login_form(driver)
        login(driver, email, TEST_PASSWORD)  

        driver.find_element(*Locators.EXIT_BUTTON).click()
        login_and_registration_button = WebDriverWait(driver, TIMEOUT).until(
            EC.visibility_of_element_located(Locators.LOGIN_AND_REGISTRATION_BUTTON))

        assert len(driver.find_elements(*Locators.AVATAR_PLACEHOLDER)) == 0, \
            "После выхода аватар по-прежнему отображается"
        assert len(driver.find_elements(*Locators.PROFILE_TEXT_NAME)) == 0, \
            "После выхода имя User по-прежнему отображается"
        assert login_and_registration_button.text == 'Вход и регистрация'