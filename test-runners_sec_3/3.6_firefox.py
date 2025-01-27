from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

# Настройка GeckoDriver

ff_options = Options()
ff_service = Service(GeckoDriverManager().install())

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
browser = webdriver.Firefox(service=ff_service, options=ff_options)

link = 'https://stepik.org/lesson/25969/step/8'
browser.get(link)
