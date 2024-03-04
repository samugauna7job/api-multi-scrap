from flask import jsonify, request
from driver.selenium_config import getDriver
from src.login.login_sii import login_sii
from src.res_hon.resumenHonorarios import getResumenHonorarios


# Definir una ruta para el inicio de sesión seguido por el resumen de honorarios
def login_and_resumenHonarios():
    driver=getDriver()
    # Obtener los datos del cuerpo de la solicitud
    data = request.json
    rut = data.get("rut")
    clave = data.get("clave")
    # Verificar si se proporcionaron los datos necesarios
    if not rut or not clave:
        return jsonify({"message": "Faltan datos: se requiere rut y clave"}), 400
    # Iniciar sesión
    login_result = login_sii(driver, rut, clave)
    # Si el inicio de sesión fue exitoso, obtener el resumen de honorarios
    if login_result:
        resumen_result = getResumenHonorarios(rut, clave, driver)
        return jsonify(resumen_result)
    else:
        return jsonify({"message": "Inicio de sesión fallido"}), 401