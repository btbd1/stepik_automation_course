from time import sleep
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

link = "http://suninjuly.github.io/execute_script.html"

try:
    driver.get(link)

    def calc(n):
        return str(math.log(abs(12 * math.sin(int(n)))))

    x = driver.find_element(By.ID, 'input_value').text
    y = calc(x)

    driver.find_element(By.ID, 'answer').send_keys(y)  # вставляем полученный результат в поле
    driver.find_element(By.CSS_SELECTOR, '#robotCheckbox').click()  # ставим галку в чекбокс
    button = driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary') # переменная для эл-та, к которому скроллим
    driver.execute_script("return arguments[0].scrollIntoView(true);", button)  # скрипт скролла к эл-ту
    driver.find_element(By.CSS_SELECTOR, '#robotsRule').click()
    button.click()

finally:
    sleep(10)
    driver.quit()
