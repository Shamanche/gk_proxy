import requests, os
from flask import Flask, request
from lxml import etree 


URL_STORE = 'http://test.gorkarta.ru:8383/RSLoyaltyStoreService'


app = Flask(__name__)

@app.route('/', methods=['GET'])
def test():
    print('Получен GET запрос')
    return "It's OK"

@app.route('/', methods=['POST'])
def handler():

    def transaction_type(root):
        transaction_element = root.find('.//{*}Body/')
        namespace_none = transaction_element.nsmap[None] 
        transaction_name = transaction_element.tag.replace(
            '{' + namespace_none + '}', '') # убираем namespace вместе с {}
        return transaction_name

    def econom(root): 
        MAX_CHEQUE_SUMM = 20.0
        cheque = root.find('.//{*}cheque')
        cheque_xml = etree.XML(bytes(cheque.text, 'utf-16'))
        cheque_sum = float(cheque_xml.get('Amount'))
        if cheque_sum > MAX_CHEQUE_SUMM:
            for cheque_line in cheque_xml.findall('.//ChequeLine'):
                price = cheque_line.get('Price')
                cheque_line.set('MinPrice', price)

        cheque_str = etree.tostring(cheque_xml).decode('utf-8')
        cheque.text = cheque_str
        body = etree.tostring(root)
        return body

    print('Получен POST запрос.')
    headers = dict(request.headers) # заголовки входящего запроса
    headers['Authorization'] ='Basic cGF0cmlrbWFyaVBPUy10ZXN0OnM2ZDN5OGVaNA==' #временно
    # data = request.data.decode('utf-8') # тело входящего запроса
    request_body = request.data # тело входящего запроса в bytes
    print(request_body)
    root = etree.XML(request_body) # строим дерево xml
    if transaction_type(root) == 'SubtractBonus45':
        response_body = econom(root)
    else:
        response_body = request_body.decode('utf-8')
    response_from_store = requests.post(
        URL_STORE, headers=headers, data=response_body)
    response_headers =  dict(response_from_store.headers)
    response_status_code = response_from_store.status_code
    response_body = response_from_store.content # в формате bytes
    return (response_body, response_status_code, response_headers)



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=True)
