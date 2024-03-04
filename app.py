from flask import Flask, request, jsonify
#from src.sii_scrapper import login_sii, getData
from src.routes.routes import login_and_resumenHonarios
app = Flask(__name__)





# Rutas
@app.route('/resumen-honorarios', methods=['POST'])
def login_and_resumen_hon_route():
    return login_and_resumenHonarios()





if __name__ == "__main__":
    app.run(debug=True)