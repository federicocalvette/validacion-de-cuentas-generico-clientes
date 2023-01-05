# validacion-de-cuentas-generico-clientes

### Primeros pasos

Creo mi environment
```
python3 -m venv env
```

Activo el environment que cree
```
source env/bin/activate
```

Instalo las dependencias 
```
pip install -r requirements.txt
```

Ingreso a la carpeta de la APP
```
cd app
```

Cambio el nombre de settings_exaples.py a settings.py
```
mv settings_example.py settings.py 
```

Recordatorio! 
Debo pegar mi API Key de Prometeo en la variable API_KEY de settings.py
Y generar una SECRET_KEY para la app de Flask, por ejemplo df0331cefc6c2b9a5d0208a726a5d1c0fd37324feba25506

Seteo las variables
```
export FLASK_APP=app
```
```
export FLASK_ENV=development
```

Corro la APP
```
flask run
```
Una vez corriendo, podemos ir a la web http://127.0.0.1:5000/ y hacer uso de nuestra demo (:



### Ejemplos

Video

https://user-images.githubusercontent.com/97620201/210805261-a82167f0-9ee4-4a8d-b828-c99c2e309e5d.mp4


Imagenes
![image (4)](https://user-images.githubusercontent.com/97620201/210805072-cf128c68-9100-4956-9962-fbfb106df5cd.png)
![image (2)](https://user-images.githubusercontent.com/97620201/210804964-c4663837-5365-4400-bb1e-f23b89fa2f49.png)
![image (3)](https://user-images.githubusercontent.com/97620201/210804978-11f5af20-11e7-4cdd-b7b8-d59f01dc3c75.png)

