from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time


def login_sii (driver,rut,clave):
        
        try:
            driver.get("https://zeusr.sii.cl//AUT2000/InicioAutenticacion/IngresoRutClave.html?https://misiir.sii.cl/cgi_misii/siihome.cgi")
            ruter_input =  driver.find_element(By.ID, "rutcntr")
            ruter_input.send_keys(rut)
            pass_input = driver.find_element(By.ID, "clave")
            pass_input.send_keys(clave)
            btn_ingreso = driver.find_element(By.ID, "bt_ingresar")
            btn_ingreso.click()
            time.sleep(2)
            
            try:
                alert = driver.switch_to.alert
                alert.dismiss()
            except:
                pass
            
            try:
                alert = driver.switch_to.alert
                alert.dismiss()
            except:
                pass
            
            try:
                driver.find_element(By.ID, "titulo")
                print("no se pudo hacer login")
                return False
            except NoSuchElementException:
                print('login exitosos')
                #aca analizo si esta la pantalla de siguiente"
                try:
                    try:
                        modal = driver.find_element(By.CSS_SELECTOR, 'div.modal-dialog')
                        if modal:
                            # Si hay un modal, hacer clic en el botón de cierre
                            btn_cierre_modal = driver.find_element(By.XPATH, '//*[@id="ModalEmergente"]/div/div/div[3]/button')
                            btn_cierre_modal.click()
                    except:
                        pass
                    time.sleep(2)
                    try:
                        modal = driver.find_element(By.ID,'myMainCorreoVigente')
                        if modal.is_displayed():
                            driver.execute_script("arguments[0].style.display = 'none';", modal)
                    except:
                        pass
                except NoSuchElementException:
                    boton_siguiente = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/p[2]/a[1]')
                    boton_siguiente.click()
                    try:
                        try:
                            alert = driver.switch_to.alert
                            alert.dismiss()
                        except:
                            pass
                        try:
                            alert = driver.switch_to.alert
                            alert.dismiss()
                        except:
                            pass
                        try:
                            modal = driver.find_element(By.CSS_SELECTOR, 'div.modal-dialog')
                            if modal:
                                # Si hay un modal, hacer clic en el botón de cierre
                                btn_cierre_modal = driver.find_element(By.XPATH, '//*[@id="ModalEmergente"]/div/div/div[3]/button')
                                btn_cierre_modal.click()
                        except:
                            pass
                        time.sleep(2)
                        try:
                            modal = driver.find_element(By.ID,'myMainCorreoVigente')
                            if modal.is_displayed():
                                driver.execute_script("arguments[0].style.display = 'none';", modal)
                        except:
                            pass
                    except NoSuchElementException:
                        print('keseste erroooor!!')
                return True
        except TimeoutException as timeout_error:
            print(f"Error de tiempo de espera para RUT {rut}: {timeout_error}")
        except Exception as e:
            print(f"Error durante el proceso para RUT {rut}: {e}")
