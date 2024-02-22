from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging
from selenium.webdriver.common.alert import Alert
import yaml

class TestSearchLocators:
    ids = dict()
    with open("./locators.yaml") as f:
        locators = yaml.safe_load(f)
    for locator in locators["xpath"].keys():
        ids[locator] = (By.XPATH, locators["xpath"][locator])
    for locator in locators["css"].keys():
        ids[locator] = (By.CSS_SELECTOR, locators["css"][locator])

class OperationsHelper(BasePage):
    def enter_text_info_field(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.debug(f"send {word} to element {element_name}")

        field = self.find_element((locator))
        if not field:
            logging.error(f"element {locator} not found")
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f" exception while operation with {locator}")
            return False
        return True

# ВВОД ТЕКСТА
    def enter_login(self, word):
        self.enter_text_info_field(TestSearchLocators.ids["LOCATOR_LOGIN_FIELD"], word, description="login form")

    def enter_pass(self, word):
        self.enter_text_info_field(TestSearchLocators.ids["LOCATOR_PASS_FIELD"], word, description="password form")

    def enter_post_title(self, word):
        self.enter_text_info_field(TestSearchLocators.ids["LOCATOR_POST_TITLE"], word, description="post_title")

    def enter_post_descrition(self, word):
        self.enter_text_info_field(TestSearchLocators.ids["LOCATOR_POST_DESCRIPTION"], word, description="post_descrition")

    def enter_post_content(self, word):
        self.enter_text_info_field(TestSearchLocators.ids["LOCATOR_POST_CONTENT"], word, description="post_content")

    def enter_name_for_contact(self, word):
        self.enter_text_info_field(TestSearchLocators.ids["LOCATOR_CONTACT_NAME"], word, description="contact name form")


    def enter_emael_for_contact(self, word):
        self.enter_text_info_field(TestSearchLocators.ids["LOCATOR_CONTACT_EMAIL"], word, description="contact email form")

    def enter_content_for_contact(self, word):
        self.enter_text_info_field(TestSearchLocators.ids["LOCATOR_CONTENT_CONTACT"], word, description="content for contact form")


    def contact_us_alert(self, expected_text):
        logging.info("Get alert text")
        text = self.get_alert_text()
        logging.info(text)
        return text


# НАЖИМАНИЕ КНОПОК
    def click_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception("exception with click")
            return False
        logging.debug(f"Clicked {element_name} button")
        return True

    def click_login_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_LOGIN_BTN"], description="login")

    def click_create_post_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_CREATE_POST_BUTTON"], description="create_post")

    def click_save_post_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_POST_SAVE_BUTTON"], description="save_post")

    def click_contact_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_CONTACT_BTN"], description="contact")

    def click_contact_us_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_SEND_REPORT"], description="contact send")

    def click_about(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_ABOUT"], description="contact send")

# ПОЛУЧЕНИЕ ТЕКСТА
    def get_text_from_elemet(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=3)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f"exception while get test from {element_name}")
            return None
        logging.debug(f"we find text {text} in field {element_name}")
        return text
    def get_error_text(self):
        return self.get_text_from_elemet(TestSearchLocators.ids["LOCATOR_ERROR_FIELD"])

    def get_success_text(self):
        return self.get_text_from_elemet(TestSearchLocators.ids["LOCATOR_SUCCESS_LOGIN"])

    def check_new_post_title(self):
        return self.get_text_from_elemet(TestSearchLocators.ids["LOCATOR_CHECK_NEW_POST"])

    def get_contact_us_text(self):
        return self.get_text_from_elemet(TestSearchLocators.ids["LOCATOR_CONTACT_US_MSG"])

    def get_text(self):
        return self.get_text_from_elemet(TestSearchLocators.ids["LOCATOR_TEXT"])

    def get_alert(self):
        logging.info("get alert text")
        text = self.get_alert_text()
        logging.info(text)
        return text

    def get_header_font_size(self):
        header_locator = TestSearchLocators.ids[
            "LOCATOR_TEXT"]  # Replace with the actual locator for your header
        header_element = self.find_element(header_locator, time=3)

        if not header_element:
            logging.error("Header element not found")
            return None

        try:
            font_size = header_element.value_of_css_property("font-size")
            return int(font_size.replace("px", ""))
        except Exception as e:
            logging.exception(f"Exception while getting header font size: {str(e)}")
            return None