import bcrypt
from src.db.db_config import mycursor, mydb, logger

# Función para crear un nuevo usuario
def create_user(username, password):
    # Hashear la contraseña con bcrypt
    hashed_password= bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    # Insertar el usuario en la base de datos
    sqlCommandAdd= "INSERT INTO users (name_user, pass_hash) VALUES (%s, %s)"
    val = (username, hashed_password)
    mycursor.execute(sqlCommandAdd, val)
    mydb.commit()
    logger.info("user creado correctamente")
