# CordinationPython
It is a program focused on coordinating a blockchain (Blockchain) in a simple way.

To decide who to send the information to, it is necessary to have 3 components:

* Origin: Address where the information comes from
* Operation: Operation to be requested
* Data: Data to be passed to destination

```
    parameters ={
        "origen":"origen de los datos",
        "operacion":"operacion que se desea solicitar",
        "datos":"datos que se pasaran al destino"
    }
    
```
Public link: http://142.44.246.23/coordinator


For this software, the Coordinating Component will be managed, 
who is in charge of receiving and sending the information to whom it may concern, 
given the case that more components are willing to speak with this software.

 ```
from flask import Flask, jsonify,request
from pip._vendor import requests
```

Flask is a framework for making web pages and its interpretations are given in json language. 
At the moment they are the libraries that are going to be imported.

```
@app.route("/")
def hola_mundo ():
    return jsonify({"hola":"mundo"})
```
At the same time, there is a method to generate a waiting state, 
to the requests sent by the external components, and at the same time they must send the information that is sent to them.


```

@app.route("/coordinator",methods = ['GET','POST'])
def recepcion(): 
        parametros = request.get_json()
        print (parametros)
        #content = request.get_json(silent=True)
```

In other words, every component must send an Object with this type of parameters as well as the one that sends them.

```
        
        if(parametros["origen"] == "wallet"):
            if parametros["operacion"] == "registrartransaccion":
                r = requests.post('http://localhost:8081/register',json=parametros["datos"])
                return jsonify({"mensaje":"datos enviados al register"},{"mensaje" : "Peticion recibida","peticion":parametros})

            elif parametros["operacion"] == "consultarfondos":
                return jsonify({"mensaje":"datos enviados a blockchain"},{"mensaje" : "Peticion recibida","peticion":parametros})

            else:
                return jsonify({"error":"la funcion que ingreso es erronea"},{"mensaje" : "Peticion recibida","peticion":parametros})

        elif (parametros["origen"] == "register"):
            if parametros["operacion"] == "registrartransaccion":
                return jsonify({"mensaje":"datos enviados a blockchain"},{"mensaje" : "Peticion recibida","peticion":parametros})

            else:
                 return jsonify({"error":"la funcion que ingreso es erronea"},{"mensaje" : "Peticion recibida","peticion":parametros})

        elif (parametros["origen"] == "opencloser"):
            if parametros["operacion"] == "solicitrdatabloque":
                return jsonify({"mensaje":"datos enviados a blockchain"},{"mensaje" : "Peticion recibida","peticion":parametros})
            
            elif parametros["operacion"] == "cerrarbloque":
                return jsonify({"mensaje":"datos enviados a blockchain"},{"mensaje" : "Peticion recibida","peticion":parametros}) 

        elif (parametros["origen"] == "blockchain"):
            if parametros["operacion"] == "cerrarbloque":
                return jsonify({"mensaje":"datos enviados a opencloser"},{"mensaje" : "Peticion recibida","peticion":parametros})
            
            else:
                return jsonify({"error":"la funcion que ingreso es erronea"},{"mensaje" : "Peticion recibida","peticion":parametros})
```

When finished, a Main is created to run the file.

```

if __name__ == '__main__':
    app.run(host='localhost',debug = True ,port=5596)
 
```
Imagenes:

![Alt text](https://github.com/JohanStivenMartinez/CordinationPython/blob/master/assets/imagex.jpg "Ejemplo de petición y respuesta")

![Alt text](https://github.com/JohanStivenMartinez/CordinationPython/blob/master/assets/image5.jpg "Ejemplo de respuesta")

![Alt text](https://github.com/JohanStivenMartinez/CordinationPython/blob/master/assets/image3.jpg "Respuesta Erronea")


END!!!!!!!!!!!
