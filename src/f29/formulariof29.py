from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
from bs4 import BeautifulSoup


def getf29(driver, rut, clave, mes):
    resultados= {}
    time.sleep(1)
    months_xpaths={
        'enero': '//*[@id="item-form"]/select[2]/option[2]',
        'febrero': '//*[@id="item-form"]/select[2]/option[3]',
        'marzo': '//*[@id="item-form"]/select[2]/option[4]',
        'abril': '//*[@id="item-form"]/select[2]/option[5]',
        'mayo': '//*[@id="item-form"]/select[2]/option[6]',
        'junio': '//*[@id="item-form"]/select[2]/option[7]',
        'julio': '//*[@id="item-form"]/select[2]/option[8]',
        'agosto': '//*[@id="item-form"]/select[2]/option[9]',
        'septiembre': '//*[@id="item-form"]/select[2]/option[10]',
        'octubre': '//*[@id="item-form"]/select[2]/option[11]',
        'noviembre': '//*[@id="item-form"]/select[2]/option[12]',
        'diciembre': '//*[@id="item-form"]/select[2]/option[13]',
    }
    month_xpath = months_xpaths.get(mes.lower()) 
    print("este usuario se esta ejecutando")
    print(rut, clave)
    #IR A BOLETAS DE ELECTRONICAS EMITIDAS
    wait=WebDriverWait(driver,15)
    driver.get("https://www4.sii.cl/rfiInternet/consulta/index.html#rfiSelFormularioPeriodo")
    try:
        # Primer select tipo de formulario
        selectf29=wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="item-form"]/select/option[2]')))
        selectf29.click()
        selectYear=wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="item-form"]/select[1]')))
        selectYear.click()
        # Segundo select año
        select2023=wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="item-form"]/select[1]/option[42]')))
        select2023.click()
        selectYear=wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="item-form"]/select[1]')))
        selectYear.click()
        # Tercer select mes
        selectMonth=wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="item-form"]/select[2]')))
        selectMonth.click()
        # Contiene el xpath del mes
        if month_xpath:
            # Hacer clic en el elemento correspondiente al mes
            month = wait.until(EC.element_to_be_clickable((By.XPATH, month_xpath)))
            month.click()
            mes = month.text
        else:
            # Si no se encuentra un XPath para el mes dado, imprimir un mensaje de error
            print("Error: Mes no válido")
        # button Buscar datos ingresados
        buttonBuscarDatos=wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="item-form"]/table/tbody/tr/td/table/tbody/tr/td/button')))
        buttonBuscarDatos.click()
        wait=WebDriverWait(driver, 5)
        #folio ancor
        try:
            folio=wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/table/tbody/tr/td/table/tbody/tr[7]/td/div/div[2]/table[1]/tbody/tr[4]/td')))
            # wait.until(EC.presence_of_element_located((By.XPATH, '')))
            text_folio=folio.text
            text_NohayFolios= 'No se encontraron Declaraciones'
            if text_NohayFolios in text_folio:
                resultados["Folio"] = "No contiene folios para el mes correspondiente"
        except:
            pass
        try:
            folioClikeable=wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/table/tbody/tr/td/table/tbody/tr[7]/td/div/div[2]/table[1]/tbody/tr[3]/td[1]/div/a')))
            folioClikeable.click()
            wait=WebDriverWait(driver, 10)
            time.sleep(3)
            #button ver datos
            buttonVerDatos=wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr/td/table/tbody/tr[8]/td/table/tbody/tr/td/table/tbody/tr/td[1]/button')))
            buttonVerDatos.click()
            codigos_deseados = ['586', '142', '538', '584', '562', '534', '535', '537', '77', '48', '49', '151', '155', '563', '91']
            formTable = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/table/tbody/tr/td/table/tbody/tr[7]/td/div/div[3]/table/tbody/tr[4]/td[2]')))
            html_text=driver.page_source
            soup=BeautifulSoup(html_text, 'html.parser')
            elementos_td = soup.find_all('td', class_='celda-codigo')
            for elemento in elementos_td:
                codigo = elemento.text.strip()  # Obtiene el texto dentro del elemento <td> y elimina espacios en blanco
                if codigo in codigos_deseados:
                    # Busca el siguiente elemento <td>
                    siguiente_elemento = elemento.find_next_sibling('td')
                    if siguiente_elemento and siguiente_elemento.text.strip():
                        valor = siguiente_elemento.text.strip()
                    else:
                        valor = "---"
                    resultados[codigo] = valor
                    # print(f"Código: {codigo}, Valor: {valor}")
        except:
            pass
    except:
        pass
    driver.quit()
    return resultados