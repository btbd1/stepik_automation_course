import time

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

try:
    driver.get("http://suninjuly.github.io/huge_form.html")
    elements = driver.find_elements(By.TAG_NAME, "input")
    for element in elements:
        element.send_keys("Мой ответ")

    button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    driver.quit()
