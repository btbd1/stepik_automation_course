import os
from time import sleep
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

link = "https://suninjuly.github.io/file_input.html"

try:
    driver.get(link)

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
    # print(os.path.abspath(__file__))
    # print(os.path.abspath(os.path.dirname(__file__)))
    # print(file_path)
    driver.find_element(By.NAME, 'firstname').send_keys('Госпожа')
    driver.find_element(By.NAME, 'lastname').send_keys('Шапокляк')
    driver.find_element(By.NAME, 'email').send_keys('shapoklyak@mail.ru')
    driver.find_element(By.ID, 'file').send_keys(file_path)
    driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary').click()

finally:
    sleep(10)
    driver.quit()
