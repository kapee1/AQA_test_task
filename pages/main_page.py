from selenium.webdriver.support.select import Select
from pages.base_page import BasePage
from locators import Locators
import allure

class MainPage(BasePage):

    @allure.step('Заполнить все обязательные поля')
    def fill_name_email_message(self):
        self.fill_name()
        self.fill_email()
        self.fill_message()

    @allure.step('Скролл до формы Quote')
    def scroll_to_quote_form(self):
        self.scroll(Locators.quote_header)

    @allure.step('Заполнить поле email')
    def fill_email(self, email='asd@asd.com'):
        self.wait_and_find_element(Locators.email_fill).send_keys(email)

    @allure.step('Заполнить поле name')
    def fill_name(self, name='Vladimir'):
        self.wait_and_find_element(Locators.name_fill).send_keys(name)

    @allure.step('Заполнить поле message')
    def fill_message(self, message='Возьмите на работу'):
        self.wait_and_find_element(Locators.message_fill).send_keys(message)

    @allure.step('Клик по кнопке Request Quote')
    def request_button_click(self):
        self.click(Locators.request_button)

    @allure.step('Выбрать пункт B-Service')
    def select_b_service(self):
        select_element = self.wait_and_find_element(Locators.service_selector)
        select = Select(select_element)
        select.select_by_value('B Service')

    @allure.step('Выбрать пункт A-Service')
    def select_a_service(self):
        select_element = self.wait_and_find_element(Locators.service_selector)
        select = Select(select_element)
        select.select_by_value('A Service')

    @allure.step('Выбрать пункт C-Service')
    def select_c_service(self):
        select_element = self.wait_and_find_element(Locators.service_selector)
        select = Select(select_element)
        select.select_by_value('C Service')

    @allure.step('Проверка на отображение статуса отправления формы')
    def is_form_sent_text_displayed(self):
        return self.is_element_displayed(Locators.form_sent_status)
