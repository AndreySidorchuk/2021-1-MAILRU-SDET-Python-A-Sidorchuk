from selenium.webdriver.common.by import By


class AuthorizationLocators:
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'div[class^="responseHead-module-button"]')
    EMAIL_INPUT = (By.NAME, 'email')
    PASSWORD_INPUT = (By.NAME, 'password')
    CHECK_AUTH_SUCCESS = (By.CSS_SELECTOR, 'ul[class^="rightMenu-module-rightMenu"]')


class BasePageLocators:
    WRAP_BUTTON = (By.CSS_SELECTOR, 'div[class^="right-module-rightButton"]')
    LOGOUT_BUTTON = (By.XPATH, '//a[contains(@href,"logout")]')
    PROFILE_BUTTON = (By.CSS_SELECTOR, 'a[href="/profile"]')
    NUMBER = (By.CSS_SELECTOR, 'input[maxlength="20"]')
    FIO = (By.CSS_SELECTOR, '.input__inp.js-form-element')
    SAVE = (By.CLASS_NAME, 'button__text')
    AUDITORS = (By.CSS_SELECTOR, 'a[href="/segments"]')
    STATISTIC_SUM = (By.CSS_SELECTOR, 'a[href="/statistics/summary"]')