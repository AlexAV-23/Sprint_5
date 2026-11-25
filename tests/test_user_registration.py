import pytest
from constants import TEST_PASSWORD, TIMEOUT, EXPECTED_RED
from locators import Locators
from helpers import open_registration_form, register
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestUserRegistration:

    def test_user_registration_success(self, driver, mail_generation):
        open_registration_form(driver)
        register(driver, mail_generation, TEST_PASSWORD)

        WebDriverWait(driver, TIMEOUT).until(
            EC.visibility_of_element_located(Locators.EXIT_BUTTON))


        user_name = driver.find_element(*Locators.PROFILE_TEXT_NAME).text
        assert driver.find_element(*Locators.AVATAR_PLACEHOLDER).is_displayed(), \
            "Не отображается блок аватара (заглушка)"
        assert user_name.strip() == 'User.', f"Ожидалось имя 'User.', получено: '{user_name}'"

    
    @pytest.mark.parametrize("field_name, wrapper_locator", [
        ("Email", Locators.EMAIL_ERROR_WRAPPER_INPUT),
        ("Пароль", Locators.PASSWORD_ERROR_WRAPPER_INPUT),
        ("Повторить пароль", Locators.SUBMITPASSWORD_ERROR_WRAPPER_INPUT),
    ])
    def test_user_registration_with_incorrect_email_shows_error(self, driver, wrong_mail_generation, field_name, wrapper_locator):
        open_registration_form(driver)
        register(driver, wrong_mail_generation, TEST_PASSWORD)

        error_message = WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located(Locators.EMAIL_ERROR_MESSAGE))
        color = driver.find_element(*wrapper_locator).value_of_css_property("border-color")
        assert color == EXPECTED_RED, f"Поле {field_name} не выделено красным (ожидаемое значение цвета {EXPECTED_RED})"
        assert error_message.text == 'Ошибка', "Под полем Email не отображается сообщение «Ошибка»"


    @pytest.mark.parametrize("field_name, wrapper_locator", [
        ("Email", Locators.EMAIL_ERROR_WRAPPER_INPUT),
        ("Пароль", Locators.PASSWORD_ERROR_WRAPPER_INPUT),
        ("Повторить пароль", Locators.SUBMITPASSWORD_ERROR_WRAPPER_INPUT),
    ])
    def test_user_registration_of_existing_user_shows_error(self, driver, registered_user, field_name, wrapper_locator):
        email = registered_user
        open_registration_form(driver)
        register(driver, email, TEST_PASSWORD)

        error_message = WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located(Locators.EMAIL_ERROR_MESSAGE))
        color = driver.find_element(*wrapper_locator).value_of_css_property("border-color")
        assert color == EXPECTED_RED, f"Поле {field_name} не выделено красным (ожидаемое значение цвета {EXPECTED_RED})"
        assert error_message.text == 'Ошибка', "Под полем Email не отображается сообщение «Ошибка»"


