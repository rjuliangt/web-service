from flask import Flask, jsonify, request, make_response, render_template
import datetime
import jwt
# from configure import key
from functools import wraps
# Nombramos a nuestra apliacion como app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'key1234'

# ************ FUNCION PARA VERIDICAR ELTOKEN ********************
# ****************************************************************
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')

        if not token:
            return jsonify({'mesagge' : 'Token is missing!!'}), 403

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return jsonify({'message' : 'Token is missing or invalid'}), 403
        return f(*args, **kwargs)

# CREACION DE RUTAS DEL WEB SERVICES
# ************** METODOS "GET" ******************************
# ***********************************************************
@app.route('/', methods=['GET'])
def home():
    return jsonify({"Hola" : "Bienveindo"})
    # return render_template('donor.html')

@app.route('/authentication', methods=['GET'])
def authentication():
    auth = request.authorization
    if auth and auth.password == 'password':
        token = jwt.encode({'user' : auth.username, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECTRET_KEY'])
        return jsonify({'token' : token.decode('UTF-8')})

    return make_response('Unverified customer', 401, {'WWW_authentiaction' : 'Login required'})

@app.route('/add_donor', methods=['GET'])
def add_donor():
    return render_template('donor.html')

@app.route('/unprotected')
def unprotected():
    return jsonify({'mesagge' : 'Anoye can view this!'})

@app.route('/protected')
def protected():
    return jsonify({'mesagge' : 'This is only avaliable for people with valid tokens!'})
# ***************************************************************
# ************************* Metodos "POST" **********************
# @app.route('/add_donor', methods=['POST'])
# def add_donor():
#     return jsonify({"Holla:","Bienveindo"})





if __name__ == '__main__':
# app.run(port = 3000, debug = True) UNA MANERA MAS DE ESTABLECER UN PUERTO ESPECIFICO
    app.run(debug=True)  # para que al hacer cambio se actualice la pag solo
