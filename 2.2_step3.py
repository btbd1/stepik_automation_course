import time

from selenium import webdriver  # webdriver это и есть набор команд для управления браузером
from selenium.webdriver.common.by import By  # импортируем класс By, который позволяет выбрать способ поиска элемента
from selenium.webdriver.chrome.service import Service  # Импорт для управления службой ChromeDriver
from selenium.webdriver.chrome.options import Options  # Импорт для настройки параметров запуска браузера
from webdriver_manager.chrome import ChromeDriverManager  # Импорт для автоматической загрузки ChromeDriver
from selenium.webdriver.support.ui import Select  # для работы со списками


# Настройка ChromeDriver

chrome_options = Options()
chrome_service = Service(ChromeDriverManager().install())

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

link = "http://suninjuly.github.io/selects1.html"
link2 = "https://suninjuly.github.io/selects2.html"

try:
    driver.get(link)

    select = Select(driver.find_element(By.TAG_NAME, "select"))

    x = int(driver.find_element(By.ID, 'num1').text) + int(driver.find_element(By.ID, 'num2').text)
    select.select_by_value(str(x))
    driver.find_element(By.CLASS_NAME, 'btn.btn-default').click()

finally:
    # успеваем скопировать код
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    driver.quit()
