# flask-firestore

## Requerimientos:

  - instalar pyrbase4:
  ```
    pip install pyrebase4
  ```
  - instalar flask
  ```
    pip install flask
  ```
  - crear base de datos en firebase
  
 
### Creacion y configuracion de firebase:

1. Seleccionar el servicio realtime database, y crearlo.
  
2. Seleccionar la opcion configuracion del proyecto.

3. Seleccionar la opcion aplicacion web, registrarlo y copiar el CDN
   (solo el objeto firebaseconfig), y copiarlo en el proyecto pero modificandolo
    para que sea un diccionario en python.


### Inicializacion de la base de datos en python

  ```python
    import pyrebase
    
    firebaseConfig = {
      "apiKey":"",
      "authDomain":"",
      "databaseURL":"",
      "projectId":"",
      "storageBucket":"",
      "messagingSenderId":"",
      "appId":""
    }
    
    #Inicializacion:
    firebase = pyrebase.initiliaze_app(firebaseConfig)
    db = firebase.database()
  ```
  
