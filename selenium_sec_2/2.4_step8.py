from time import sleep
import math
from selenium import webdriver  # webdriver это и есть набор команд для управления браузером
from selenium.webdriver.common.by import By  # импортируем класс By, который позволяет выбрать способ поиска элемента
from selenium.webdriver.chrome.service import Service  # Импорт для управления службой ChromeDriver
from selenium.webdriver.chrome.options import Options  # Импорт для настройки параметров запуска браузера
from webdriver_manager.chrome import ChromeDriverManager  # Импорт для автоматической загрузки ChromeDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Настройка ChromeDriver

chrome_options = Options()
chrome_service = Service(ChromeDriverManager().install())

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

link = 'http://suninjuly.github.io/explicit_wait2.html'

try:
    driver.get(link)

    WebDriverWait(driver, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '100'))
    driver.find_element(By.ID, 'book').click()

    def calc(n):
        return str(math.log(abs(12 * math.sin(int(n)))))

    x = driver.find_element(By.ID, 'input_value').text
    y = calc(x)

    driver.find_element(By.ID, 'answer').send_keys(y)
    driver.find_element(By.ID, 'solve').click()

finally:
    sleep(10)
    driver.quit()
