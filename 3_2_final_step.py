import time
import unittest

from selenium import webdriver  # webdriver это и есть набор команд для управления браузером
from selenium.webdriver.common.by import By  # импортируем класс By, который позволяет выбрать способ поиска элемента
from selenium.webdriver.chrome.service import Service  # Импорт для управления службой ChromeDriver
from selenium.webdriver.chrome.options import Options  # Импорт для настройки параметров запуска браузера
from webdriver_manager.chrome import ChromeDriverManager  # Импорт для автоматической загрузки ChromeDriver


class TestRegister(unittest.TestCase):  # создаем класс, хранящий методы для теста
    def check_registration_fields(self, page_number):  # прописываем в метод функцию
        chrome_options = Options()
        chrome_service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
        link = f"http://suninjuly.github.io/registration{page_number}.html"
        driver.get(link)

        driver.find_element(By.CSS_SELECTOR, '.first_block .form-control.first').send_keys('Afonya')
        driver.find_element(By.CSS_SELECTOR, '.first_block .form-control.second').send_keys('Ivanov')
        driver.find_element(By.CSS_SELECTOR, '.first_block .form-control.third').send_keys('jena@jizni.net')

        button = driver.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = driver.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Something went wrong")

        time.sleep(10)
        driver.quit()

    def test_registration1(self):  # запускаем тест для первой ссылки
        self.check_registration_fields(1)

    def test_registration2(self):  # запускаем тест для второй ссылки
        self.check_registration_fields(2)


if __name__ == "__main__":
    unittest.main()
