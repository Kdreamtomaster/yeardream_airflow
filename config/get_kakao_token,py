import requests
# client_id, authorize_code 노출 주의, 실제 값은 임시로만 넣고 Git에 올라가지 않도록 유의

client_id = '6c64535173392f61f5cc7f35089be7b2'
redirect_uri = 'https://exmaple.com/oauth'
authorize_code = 'gEX3Oo-W6BJUIO5UQxbJjMvzT-kkORlhqY6uMAEpt1VRgF53K_PQtwAAAAQKKcjYAAABkC35tja2xj-RG-1vuA'


token_url = 'https://kauth.kakao.com/oauth/token'
data = {
    'grant_type': 'authorization_code',
    'client_id': client_id,
    'redirect_uri': redirect_uri,
    'code': authorize_code,
    }

response = requests.post(token_url, data=data)
tokens = response.json()
print(tokens)

