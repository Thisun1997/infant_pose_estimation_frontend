import json

import requests

base_url = "http://127.0.0.1:5000/"


def sendPostRequest(path, data, method="POST"):
    try:
        response = None
        if method == "POST":
            response = requests.post(base_url + path, data=json.dumps(data), headers={'Content-Type': 'application/json'})
        elif method == "PUT":
            response = requests.put(base_url + path, data=json.dumps(data), headers={'Content-Type': 'application/json'})
        return ({
            "code": response.status_code,
            "message": response.json()['message']
        })
    except Exception as e:
        return ({
            "code": 500,
            "message": "Internal Error: " + str(e)
        })


def has_empty_or_null_value(d):
    for key, value in d.items():
        if value in [None, '', [], {}, ()]:
            return True
    return False


def fetch_data(path, data=None):
    try:
        if data:
            response = requests.get(base_url + path, data=json.dumps(data), headers={'Content-Type': 'application/json'})
        else:
            response = requests.get(base_url + path, headers={'Content-Type': 'application/json'})
        return response.json()
    except Exception as e:
        return ({
            "code": 500,
            "message": "Internal Error: " + str(e)
        })


def get_prediction(path, data):
    try:
        response = requests.get(base_url + path, data=json.dumps(data), headers={'Content-Type': 'application/json'})
        if response.status_code == 200:
            img_data = response.content
            return img_data
        else:
            return f"Error: {response.status_code} - {response.content}"
    except Exception as e:
        return f'Error: {str(e)}'
