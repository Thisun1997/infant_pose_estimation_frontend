import json

import requests

base_url = "http://127.0.0.1:5000/"


def sendPostRequest(path, data):
    try:
        response = requests.post(base_url + path, data=json.dumps(data), headers={'Content-Type': 'application/json'})
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
        if value in [None, '', [], {}, ()]:  # Add any other values you consider as "empty"
            return True
    return False


def fetch_data(path, data):
    try:
        response = requests.get(base_url + path, data=json.dumps(data), headers={'Content-Type': 'application/json'})
        return response.json()
    except Exception as e:
        return ({
            "code": 500,
            "message": "Internal Error: " + str(e)
        })
