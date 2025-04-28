from selenium.webdriver.support.select import Select
from pages.base_page import BasePage
from locators import Locators


class MainPage(BasePage):

    def fill_name_email_message(self):
        self.fill_name()
        self.fill_email()
        self.fill_message()

    def scroll_to_quote_form(self):
        self.scroll(Locators.quote_header)

    def fill_email(self, email='asd@asd.com'):
        self.wait_and_find_element(Locators.email_fill).send_keys(email)

    def fill_name(self, name='Vladimir'):
        self.wait_and_find_element(Locators.name_fill).send_keys(name)

    def fill_message(self, message='Возьмите на работу'):
        self.wait_and_find_element(Locators.message_fill).send_keys(message)

    def request_button_click(self):
        self.click(Locators.request_button)

    def select_b_service(self):
        select_element = self.wait_and_find_element(Locators.service_selector)
        select = Select(select_element)
        select.select_by_value('B Service')

    def select_a_service(self):
        select_element = self.wait_and_find_element(Locators.service_selector)
        select = Select(select_element)
        select.select_by_value('A Service')

    def select_c_service(self):
        select_element = self.wait_and_find_element(Locators.service_selector)
        select = Select(select_element)
        select.select_by_value('C Service')

    def is_form_sent_text_displayed(self):
        return self.is_element_displayed(Locators.form_sent_status)
