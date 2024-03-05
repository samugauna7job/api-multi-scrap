import time
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


def getddjj1879(driver, rut, clave):
    
    print("este usuario se esta ejecutando")
    print(rut, clave)
    driver.get('https://www4.sii.cl/djconsultarentaui/internet/#/')
    wait = WebDriverWait(driver, 40)
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="anuales"]/div[3]/table/thead/tr/th[3]/a')))
    time.sleep(1)
    
    resultados = {  # Initialize resultados dictionary with all keys set to 'Empty'
        'codigo': 'Empty',
        'totalDeCasosInformados': 'Empty',
        'tasa13Informada': 'Empty',
        'tasa10Informada': 'Empty',
        'tasa35Informada': 'Empty',
        'montoPagadoPascuaInformado': 'Empty',
        'prestamosTasa02020a2021Informado': 'Empty',
        'montoTotalHonorariosSinActualizar': 'Empty',
        'totalDeCasosCalculados': 'Empty',
        'tasa13Calculada': 'Empty',
        'tasa10Calculada': 'Empty',
        'tasa35Calculada': 'Empty',
        'montoPagadoPascuaCalculado': 'Empty',
        'prestamosTasa02020a2021Calculado': 'Empty'
    }

    try:
        xpaths = [
            '//*[@id="anuales"]/div[3]/table/tbody/tr[1]/td[3]/a/span',
            '//*[@id="anuales"]/div[3]/table/tbody/tr[2]/td[3]/a/span',
            '//*[@id="anuales"]/div[3]/table/tbody/tr[3]/td[3]/a/span',
            '//*[@id="anuales"]/div[3]/table/tbody/tr[4]/td[3]/a/span'
        ]
        
        for xpath in xpaths:
            try:
                print("first searching")
                element = driver.find_element(By.XPATH, xpath)
                wait.until(lambda driver: len(element.text.strip()) > 0)
                element.click()
                time.sleep(1)
                break
            except NoSuchElementException:
                continue  
            except TimeoutException:
                print("Timeout: Element is empty")
                raise
        
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="detail-1879"]/div[2]/div[2]/div[2]/div[2]/a[3]')))                
        try:
            detalle_codigo1879 = driver.find_element(By.XPATH, '//*[@id="detail-1879"]/div[2]/div[2]/div[2]/div[2]/a[3]')                    
            detalle_codigo1879.click()
        
        except NoSuchElementException:
            print("error en detalle codigo1879 ")
            raise
       
        
        xpaths1 = {
            'codigo': '/html/body/div[6]/div/div/div/div[1]/div/h5/span',
            'totalDeCasosInformados': '/html/body/div[6]/div/div/div/div[2]/div[4]/div[1]/table/tbody/tr[6]/td[1]',
            'tasa13Informada': '/html/body/div[6]/div/div/div/div[2]/div[4]/div[1]/table/tbody/tr[6]/td[2]',
            'tasa10Informada': '/html/body/div[6]/div/div/div/div[2]/div[4]/div[1]/table/tbody/tr[6]/td[3]',
            'tasa35Informada': '/html/body/div[6]/div/div/div/div[2]/div[4]/div[1]/table/tbody/tr[6]/td[4]',
            'montoPagadoPascuaInformado': '/html/body/div[6]/div/div/div/div[2]/div[4]/div[1]/table/tbody/tr[6]/td[5]',
            'prestamosTasa02020a2021Informado': '/html/body/div[6]/div/div/div/div[2]/div[4]/div[1]/table/tbody/tr[6]/td[6]',
            'montoTotalHonorariosSinActualizar': '/html/body/div[6]/div/div/div/div[2]/div[4]/div[1]/table/tbody/tr[6]/td[7]',
            'totalDeCasosCalculados': '/html/body/div[6]/div/div/div/div[2]/div[4]/div[1]/table/tbody/tr[6]/td[8]',
            'tasa13Calculada': '/html/body/div[6]/div/div/div/div[2]/div[4]/div[1]/table/tbody/tr[6]/td[9]',
            'tasa10Calculada': '/html/body/div[6]/div/div/div/div[2]/div[4]/div[1]/table/tbody/tr[6]/td[10]',
            'tasa35Calculada': '/html/body/div[6]/div/div/div/div[2]/div[4]/div[1]/table/tbody/tr[6]/td[11]',
            'montoPagadoPascuaCalculado': '/html/body/div[6]/div/div/div/div[2]/div[4]/div[1]/table/tbody/tr[6]/td[12]',
            'prestamosTasa02020a2021Calculado': '/html/body/div[6]/div/div/div/div[2]/div[4]/div[1]/table/tbody/tr[6]/td[13]'
        }
        
        for key, xpath in xpaths1.items():
            try:
                element = driver.find_element(By.XPATH, xpath)
                resultados[key] = element.text
                print(key + ':', resultados[key])
            except NoSuchElementException:
                resultados[key] = 'Empty'
                print(key + ':', 'Empty')
            time.sleep(1)

    except Exception as e:
        print(e)
                
    driver.quit()    
    return resultados
