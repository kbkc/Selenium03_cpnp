from dicttoxml import dicttoxml
from xmltodict import parse, unparse

xml_fn = 'session_data.xml'

def main():
	dict = {'id': '1345345t54g4f34', 'url': '30://gfgbf/gnfn'}



	out = dicttoxml(dict, custom_root='session_data', attr_type=False)

	#out = unparse(dict, full_document=False)
	with open(xml_fn, 'wb') as file:
		file.write(out)
		file.close()
	
	with open(xml_fn, 'rb') as f:    # notice the "rb" mode
		xmld = f.read()
		d = parse(xmld)
	
	print(d)
	print('id = ', d['session_data']['id'], ', url = ', d['session_data']['url'])

main()