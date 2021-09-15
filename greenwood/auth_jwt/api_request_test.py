import json
import requests


def answer_reg():# запустить со своими данными для регистрации
    url = 'http://127.0.0.1:8002/api/users/'

    api_mes = {
        "user": {
            "username": "user4",
            "email": "user4@user.user",
            "password": "qweasdzxc"
        }}

    headers = {'Content-type': 'application/json'}

    answer=requests.post(url,data=json.dumps(api_mes),headers=headers).text

    try:
        print(f"Congratulations\nYour token is {json.loads(answer)['token']}")
    except:
        print(answer)
    return



def answer_login():# логин по полученому токену
    url = 'http://127.0.0.1:8002/api/users/login/'

    api_mes = {
        "user": {
            # "username": "user2",
            "email": "user4@user.user",
            "password": "qweasdzxc"

        }}

    headers = {'Content-type': 'application/json'}

    answer=requests.post(url,data=json.dumps(api_mes),headers=headers).text

    print('answer log',answer)
    print(json.loads(answer)['user']['token'])
    return json.loads(answer)['user']['token']

# answer_login(token) answer {"user": {"email": "user2@user.user", "username": "user2", "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MywiZXhwIjoxNjMxMzY5OTY2fQ.eTl_H3QaPAuny-hudWso-gFUjq9xTRdnnHqhEcCDL8E"}}
#
# Pro

def answer_login_detail(token='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6NCwiZXhwIjoxNjMxMzc2OTYyfQ.8_0Bif_ZbekU-U9KQJ42nzXVsHhKIqG2QtJu3eZR9v4'):# логин по полученому токену
    url = 'http://127.0.0.1:8002/api/user/'

    api_mes = {
        "user": {
            "username": "user2",
            # "email": "user2@user.user",
            # "password": "qweasdzxc",
            "token":token

        }}

    headers = {'Content-type': 'application/json'}

    answer=requests.get(url,params=api_mes,headers=headers).text

    print('answer',answer)
    return
#
# answer_login()

# token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MywiZXhwIjoxNjMxMzcxNTEyfQ.h9G9byOg0MDmTo8wt5CgdcgP_q423EIBmltBcftKv0M"

# answer_login_detail(answer_login())

answer_login_detail('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MiwiZXhwIjoxNjMxNzA3MTY3fQ.0h5FfxAw7kIc88FUHxz4G52o7pSZCr4UOSijukPV0aU')