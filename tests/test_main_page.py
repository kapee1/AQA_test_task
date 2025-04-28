import allure
from conftest import driver
from pages.main_page import MainPage


class TestMainPage:

    @allure.title('Успешный запрос quote')
    def test_quote_request_success(self, driver):
        main = MainPage(driver)
        main.scroll_to_quote_form()
        main.fill_name_email_message()
        main.select_b_service()
        main.request_button_click()

        assert main.is_form_sent_text_displayed()

    @allure.title('Длинна имени ниже допустимого')
    def test_short_name_for_quote_failed(self, driver):
        main = MainPage(driver)
        main.scroll_to_quote_form()
        main.fill_name('A')
        main.fill_email()
        main.fill_message()
        main.select_b_service()
        main.request_button_click()

        assert main.is_form_sent_text_displayed() == False

    @allure.title('Нет email')
    def test_no_email_for_quote_failed(self, driver):
        main = MainPage(driver)
        main.scroll_to_quote_form()
        main.fill_name()
        main.fill_message()
        main.select_b_service()
        main.request_button_click()

        assert main.is_form_sent_text_displayed() == False




