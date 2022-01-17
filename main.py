from urllib import response
import requests
from flask import Flask, request, make_response
import xml.etree.ElementTree as ET
from config import *

app = Flask(__name__)

@app.route('/', methods=['GET'])
def test():
    return "It's OK"

@app.route('/', methods=['POST'])
def handler():
    headers = dict(request.headers) # заголовки входящего запроса
    data = request.data.decode('utf-8') # тело входящего запроса
    response_from_store = requests.post(URL_STORE, headers=headers, data=data) 
    response_headers =  dict(response_from_store.headers)
    response_status_code = response_from_store.status_code
    response_body = response_from_store.text
    return (response_body, response_status_code, response_headers)

if __name__ == "__main__":
    # port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=True)



