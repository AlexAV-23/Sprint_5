from selenium.webdriver.common.by import By
from constants import SELECTED_CATEGORY, SELECTED_CITY,PRODUCT_NAME

# локаторы в виде кортежей из двух элементов: метод поиска и значение селектора

class Locators:

    # локаторы для test_user_registration
    LOGIN_AND_REGISTRATION_BUTTON = (By.XPATH, '//button[normalize-space()="Вход и регистрация"]')
    LOGIN_BUTTON = (By.XPATH, '//button[normalize-space()="Войти"]')
    NO_ACCOUNT_BUTTON = (By.XPATH, '//button[normalize-space()="Нет аккаунта"]')
    EMAIL_INPUT_FIELD = (By.XPATH, '//input[@name="email"]')
    PASSWORD_INPUT_FIELD = (By.XPATH, '//input[@name="password"]')
    PASSWORD_REPEAT_INPUT_FIELD = (By.XPATH, '//input[@name="submitPassword"]')
    CREATE_ACCOUNT_BUTTON = (By.XPATH, '//button[normalize-space()="Создать аккаунт"]')
    EXIT_BUTTON = (By.XPATH, '//button[normalize-space()="Выйти"]')
    PROFILE_TEXT_NAME = (By.CSS_SELECTOR, '.profileText.name')
    AVATAR_PLACEHOLDER = (By.CSS_SELECTOR, "button.circleSmall")

    # test_user_registration_incorrect_email_shows_error
    EMAIL_ERROR_WRAPPER_INPUT = (By.XPATH, "//input[@name='email']/parent::div")
    PASSWORD_ERROR_WRAPPER_INPUT = (By.XPATH, "//input[@name='password']/parent::div")
    SUBMITPASSWORD_ERROR_WRAPPER_INPUT = (By.XPATH, "//input[@name='submitPassword']/parent::div")
    EMAIL_ERROR_MESSAGE = (By.XPATH, "//input[@name='email']/ancestor::div/span[contains(@class, 'input_span')]")

    # test_creating_ad_by_unauthorized_user_requires_login
    PLACE_AD_BUTTON = (By.XPATH, "//button[text()='Разместить объявление']")
    WINDOW_LOGIN_TO_PLACE_AD = (By.XPATH, "//h1 [normalize-space()='Чтобы разместить объявление, авторизуйтесь']")

    # test_creating_ad_by_authorized_user_success
    PRODUCT_NAME_INPUT_FIELD = (By.XPATH, '//input[@name="name"]')
    PRODUCT_DESCRIPTION_INPUT_FIELD = (By.XPATH, '//textarea[@name="description"]')
    PRODUCT_PRICE_INPUT_FIELD = (By.XPATH, '//input[@name="price"]')
    
    CATEGORY_DROP_DOWN_LIST_ARROW_BUTTON = (By.XPATH, '//input[@name="category"]/parent::div/button')
    CATEGORY_DROP_DOWN_LIST_ITEM = (By.XPATH, f'//button[.//span[normalize-space()="{SELECTED_CATEGORY}"]]')
    
    CITY_DROP_DOWN_LIST_ARROW_BUTTON = (By.XPATH, '//input[@name="city"]/parent::div/button')
    CITY_DROP_DOWN_LIST_ITEM = (By.XPATH, f'//button[.//span[normalize-space()="{SELECTED_CITY}"]]')
    
    CONDITION_OF_PRODUCT = (By.XPATH, '//input[@value="Б/У"]/parent::div/div')
    PUBLISH_BUTTON = (By.XPATH, '//button[text()="Опубликовать"]')
    CARD_IN_MY_ADS_BLOCK = (By.XPATH, '//div[./h1[text()="Мои объявления"]]//div[@class="card"]')
    TEST_CARD_IN_MY_ADS_BLOCK = (By.XPATH, '//div[./h1[text()="Мои объявления"]]//div[@class="card"]'\
        f"[.//h2[normalize-space()='{PRODUCT_NAME}']]")
    TEST_CARD_PPRODUCT_CITY_IN_MY_ADS_BLOCK = (By.XPATH,'.//div[@class="about"]/h3[@class="h3"]')
    TEST_CARD_PPRODUCT_PRICE_IN_MY_ADS_BLOCK = (By.XPATH,'.//div[@class="price"]/h2[@class="h2"]')
    

