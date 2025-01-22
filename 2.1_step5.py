import time
import math

from selenium import webdriver  # webdriver это и есть набор команд для управления браузером
from selenium.webdriver.common.by import By  # импортируем класс By, который позволяет выбрать способ поиска элемента
from selenium.webdriver.chrome.service import Service  # Импорт для управления службой ChromeDriver
from selenium.webdriver.chrome.options import Options  # Импорт для настройки параметров запуска браузера
from webdriver_manager.chrome import ChromeDriverManager  # Импорт для автоматической загрузки ChromeDriver

# Настройка ChromeDriver

chrome_options = Options()
chrome_service = Service(ChromeDriverManager().install())

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

link = "https://suninjuly.github.io/math.html"


try:
    driver.get(link)

    def calc(n):
        return str(math.log(abs(12 * math.sin(int(n)))))

    # Ваш код, который заполняет поля
    x_element = driver.find_element(By.CSS_SELECTOR, 'label #input_value')
    x = x_element.text
    y = calc(x)

    driver.find_element(By.CSS_SELECTOR, '#answer').send_keys(y)
    driver.find_element(By.CSS_SELECTOR, '#robotCheckbox').click()
    driver.find_element(By.CSS_SELECTOR, '[for="robotsRule"]').click()

    # Отправляем заполненную форму
    driver.find_element(By.CSS_SELECTOR, ".btn.btn-default").click()

finally:
    # успеваем скопировать код
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    driver.quit()
