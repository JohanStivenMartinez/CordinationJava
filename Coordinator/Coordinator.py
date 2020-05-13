#It is a program focused on coordinating a blockchain (Blockchain) in a simple way.

"""For this software, the Coordinating Component will be managed, 
who is in charge of receiving and sending the information to whom it may concern, 
given the case that more components are willing to speak with this software. """

from flask import Flask, jsonify,request
from pip._vendor import requests

app = Flask(__name__)

url_register='http://register.local/recibirData.php'
url_blockchain='http://127.0.0.1:5000/new_transactions'
url_wallet1='http://142.44.246.66:4000/wallet_1'
url_wallet2=' http://142.44.246.66/Registro'
url_wallet3='https://wallet220200504202955.azurewebsites.net/'
url_opencloser=''

@app.route("/")
def hola_mundo ():
    return jsonify({"hola":"mundo"})


@app.route("/coordinator",methods = ['GET','POST'])
def recepcion(): 
    try:
        parametros = request.get_json()
        print (parametros)
        
        #In other words, every component must send an Object with this type of parameters as well as the one that sends them.
        if(parametros["origen"] == "wallet"):
            if parametros["operacion"] == "registrartransaccion":
                try:
                    r = requests.post(url_register,json=parametros["datos"])
                    return jsonify({"mensaje":"datos enviados al register"},{"mensaje" : "Peticion recibida","peticion":parametros})
                except:
                    return jsonify({'mensaje':'Error al enviar los datos'})
            
            elif parametros["operacion"] == "consultarfondos":
                try:
                    r = requests.post(url_blockchain,json=parametros["datos"])
                    return jsonify({"mensaje":"datos enviados a blockchain"},{"mensaje" : "Peticion recibida","peticion":parametros})
                except:
                    return jsonify({'mensaje':'Error al enviar los datos'})
                
            else:
                return jsonify({"error":"la funcion que ingreso es erronea"},{"mensaje" : "Peticion recibida","peticion":parametros})

        elif (parametros["origen"] == "register"):
            
            if parametros["operacion"] == "registrartransaccion":
                try:
                    r = requests.post(url_blockchain,json=parametros["datos"])
                    return jsonify({"mensaje":"datos enviados a blockchain"},{"mensaje" : "Peticion recibida","peticion":parametros})
                except:
                    return jsonify({'mensaje':'Error al enviar los datos'})

            else:
                 return jsonify({"error":"la funcion que ingreso es erronea"},{"mensaje" : "Peticion recibida","peticion":parametros})

        elif (parametros["origen"] == "opencloser"):
            if parametros["operacion"] == "solicitardatabloque":
                try:
                    r = requests.post(url_blockchain,json=parametros["datos"])
                    return jsonify({"mensaje":"datos enviados a blockchain"},{"mensaje" : "Peticion recibida","peticion":parametros})
                except:
                    return jsonify({'mensaje':'Error al enviar los datos'})
                
            elif parametros["operacion"] == "cerrarbloque":
                try:
                    r = requests.post(url_blockchain,json=parametros["datos"])
                    return jsonify({"mensaje":"datos enviados a blockchain"},{"mensaje" : "Peticion recibida","peticion":parametros}) 
                except:
                    return jsonify({'mensaje':'Error al enviar los datos'})
                
            else:
                 return jsonify({"error":"la funcion que ingreso es erronea"},{"mensaje" : "Peticion recibida","peticion":parametros})

        elif (parametros["origen"] == "blockchain"):
            if parametros["operacion"] == "cerrarbloque":
                try:
                    r = requests.post(url_opencloser,json=parametros["datos"])
                    return jsonify({"mensaje":"datos enviados a opencloser"},{"mensaje" : "Peticion recibida","peticion":parametros})
                except:
                    return jsonify({'mensaje':'Error al enviar los datos'})
                
            else:
                return jsonify({"error":"la funcion que ingreso es erronea"},{"mensaje" : "Peticion recibida","peticion":parametros})
        
        else:
            return jsonify({"error":"El origen ingresado es erroneo"})

    except :
        return jsonify({"Mensaje":"No se han detectado datos de entrada",
                        "Status":"Servicio en funcionamiento",
                        "Disclaimer":"Se reciben datos formato JSON desde GET y POST"})
        
#
#
#se crea el main y se inicia el servidor en el puerto 5596
if __name__ == '__main__':
    app.run(host='142.44.246.23',debug = True, port=5596 )
    
