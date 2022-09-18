Challenge T-MOB
====================
Repositorio para evaluación de la empresa T-MOB.

En la carpeta docker se encuentra el proyecto dockerizado.
En la carpeta challenge_redirect se encuentra el proyecto sin dockerizar.

Requirements
============

- Python (3.5, 3.6, 3.7, 3.8, 3.9, 3.10)
- Django (2.2)
- Django-environ (0.9)
- mysqlclient (2.1.1)
- python-memcached (1.59)

Information
===========
- Cada proyecto tiene su propio archivo .env


PROYECTO NORMAL
===============

Se deja un archivo .env.template con las variables de entorno para el archivo .env

Se adjunta archivo requirements.txt con las librerias necesarias para el correcto funcionamiento del proyecto.

Se deben de seguir las siguientes instrucciones:

- Instalando librerias:
```cmd
pip install -r requirements.txt
```

- Migraciones:
```python
python manage.py makemigrations
python manage.py migrate
```

- Cargando la bd
```python
python manage.py loaddata fixture/data.json
```

Al agregar la data se crea un usuario con las siguientes credenciales:
- usuario: admin
- contraseña: admin

También se crea 5 objetos de tipo "Redirect" para realizar las pruebas de la carga de los datos a la cache.

Luego de esto ya estaría listo para levantar el proyecto
```python
python manage.py runserver
```

PROYECTO CON DOCKER
===================
Se deja un archivo .env.template con las variables de entorno para el archivo .env

Antes de levantar el proyecto con docker se debe de crear el archivo .env con las variables de entorno para la conexión a la base de datos.

para leventar el proyecto:
```cmd
docker-compose up --build
```

Automaticamente se realizaran las migraciones y la carga de los datos en la bd.

Esto levantará el proyecto en el 0.0.0.0:8000

Para acceder al admin se debe de ingresar con las siguientes credenciales:
- usuario: admin
- contraseña: admin

COLECCIONES POSTMAN
===================
Se adjunta un archivo de tipo colección que contiene las peticiones GET para hacer las pruebas.

- Challenge_TMOB.postman_collection.json

POSIBLES ERRORES
================
Si hay un error con el memcached (si esta ocupado el puerto), correr el siguiente comando:
```cmd
service memcached stop
```
