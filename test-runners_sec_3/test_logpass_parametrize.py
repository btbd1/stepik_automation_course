import pytest
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


@pytest.mark.parametrize('ufo_link', ['236895', '236896', '236897', '236898', '236899', '236903', '236904', '236905'])
# @pytest.mark.parametrize('ufo_link', ['236895'])
def test_login_stepik(browser, ufo_link):
    link = f"https://stepik.org/lesson/{ufo_link}/step/1?auth=login"
    browser.get(link)
    time.sleep(3)
    browser.find_element(By.NAME, 'login').send_keys("input_email")
    browser.find_element(By.NAME, 'password').send_keys("input_password")
    browser.find_element(By.CSS_SELECTOR, '#login_form > button').click()
    time.sleep(3)
    try:
        again_button = browser.find_element(By.CLASS_NAME, "again-btn")
        again_button.click()
        ok_button = browser.find_element(By.CSS_SELECTOR, '.modal-popup__footer > button:nth-child(1)')
        ok_button.click()
    except NoSuchElementException:
        # Кнопка не найдена, продолжаем выполнение теста
        pass
    time.sleep(5)
    answer = math.log(int(time.time()))
    textarea = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.ember-text-area')))
    time.sleep(5)
    textarea.send_keys(str(answer))
    time.sleep(3)
    submit_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.submit-submission')))
    submit_button.click()
    time.sleep(3)
    x = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.smart-hints__hint')))
    x_text = x.text
    assert x_text == 'Correct!', f'Does not match in this link {ufo_link}, returned {x_text}'
