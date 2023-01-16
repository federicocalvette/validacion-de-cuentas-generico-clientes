from flask import Flask, render_template, request
import prometeo_request
import settings

app = Flask(__name__)
app.config['SECRET_KEY'] = settings.SECRET_KEY


@app.route('/', methods=['GET'])
def home():
    """Esta funcion retorna el contenido para el home de la web de demo, solo acepta peticiones GET. 

    Returns:
        render_template: Es un str donde se encuentra el contenído HTML de la pagina web. 
    """
    return render_template('index.html')


@app.route('/validation/', methods=['POST'])
def validation():
    """Funcion que se encarga de llamar al validador de cuentas (API de Prometeo). Controla la respuesta del mismo y retorna un mensaje para el front.

    Returns:
        str: Retorna un string donde se denota el estado de la cuenta o de la solicitud en si. Informando errores o casos satisfactorios. 
    """

    # Variables que recibo desde el form-front y utilizo para consultar a Prometeo por la cuenta.
    numero_cuenta = request.form['numero_cuenta']
    codigo_banco = request.form['codigo_banco']
    codigo_pais = request.form['codigo_pais']

    # Control de parametros previo a la consulta.
    # Controlo que no falten parametros requeridos, ya que afectaría la consulta.
    if not numero_cuenta:
        return 'Error en el formulario, el número de cuenta es requerido!'

    elif not codigo_banco and codigo_pais != 'PE':
        return 'Error en el formulario, el código de banco es requerido!'

    elif not codigo_pais:
        return 'Error en el formulario, el código de país es requerido!'

    else:
        # Si pasa el control de parametros llamo a make_request de prometeo_request, enviando los parametros de numero_cuenta, codigo_banco, codigo_pais.
        # Una vez obtengo la respuesta la guardo en response_request y procedo a enviar el mensaje al front, en funcion de la respuesta obtenida.
        response_request = prometeo_request.make_request(numero_cuenta, codigo_banco, codigo_pais)

        print(type(response_request))

        if type(response_request) is dict:

            if response_request['hasName']:
                return f'El titular de la cuenta bancaria {numero_cuenta} se llama: {response_request["name"]}.'

            else:
                return response_request['message']

        else:
            return 'Error interno'


if __name__ == '__main__':
    app.run(debug=True, port=settings.PORT)