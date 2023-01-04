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

https://user-images.githubusercontent.com/97620201/210638512-a27a8b62-c5fe-4e8b-a06e-c46a600fdbae.mp4


Imagen
![image_example](https://user-images.githubusercontent.com/97620201/210638345-1c4caf77-2b69-462b-9d82-8553717784de.png)
