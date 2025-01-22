from webdriver_manager.chrome import ChromeDriverManager

path_to_driver = ChromeDriverManager().install()
print(f"Драйвер установлен по пути: {path_to_driver}")