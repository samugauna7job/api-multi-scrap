from flask import render_template, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required
import bcrypt
import mysql.connector
from src.db.db_config import mycursor, mydb, logger

def verify_password(input_password, hashed_password):
    return bcrypt.checkpw(input_password.encode('utf-8'), hashed_password.encode('utf-8'))

def check_credentials(username, password):
    try:
        consultQuery= "SELECT pass_hash FROM users WHERE name_user =%s"
        mycursor.execute(consultQuery, (username,))
        result= mycursor.fetchone()
        if result:
            pass_hash= result[0]
            if verify_password(password, pass_hash):
                return True
        return False
    except mysql.connector.Error as err:
        logger.error("error al verificar las credenciales", err)
        return False
    
def login_route():
    print("Entrando a login_route()")
    if request.method == 'POST':
        username = request.form.get("usuario")
        password = request.form.get("contrasena")
        print("Usuario:", username)
        print("Contraseña:", password)
        if not username or not password:
            return jsonify({"error": "Falta el usuario o contraseña"}), 400
        # Verificamos las credenciales del usuario
        if check_credentials(username, password):
            # Si las credenciales son válidas, se crea un token de acceso
            access_token = create_access_token(identity=username)
            return render_template('home.html')
        else:
            #Si las credenciales son incorrectas
            error_message = "Credenciales incorrectas. Intente de nuevo."
            return render_template('index.html', error_message=error_message)
    return render_template('index.html')