from selenium.webdriver.common.by import By

class Locators:
    name_fill = By.XPATH, './/input[@placeholder="Your Name"]'
    email_fill = By.XPATH, './/input[@placeholder="Your Email"]'
    message_fill = By.XPATH, './/textarea[@id="message"]'
    quote_header = By.XPATH, './/h5[text()="Request A Quote"]'
    request_button = By.XPATH, './/button[text()="Request A Quote"]'
    service_selector = By.XPATH, './/select[@id="service"]'
    form_sent_status = By.XPATH, './/div[@id="formStatus"]'
