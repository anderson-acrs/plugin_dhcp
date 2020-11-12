import requests
import json
"""
Variaveis de conexão com a API-UFRN. Para mais informações ver README.
"""
URL_BASE = 'https://api.info.ufrn.br/'
VERSION = 'v1'
URL_BASE_AUTENTICACAO = 'https://autenticacao.info.ufrn.br/'
client_id = 'tools-id'
client_secret = 'segredo'
x_api_key = '7a88PIG3R7glZ6nmZrFLoYc3jDQOUtre2cSvGSmR'

def get_token():
    """
    Esta função conecta-se com api para autenticar o usuario e retornar uma token access e com esse token ele ira fazer as consultas a api.
    """
    url_token = URL_BASE_AUTENTICACAO + 'authz-server/oauth/token?client_id='+ client_id +'&client_secret=' + client_secret + '&grant_type=client_credentials'.format(client_id, client_secret)
    requisicao_token = requests.post(url_token)
    resposta = json.loads(requisicao_token.content)
    token = resposta['access_token']
    headers = {'Authorization': 'bearer'+token, 'x-api-key': x_api_key}
    return headers

def get_user(username):
    """
    Essa função consulta um user apartir de seu login.
    """
    headers = get_token()
    URL = URL_BASE +'usuario/'+ VERSION + '/usuarios?login=' + username + '&ativo=true'
    user = requests.get(URL, headers=headers)
    return json.loads(user.content)

def get_unit(unit):
    """
    Essa função consulta uma unidade apartir de seu id-unit.
    """
    headers = get_token()
    URL = URL_BASE + 'unidade/' + VERSION + '/unidades/' + unit
    un = requests.get(URL, headers=headers)
    return json.loads(un.content)

def get_server(complete_name):
    """
    Essa função buscas dados sobre a atuação do servidor.
    """
    headers = get_token()
    URL = URL_BASE +'pessoa/'+ VERSION + '/servidores?nome=' + complete_name + '&ativo=true'
    user = requests.get(URL, headers=headers)
    return json.loads(user.content)