from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


def getDriver():
    # Configurar y devolver el driver de Selenium (en este caso, Chrome)
    options = Options()
    # options.add_argument("--headless")
    driver_path = r"C:\Users\USUARIO\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=options)
    return driver