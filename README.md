# API V2 Flask

BackEnd  en Flask Python 3.7


# BackEndBase
Sistema base para el desarrollo de Back-End's usando Python preferiblemente la version 3.7.6(codename: **Lilith**)


# Descripción
Este sistema, describe el uso y puesta a punto de una **Api rest** usando [**Python**](https://www.python.org/downloads/) y [**Flask**](http://flask.pocoo.org/)

![flask](http://flask.pocoo.org/static/badges/powered-by-flask-s.png)


## Documentación
Puedes encontrar la documentación completa en el [sitio web del proyecto.](http://docs.awesome-backend.appspot.com/)


# Requisitos
- [**Python**](https://www.python.org/downloads/) 3.7.x
- [**virtualenv**](https://virtualenv.pypa.io/en/stable/) (Recomendado)


## Instalación de este repositorio
Clonar este repositorio y alojarlo en una carpeta conveniente.

    git clone https://github.com/georgus/infoIp.git

Se recomienda usar [**virtualenv**](https://virtualenv.pypa.io/en/stable/) para desarrollo y pruebas.


## Activar virtualenv en entornos Gnu/Linux, Mac OS

```sh
$ virtualenv --python python3 env
$ source env/bin/activate
```


## Instalar las dependencias
Una vez dentro del entorno, instalar las dependencias:

```sh
(env) $ pip install -r requirements.txt
(env) $ pip install python-whois
(env) $ python -m pip install socket
(env) $ pip install urllib
(env) $ pip install bs4
(env) $ pip install binascii
```

# Uso de Firestore en modo local (opcional)
Si se esta usando [**FireStore**](https://firebase.google.com/docs/) como base de datos, se puede usar en modo local, definiendo una variable de entorno en el S.O., que tenga la ruta de una [cuenta de servicio](https://cloud.google.com/docs/authentication/getting-started).

```
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/service-account.json"
```


tambien es posible hacer uso del archivo **.flaskenv**, ubicado en la raiz del proyecto y fijar la variable de entorno, mencionada arriba:

```.flaskenv
GOOGLE_APPLICATION_CREDENTIALS=/path/to/service-account.json
```


# Iniciando el servidor web
A continuación se describen algunas configuraciones para iniciar el servidor web.


## Usando python

```sh
(env) $ python main.py
```

> El folder **Test** se utiliza para archivos de pruebas y adicionalmente el folder **.gcloud** si se usa [Google Cloud Platform.](https://cloud.google.com/)
>>>>>>> Inicio de proyecto, estructura en Flask con python 37
