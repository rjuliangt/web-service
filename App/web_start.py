from flask import Flask, jsonify, request, make_response, render_template
import jwt


# Nombramos a nuestra apliacion como app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'KEY'
# CREACION DE RUTAS DEL WEB SERVICES
# METODOS "GET"

@app.route('/', methods=['GET'])
def home():
    return jsonify({"Hola:","Bienveindo"})
    # return render_template('donor.html')

@app.route('/authentication', methods=['GET'])
def authentication():
    return jsonify({"Holla:","Bienveindo"})

@app.route('/add_donor', methods=['GET'])
def add_donor():
    return render_template('donor.html')

# METODOS "POST"
@app.route('/add_donor', methods=['POST'])
def add_donor():
    return jsonify({"Holla:","Bienveindo"})

@app.route('/', methods=['GET'])
def home():
    return jsonify({"Holla:","Bienveindo"})


if __name__ == '__main__':
# app.run(port = 3000, debug = True) UNA MANERA MAS DE ESTABLECER UN PUERTO ESPECIFICO
app.run(debug=True)  # para que al hacer cambio se actualice la pag solo
