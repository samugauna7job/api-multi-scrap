from flask import Flask, request, jsonify
#from src.sii_scrapper import login_sii, getData
from src.routes.routes import login_and_resumenHonarios, login_and_f22, login_and_f29, login_and_ddjj1879
app = Flask(__name__)





# Rutas
@app.route('/resumen-honorarios', methods=['POST'])
def login_and_resumen_hon_route():
    return login_and_resumenHonarios()

@app.route('/f22', methods=['POST'])
def login_and_f_22():
    return login_and_f22()

@app.route('/f29', methods=['POST'])
def login_and_f_29():
    return login_and_f29()


@app.route('/ddjj1879', methods=['POST'])
def login_and_ddjj_1879():
    return login_and_ddjj1879()






if __name__ == "__main__":
    app.run(debug=True)