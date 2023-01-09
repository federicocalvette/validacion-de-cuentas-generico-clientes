# validacion-de-cuentas-generico-clientes

## Primeros pasos

Creo mi environment
```bash
python3 -m venv env
```

Activo el environment que cree
```bash
source env/bin/activate
```

Instalo las dependencias 
```bash
pip install -r requirements.txt
```

Ingreso a la carpeta de la APP
```bash
cd app
```

Cambio el nombre de settings_exaples.py a settings.py
```bash
mv settings_example.py settings.py 
```

Recordatorio! 
Debo pegar mi API Key de Prometeo en la variable API_KEY de settings.py
Y generar una SECRET_KEY para la app de Flask, por ejemplo df0331cefc6c2b9a5d0208a726a5d1c0fd37324feba25506

Seteo las variables
```bash
export FLASK_APP=app
```
```bash
export FLASK_ENV=development
```

Corro la APP
```bash
flask run
```
Una vez corriendo, podemos ir a la web http://127.0.0.1:5000/ y hacer uso de nuestra demo (:


## Personaliza la demo con el aspecto de tu empresa! 
###### Logo y Favicon
Cambia el logo que se encuentra en el directorio: */validacion-de-cuentas-generico-clientes/app/static/img/* con el nombre **logo.png** por el de tu empresa. Y realiza el mismo procedimiento para **favicon.png**.
 
###### Colores
Para personalizar los colores de la demo a unos que se apeguen más a los que representan tu empresa, puedes editar las variables:
```css
:root {
   --color_principal: #ffff00;
   --color_secundario: #ffffaa;
   --color_letras_principal: #2b2828;
   --color_letras_secundario: #ffffff;
}
```
que se encuentran en el archivo **style.css**, del directorio */validacion-de-cuentas-generico-clientes/app/static/css/*



## Ejemplos

###### Video

https://user-images.githubusercontent.com/97620201/210805261-a82167f0-9ee4-4a8d-b828-c99c2e309e5d.mp4


###### Imagenes
![image (4)](https://user-images.githubusercontent.com/97620201/210805072-cf128c68-9100-4956-9962-fbfb106df5cd.png)
![image (2)](https://user-images.githubusercontent.com/97620201/210804964-c4663837-5365-4400-bb1e-f23b89fa2f49.png)
![image (3)](https://user-images.githubusercontent.com/97620201/210804978-11f5af20-11e7-4cdd-b7b8-d59f01dc3c75.png)

