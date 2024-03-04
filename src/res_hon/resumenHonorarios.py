from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

def getResumenHonorarios(rut, clave, driver):
    resultados= {}
    time.sleep(1)
    print("este usuario se esta ejecutando")
    print(rut, clave)
    #IR A BOLETAS DE ELECTRONICAS EMITIDAS
    wait=WebDriverWait(driver,15)
    driver.get("https://zeus.sii.cl/cvc_cgi/bte/bte_indiv_cons?1")
    selectYear=wait.until(EC.presence_of_element_located((By.ID, 'ANOA')))
    selectYear.click()
    selectYear2023=wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="ANOA"]/option[2]')))
    selectYear2023.click()
    buttonConsultar=wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/center[2]/form/table/tbody/tr[2]/td[3]/font/input[1]')))
    buttonConsultar.click()
    try:
        textCap=wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/center[2]/font')))
        texto_capturado = textCap.text
        texto_nohay_mov2023 = "NO REGISTRA MOVIMIENTOS PARA LA FECHA SEÑALADA"
        if textCap.is_displayed():
            resultados["2023-BOL-ELEC-EMITIDAS"] = "No registra movimientos"
            driver.get("https://loa.sii.cl/cgi_IMT/TMBCOC_MenuConsultasContribRec.cgi?dummy=1461943244650")
            selectYear=wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/center/table[3]/tbody/tr[2]/td[2]/div/font/select')))
            selectYear.click()
            selectYear2023=wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/center/table[3]/tbody/tr[2]/td[2]/div/font/select/option[26]')))
            selectYear2023.click()
            buttonConsultar=wait.until(EC.presence_of_element_located((By.ID, 'cmdconsultar124')))
            buttonConsultar.click()
            table = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/center/table[2]/tbody/tr[6]/td/table')))
            if table.is_displayed():
                elementos = {
                '2023-BOL-ELEC-RECIBIDAS-EMISIONES-VIGENTES': '/html/body/div[3]/center/table[2]/tbody/tr[6]/td/table/tbody/tr[15]/td[2]',
                '2023-BOL-ELEC-RECIBIDAS-HONORARIOS-BRUTOS': '/html/body/div[3]/center/table[2]/tbody/tr[6]/td/table/tbody/tr[15]/td[4]',
                '2023-BOL-ELEC-RECIBIDAS-RETENCIONES-DE-TERCEROS': '/html/body/div[3]/center/table[2]/tbody/tr[6]/td/table/tbody/tr[15]/td[5]',
                '2023-BOL-ELEC-RECIBIDAS-RETENCION-CONTRIBUYENTE': '/html/body/div[3]/center/table[2]/tbody/tr[6]/td/table/tbody/tr[15]/td[6]',
                '2023-BOL-ELEC-RECIBIDAS-TOTAL-LIQUIDO': '/html/body/div[3]/center/table[2]/tbody/tr[6]/td/table/tbody/tr[15]/td[7]',
            }
                default_value = "sin datos"
                # Recorrer los elementos y recuperar los datos
                for nombre, xpath_elemento in elementos.items():
                    try:
                        elemento = driver.find_element(By.XPATH, xpath_elemento).text
                        resultados[nombre] = elemento if elemento else default_value
                    except NoSuchElementException:
                        print("no hay nada")
            else:
                print("gola")
    except TimeoutException:
        pass
    try:
        table = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/center[2]/form[1]')))
        if table.is_displayed():
            # Datos a recuperar
            elementos = {
                '2023-BOL-ELEC-EMITIDAS-BOLETAS-VIGENTES': '/html/body/center[2]/form[1]/table/tbody/tr[15]/td[4]',
                '2023-BOL-ELEC-EMITIDAS-HONORARIOS-BRUTOS': '/html/body/center[2]/form[1]/table/tbody/tr[15]/td[6]',
                '2023-BOL-ELEC-EMITIDAS-RETENCIONES': '/html/body/center[2]/form[1]/table/tbody/tr[15]/td[7]',
                '2023-BOL-ELEC-EMITIDAS-TOTAL-LIQUIDO': '/html/body/center[2]/form[1]/table/tbody/tr[15]/td[8]',
            }
            # Valor predeterminado para datos vacíos
            default_value = "sin datos"
            # Recorrer los elementos y recuperar los datos
            for nombre, xpath_elemento in elementos.items():
                try:
                    elemento = driver.find_element(By.XPATH, xpath_elemento).text
                    resultados[nombre] = elemento if elemento else default_value
                except NoSuchElementException:
                    print("no hay nada")
            # Mostrar los datos
        print("BOLETA ELECTRONICAS EMITIDAS PROCESO TERMINADO")
        driver.get("https://loa.sii.cl/cgi_IMT/TMBCOC_MenuConsultasContribRec.cgi?dummy=1461943244650")
        selectYear=wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/center/table[3]/tbody/tr[2]/td[2]/div/font/select')))
        selectYear.click()
        selectYear2023=wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/center/table[3]/tbody/tr[2]/td[2]/div/font/select/option[26]')))
        selectYear2023.click()
        buttonConsultar=wait.until(EC.presence_of_element_located((By.ID, 'cmdconsultar124')))
        buttonConsultar.click()
        table = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/center/table[2]/tbody/tr[6]/td/table')))
        if table.is_displayed():
            elementos = {
            '2023-BOL-ELEC-RECIBIDAS-EMISIONES-VIGENTES': '/html/body/div[3]/center/table[2]/tbody/tr[6]/td/table/tbody/tr[15]/td[2]',
            '2023-BOL-ELEC-RECIBIDAS-HONORARIOS-BRUTOS': '/html/body/div[3]/center/table[2]/tbody/tr[6]/td/table/tbody/tr[15]/td[4]',
            '2023-BOL-ELEC-RECIBIDAS-RETENCIONES-DE-TERCEROS': '/html/body/div[3]/center/table[2]/tbody/tr[6]/td/table/tbody/tr[15]/td[5]',
            '2023-BOL-ELEC-RECIBIDAS-RETENCION-CONTRIBUYENTE': '/html/body/div[3]/center/table[2]/tbody/tr[6]/td/table/tbody/tr[15]/td[6]',
            '2023-BOL-ELEC-RECIBIDAS-TOTAL-LIQUIDO': '/html/body/div[3]/center/table[2]/tbody/tr[6]/td/table/tbody/tr[15]/td[7]',
        }
            default_value = "sin datos"
            # Recorrer los elementos y recuperar los datos
            for nombre, xpath_elemento in elementos.items():
                try:
                    elemento = driver.find_element(By.XPATH, xpath_elemento).text
                    resultados[nombre] = elemento if elemento else default_value
                except NoSuchElementException:
                    print("no hay nada")
            # Mostrar los datos
            print("BOLETA ELECTRONICAS RECIBIDAS PROCESO TERMINADO")
        else:
            print("gola")
    except TimeoutException: 
        pass
    driver.quit()
    return resultados
    