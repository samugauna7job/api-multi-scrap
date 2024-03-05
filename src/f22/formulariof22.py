from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time



def getf22(driver, rut, clave):
    resultados= {}
    print("este usuario se esta ejecutando")
    print(rut, clave)
    #busqueda facturas de consulta seguimiento
    wait=WebDriverWait(driver,15)
    driver.get("https://www4.sii.cl/consultaestadof22ui/#!/default")
    buttonConsultar=wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="formulario-periodo"]/div/div[2]/div/button')))
    buttonConsultar.click()
    time.sleep(2)
    year2023DoesntExist=wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="SituacionActual"]/div/div/div[2]/p')))
    texto_capturado = year2023DoesntExist.text
    texto_nohay2023 = "Actualmente no cuentas con una Declaración de Renta para el periodo tributario 2023. A continuación te dejamos las opciones de realizar una declaración de renta para este periodo o buscar por folio si ya realizaste alguna."
    if texto_nohay2023 in texto_capturado:
        try:
            driver.get('https://www4.sii.cl/consultaestadof22ui/#!/default')
            selectYear=wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="formulario-periodo"]/div/div[2]/div/select')))
            selectYear.click()
            select2022=wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="formulario-periodo"]/div/div[2]/div/select/option[2]')))
            select2022.click()
            buttonConsultar=wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="formulario-periodo"]/div/div[2]/div/button')))
            buttonConsultar.click()
            time.sleep(2)
            buttonformulariof22= wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="my-wrapper"]/div[3]/div/div/div/div/div[2]/div[2]/div/table/tbody/tr[1]/td[3]/a')))     
            buttonformulariof22.click()
            time.sleep(2)
            formulario = wait.until(EC.presence_of_element_located((By.ID, 'formulario')))
            if formulario.is_displayed():
            # Datos a recuperar
                elementos = {
                    '2022-20-IDPC-de-empresas-acogidas-al-regimen-Pro-Pyme': '20',
                    '2022-1450-Perdida-Tributaria-del-ejercicio-al-31-dic': '1450',
                    '2022-1454-Remanente-ejercicio-anterior-o-saldo-inicial-(saldo-positivo)': '1454',
                    '2022-1494-Capital-aportado-histórico-(incluye-aumentos-y-disminuciones-efectivas)': '1494',
                    '2022-1545-CPTS-Positivo-Final': '1545',
                    '2022-1546-CPTS-Negativo-Final': '1546',
                    '2022-1564-Remanente-ejercicio-siguiente-(saldo-positivo)': '1564'
                }
                # Valor predeterminado para datos vacíos
                default_value = "sin datos"
                # Recorrer los elementos y recuperar los datos
                for nombre, id_elemento in elementos.items():
                    try:
                        elemento = driver.find_element(By.ID, id_elemento).text
                        resultados[nombre] = elemento if elemento else default_value
                    except NoSuchElementException:
                        print("no hay nada")
        except:
            pass
    else:
        try:
            buttonformulariof22= wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="my-wrapper"]/div[3]/div/div/div/div/div[2]/div[2]/div/table/tbody/tr[1]/td[3]/a')))     
            buttonformulariof22.click()
            formulario = wait.until(EC.presence_of_element_located((By.ID, 'formulario')))
            if formulario.is_displayed():
                # Datos a recuperar
                elementos = {
                    '2023-20-IDPC-de-empresas-acogidas-al-regimen-Pro-Pyme': '20',
                    '2023-1450-Perdida-Tributaria-del-ejercicio-al-31-dic': '1450',
                    '2023-1454-Remanente-ejercicio-anterior-o-saldo-inicial-(saldo-positivo)': '1454',
                    '2023-1494-Capital-aportado-histórico-(incluye-aumentos-y-disminuciones-efectivas)': '1494',
                    '2023-1545-CPTS-Positivo-Final': '1545',
                    '2023-1546-CPTS-Negativo-Final': '1546',
                    '2023-1564-Remanente-ejercicio-siguiente-(saldo-positivo)': '1564'
                }
                # Valor predeterminado para datos vacíos
                default_value = "sin datos"
                # Recorrer los elementos y recuperar los datos
                for nombre, id_elemento in elementos.items():
                    try:
                        elemento = driver.find_element(By.ID, id_elemento).text
                        resultados[nombre] = elemento if elemento else default_value
                    except NoSuchElementException:
                        print("no hay nada")
        except TimeoutException: 
            pass
    driver.quit()
    return resultados