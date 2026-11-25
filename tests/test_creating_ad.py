from constants import TEST_PASSWORD, TIMEOUT, BASE_URL, PRODUCT_NAME,\
    PRODUCT_DESCRIPTION, PPRODUCT_PRICE, PRODUCT_DESCRIPTION, SELECTED_CITY
from locators import Locators
from helpers import open_login_form, login
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestCreatingAd:

    def test_creating_ad_by_unauthorized_user_requires_login(self, driver):
        driver.get(BASE_URL)
        WebDriverWait(driver, TIMEOUT).until(
            EC.element_to_be_clickable(Locators.PLACE_AD_BUTTON)).click()
        window_login_to_place_ad = WebDriverWait(driver, TIMEOUT).until(
            EC.visibility_of_element_located(Locators.WINDOW_LOGIN_TO_PLACE_AD))

        assert window_login_to_place_ad.text == 'Чтобы разместить объявление, авторизуйтесь'


    def test_creating_ad_by_authorized_user_success(self, driver, registered_user):
        email = registered_user
        open_login_form(driver)
        login(driver, email, TEST_PASSWORD)
        
        wait = WebDriverWait(driver, TIMEOUT)
        
        wait.until(EC.element_to_be_clickable(Locators.PLACE_AD_BUTTON)).click()
        
        driver.find_element(*Locators.PRODUCT_NAME_INPUT_FIELD).send_keys(PRODUCT_NAME)
        driver.find_element(*Locators.PRODUCT_DESCRIPTION_INPUT_FIELD).send_keys(PRODUCT_DESCRIPTION)
        driver.find_element(*Locators.PRODUCT_PRICE_INPUT_FIELD).send_keys(PPRODUCT_PRICE)

        driver.find_element(*Locators.CATEGORY_DROP_DOWN_LIST_ARROW_BUTTON).click()
        wait.until(EC.element_to_be_clickable(Locators.CATEGORY_DROP_DOWN_LIST_ITEM)).click()
        driver.find_element(*Locators.CITY_DROP_DOWN_LIST_ARROW_BUTTON).click()
        wait.until(EC.element_to_be_clickable(Locators.CITY_DROP_DOWN_LIST_ITEM)).click()
        wait.until(EC.element_to_be_clickable(Locators.CONDITION_OF_PRODUCT)).click()
        driver.find_element(*Locators.PUBLISH_BUTTON).click()

        wait.until(EC.url_changes(driver.current_url))
        wait.until(EC.element_to_be_clickable(Locators.AVATAR_PLACEHOLDER)).click()

        wait.until(EC.presence_of_element_located(Locators.CARD_IN_MY_ADS_BLOCK))

        cards = driver.find_elements(*Locators.TEST_CARD_IN_MY_ADS_BLOCK)

        assert len(cards) > 0, f"Объявление '{PRODUCT_NAME}' не найдено в блоке 'Мои объявления'"

        actual_city = cards[0].find_element(*Locators.TEST_CARD_PPRODUCT_CITY_IN_MY_ADS_BLOCK).text
        actual_price = cards[0].find_element(*Locators.TEST_CARD_PPRODUCT_PRICE_IN_MY_ADS_BLOCK).text

        assert actual_city == SELECTED_CITY, f"Ожидался город '{SELECTED_CITY}', получен '{actual_city}'"
        assert actual_price == f"{PPRODUCT_PRICE} ₽", f"Ожидалась цена '{PPRODUCT_PRICE} ₽', получена '{actual_price}'"

      
    