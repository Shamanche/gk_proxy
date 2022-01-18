from lxml import etree 

def transaction_type(root):
    transaction_element = root.find('.//{*}Body/')
    namespace_none = transaction_element.nsmap[None] 
    transaction_name = transaction_element.tag.replace(
        '{' + namespace_none + '}', '') # убираем namespace вместе с {}
    return transaction_name

def econom(root):
    
    cheque = root.find('.//{*}cheque')
    cheque_xml = etree.XML(bytes(cheque.text, 'utf-16'))

    for cheque_line in cheque_xml.findall('.//ChequeLine'):
        price = cheque_line.get('Price')
        cheque_line.set('MinPrice', price)

    cheque_str = etree.tostring(cheque_xml).decode('utf-8')
    cheque.text = cheque_str
    body = etree.tostring(root)
    return body