from selenium.webdriver.common.by import By
from time import sleep

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"


def test_add_to_cart_button_is_displayed(browser):
    browser.get(link)
    # sleep(30)
    button = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert button, 'Button was not found!'
