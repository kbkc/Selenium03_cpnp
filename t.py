from dicttoxml import dicttoxml
from xmltodict import parse, unparse
from funcs import *
import sys

xml_fn = 'session_data.xml'

def main():
    d = read_session_data()
    print('--- SESSSION DATA ---: \n',d)
    driver = webdriver.Remote(command_executor=d['url'],desired_capabilities={})
    driver.session_id = d['id']
    driver.get('https://webgate.ec.europa.eu/cpnp/main/?event=main.product.newComponent&component=N&p=N')
    print('\nhihih')

    #subls = ['', '//*[@id="question_100023_100037_0F847DEB-0C95-4D16-CCEED2257D38ACDD-7EB84F345AFE2125D1F476605277A2EB"]','Hair Care Cosmetics']
    #driver.find_element_by_xpath(subls[1]).send_keys(subls[2])
    # -----------------------------------------------------------------------
    #                  Sticker and label append files
    # -----------------------------------------------------------------------
    # image + ext : ld[16]+'.'+ ld[17]      sticker fname - ld[18] 
    subls = ['', '//*[starts-with(@id,"accordion_")]/h3[4]','']
    element =  driver.find_element_by_xpath(subls[1])
    driver.execute_script('arguments[0].click();', element)   

    #subls = ['', f'//*[starts-with(@id,"question_100023_100037")]','555']
    #driver.find_element_by_xpath(subls[1]).send_keys(subls[2])
    print('\nhihih')




def pain():
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
