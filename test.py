
from lxml import etree 
body = b'<?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema"><soap:Body><SubtractBonus45 xmlns="http://tempuri.org/"><discountCardNumber>0000002100000001</discountCardNumber><amount>15</amount><cheque>&lt;?xml version="1.0" encoding="utf-16"?&gt;&lt;Cheque xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" StoreID="0" ShiftNo="2411" ChequeUID="{BA31562A-9B8B-48AB-A7B9-2040B7B1B512}" ChequeNo="318606" OpenTime="2022-01-17T14:40:19" CloseTime="2022-01-17T14:42:12" Amount="30.00000" SubtractedBonus="0" PositionCount="0" Status="Open" ChequeType="Sale"&gt;&lt;DiscountCard DiscountCardID="0" DiscountCardNo="0000002100000001" SubtractAmount="0" BonusCard="true" EnteredAsPhoneNumber="false" SubtractedBonus="0" /&gt;&lt;ChequeLines&gt;&lt;ChequeLine ChequeLineNo="1" NoPayBonus="false" NoAddBonus="false" NoDiscounts="false" Price="10.00000" Quantity="1.00000" Amount="10.00000" MinAmount="0" MinPrice="0.00000" MaxDiscount="100.00000" BonusDiscount="0.00000"&gt;&lt;Item ItemID="15564" Barcode="2409900010085" /&gt;&lt;Discounts /&gt;&lt;/ChequeLine&gt;&lt;ChequeLine ChequeLineNo="2" NoPayBonus="false" NoAddBonus="false" NoDiscounts="false" Price="10.00000" Quantity="1.00000" Amount="10.00000" MinAmount="0" MinPrice="0.00000" MaxDiscount="100.00000" BonusDiscount="0.00000"&gt;&lt;Item ItemID="15563" Barcode="2409900010146" /&gt;&lt;Discounts /&gt;&lt;/ChequeLine&gt;&lt;ChequeLine ChequeLineNo="3" NoPayBonus="false" NoAddBonus="false" NoDiscounts="false" Price="10.00000" Quantity="1.00000" Amount="10.00000" MinAmount="0" MinPrice="0.00000" MaxDiscount="100.00000" BonusDiscount="0.00000"&gt;&lt;Item ItemID="9123" Barcode="2300100053219" /&gt;&lt;Discounts /&gt;&lt;/ChequeLine&gt;&lt;/ChequeLines&gt;&lt;Discounts /&gt;&lt;Payments /&gt;&lt;Messages /&gt;&lt;/Cheque&gt;</cheque></SubtractBonus45></soap:Body></soap:Envelope>'
string1 = b'<?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema"><soap:Body><Ping xmlns="http://tempuri.org/" /></soap:Body></soap:Envelope>'
string2 = '<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema"><soap:Body><Ping xmlns="http://tempuri.org/" /></soap:Body></soap:Envelope>'


root = etree.XML(body)
transaction_element = root.find('.//{*}Body/')
namespace_none = transaction_element.nsmap[None] 
tranzaction_type = transaction_element.tag.replace('{' + namespace_none + '}', '')
cheque = root.find('.//{*}cheque')
cheque_xml = etree.XML(bytes(cheque.text, 'utf-16'))

for cheque_line in cheque_xml.findall('.//ChequeLine'):
    price = cheque_line.get('Price')
    cheque_line.set('MinPrice', price)

cheque_str = etree.tostring(cheque_xml).decode('utf-8')
cheque.text = cheque_str
body = etree.tostring(root)

pass