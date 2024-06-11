import mysql.connector
import logging

logging.basicConfig(level=logging.INFO)
logger= logging.getLogger(__name__)

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="*",
        database="usersapi"
        )
    mycursor= mydb.cursor()
    logger.info("db OK")
except mysql.connector.Error as err:
    logger.error("db not ok :c", err)
