from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'div[class^="responseHead-module-button"]')
    EMAIL_INPUT_FIELD = (By.NAME, 'email')
    PASSWORD_INPUT_FIELD = (By.NAME, 'password')
    ENTER_TO_PROFILE = (By.CSS_SELECTOR, 'div[class^="authForm-module-button"]')
    CHECK_AUTH_SUCCESS = (By.CSS_SELECTOR, 'div[class^="rightMenu-module-rightMenu"]')
    CHECK_FAIL_AUTH = (By.CLASS_NAME, "formMsg_title")


class DashboardPageLocators:
    CREATE_CAMPAIGN = (By.CSS_SELECTOR, 'a[href="/campaign/new"]')
    CREATE_CAMPAIGN_BUTTON = (By.XPATH, "//div[text()='Создать кампанию']/parent::div")

    CHOOSE_TYPE_BUTTON = (By.XPATH, "//div[text()='Трафик']/parent::div")
    INPUT_URL = (By.XPATH, "//input[@placeholder='Введите ссылку']")
    AD_TYPE_BANNER_BUTTON = (By.XPATH, "//span[text()='Баннер']/parent::div")
    UPLOAD_INPUT = (By.XPATH, "//div[contains(@class, 'roles-module-buttonWrap')]/div/input")
    IMAGE_CROPPER_SAVE_BUTTON = (By.XPATH, "//input[contains(@class, 'image-cropper__save')]")
    CAMPAIGN_NAME_INPUT = (By.XPATH, "//div[contains(@class, 'input_campaign-name')]/div/input")
    FINAL_BUTTON = (By.XPATH, "//div[text()='Создать кампанию']/parent::button")
    CAMPAIGN = (By.XPATH, '//a[@title="{}"]')
    TABLE_ELEMENT = (By.XPATH, "//div[contains(@class, 'nameCell') and text()='Итого']")

    AUDITORS = (By.XPATH, "//a[@href='/segments']")


class SegmentPageLocators:
    CREATE_SEGMENT = (By.CSS_SELECTOR, 'a[href="/segments/segments_list/new/"]')
    CREATE_SEGMENT_BUTTON = (By.CLASS_NAME, 'button_submit')
    SEGMENT_TYPE_GAMES = (By.XPATH, "//div[text()='Приложения и игры в соцсетях']")
    SEGMENT_CHECKBOX = (By.CLASS_NAME, 'adding-segments-source__checkbox')
    SEGMENT_ADD_BUTTON = (By.XPATH, "//div[text()='Добавить сегмент']/parent::button")
    SEGMENT_NAME_INPUT_FIELD = (By.XPATH, "//div[contains(@class, 'input_create-segment-form')]//div//input")
    FINAL_BUTTON = (By.XPATH, "//div[text()='Создать сегмент']/parent::button")
    NEW_SEGMENT = (By.XPATH, '//a[@title="{}"]')
    NEW_SEGMENT_NAME = (By.XPATH, '//a[@class="adv-camp-cell adv-camp-cell_name"]')

    @staticmethod
    def created_segment_name_node(name: str):
        return By.XPATH, f"//a[text()='{name}']/parent::div/parent::div"

    DELETE_SEGMENT_BUTTON = (By.XPATH, ".//following-sibling::div[4]//span")
    DELETE_SEGMENT = (By.XPATH, "//div[text()='Удалить']/parent::button")
    TABLE_HEADER = (By.XPATH, "//div[contains(@class, 'page_segments__title')]")
