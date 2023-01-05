from flask import Flask, render_template, request
import prometeo_request
import settings

app = Flask(__name__)
app.config['SECRET_KEY'] = settings.SECRET_KEY


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/validation/', methods=['POST'])
def validation():

    numero_cuenta = request.form['numero_cuenta']
    codigo_banco = request.form['codigo_banco']
    codigo_pais = request.form['codigo_pais']

    if not numero_cuenta:
        return 'Error en el formulario, el número de cuenta es requerido!'
    
    elif not codigo_banco and codigo_pais == 'UY':
        return 'Error en el formulario, el código de banco es requerido!'
    
    elif not codigo_pais:
        return 'Error en el formulario, el código de país es requerido!'
    
    else:
        response_request = prometeo_request.make_request(numero_cuenta, codigo_banco, codigo_pais)

        if response_request == "Cuenta credito invalida": return response_request

        elif response_request == "Error de comunicacion con el banco": return response_request

        elif "Parametros invalidos" in response_request: return response_request

        else: return f'El titular de la cuenta bancaria {numero_cuenta} se llama: {response_request}.'
             

