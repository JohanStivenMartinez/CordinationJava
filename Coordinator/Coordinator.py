from flask import Flask, jsonify,request
from pip._vendor import requests

app = Flask(__name__)
#
#metodo de prueba
@app.route("/")
def hola_mundo ():
    return jsonify({"hola":"mundo"})
#http://142.244.44.246/coordinator
#se crea el metodo que reenvia los datos y se le asigna la ruta /coordinator
@app.route("/coordinator",methods = ['GET','POST'])
def recepcion(): 
        parametros = request.get_json()
        print (parametros)
        #content = request.get_json(silent=True)
        if(parametros["origen"] == "wallet"):
            if parametros["operacion"] == "registrartransaccion":
                r = requests.post('http://localhost:8081/register',json=parametros["datos"])
                return jsonify({"mensaje":"datos enviados al register"},{"mensaje" : "Peticion recibida","peticion":parametros})

            elif parametros["operacion"] == "consultarfondos":
                r = requests.post('url/blockchain',json=parametros["datos"])
                return jsonify({"mensaje":"datos enviados a blockchain"},{"mensaje" : "Peticion recibida","peticion":parametros})

            else:
                return jsonify({"error":"la funcion que ingreso es erronea"},{"mensaje" : "Peticion recibida","peticion":parametros})

        elif (parametros["origen"] == "register"):
            if parametros["operacion"] == "registrartransaccion":
                r = requests.post('url/blockchain',json=parametros["datos"])
                return jsonify({"mensaje":"datos enviados a blockchain"},{"mensaje" : "Peticion recibida","peticion":parametros})

            else:
                 return jsonify({"error":"la funcion que ingreso es erronea"},{"mensaje" : "Peticion recibida","peticion":parametros})

        elif (parametros["origen"] == "opencloser"):
            if parametros["operacion"] == "solicitrdatabloque":
                r = requests.post('url/blockchain',json=parametros["datos"])
                return jsonify({"mensaje":"datos enviados a blockchain"},{"mensaje" : "Peticion recibida","peticion":parametros})
            
            elif parametros["operacion"] == "cerrarbloque":
                r = requests.post('url/blockchain',json=parametros["datos"])
                return jsonify({"mensaje":"datos enviados a blockchain"},{"mensaje" : "Peticion recibida","peticion":parametros}) 
            
            else:
                 return jsonify({"error":"la funcion que ingreso es erronea"},{"mensaje" : "Peticion recibida","peticion":parametros})

        elif (parametros["origen"] == "blockchain"):
            if parametros["operacion"] == "cerrarbloque":
                r = requests.post('url/opencloser',json=parametros["datos"])
                return jsonify({"mensaje":"datos enviados a opencloser"},{"mensaje" : "Peticion recibida","peticion":parametros})
            
            else:
                return jsonify({"error":"la funcion que ingreso es erronea"},{"mensaje" : "Peticion recibida","peticion":parametros})
        
        else:
            return jsonify({"error":"El origen ingresado es erroneo"})

#
#
#se crea el main y se inicia el servidor en el puerto 5596
if __name__ == '__main__':
    app.run(host='localhost',debug = True ,port=5596)
    
