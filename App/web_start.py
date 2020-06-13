from flask import Flask, jsonify, make_response, render_template, request
import datetime
import jwt
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
    return jsonify({'mesagge' : 'Home'})

@app.route('/check', methods=['GET'])
def check():
    return jsonify({'mesagge' : 'Working web server :)'})

@app.route('/login',methods=['GET'])
def login():
    return render_template('login.html')

@app.route('/donor', methods=['GET'])
def donor():
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
#     return jsonify({"Holla:" : "Bienveindo"})

@app.route('/login',methods=['POST'])
def authentiaction():
    if request.method == "POST":
        user = request.form.get('usuario')
        passw = request.form.get('password')
        print(user)
        print(passw)
        # auth = request.authorization
        if user and passw == 'password':
            token = jwt.encode({'user' : user , 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
            return jsonify({'token' : token.decode('UTF-8')})
        else:
            return render_template('login.html')
    return make_response('Unverified customer', 401, {'WWW_authentiaction' : 'Login required'})




if __name__ == '__main__':
# app.run(port = 3000, debug = True) UNA MANERA MAS DE ESTABLECER UN PUERTO ESPECIFICO
    app.run(debug=True)  # para que al hacer cambio se actualice la pag solo
