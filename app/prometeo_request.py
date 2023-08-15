import requests
import settings


def make_request(nro_cbu, bk_code, country_code):

    url = settings.URL

    payload = f'nro_cbu={nro_cbu}&bk_code={bk_code}&country_code={country_code}'

    headers = {
        'x-api-key': settings.API_KEY,
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    try:
        response = requests.request("POST", url, headers=headers, data=payload)
    except Exception as error:
        return f'Error de tipo exception: {str(error)}'

    message = ''
    
    data_response = {
        'hasName': False,
        'name': '',
        'message': '',
        'currency': ''
    }

    if response.status_code == 200:
        response_json = response.json()
        data_response['name'] = response_json['data']['beneficiary_name']
        data_response['hasName'] = True
        data_response['currency'] = response_json["data"]["account_currency"]
        return data_response

    elif response.status_code == 404:
        message = "Cuenta credito invalida"

    elif response.status_code == 503:
        message = "Error de comunicacion con el banco"

    elif response.status_code == 400:
        message = f"Parametros invalidos -> {str(response.json())}"

    else:
        message = 'Error inesperado'

    data_response['message'] = message
    data_response['hasName'] = False
    data_response['name'] = ''
    data_response['currency'] = ''

    return data_response