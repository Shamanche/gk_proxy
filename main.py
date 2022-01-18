import requests, os
from flask import Flask, request, make_response
from lxml import etree 

from config import *
import modify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def test():
    return "It's OK"

@app.route('/', methods=['POST'])
def handler():
    headers = dict(request.headers) # заголовки входящего запроса
    headers['Authorization'] ='Basic cGF0cmlrbWFyaVBPUy10ZXN0OnM2ZDN5OGVaNA==' #временно
    # data = request.data.decode('utf-8') # тело входящего запроса
    request_body = request.data # тело входящего запроса в bytes
    root = etree.XML(request_body) # строим дерево xml
    if modify.transaction_type(root) == 'SubtractBonus45':
        response_body = modify.econom(root)
    else:
        response_body = request_body.decode('utf-8')
    response_from_store = requests.post(
        URL_STORE, headers=headers, data=response_body)
    response_headers =  dict(response_from_store.headers)
    response_status_code = response_from_store.status_code
    # response_body = response_from_store.text
    response_body = response_from_store.content # в формате bytes
    
    return (response_body, response_status_code, response_headers)





if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=True)



