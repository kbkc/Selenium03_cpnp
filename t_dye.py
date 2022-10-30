from dicttoxml import dicttoxml
from xmltodict import parse, unparse
from funcs import *
import sys

xml_fn = 'session_data.xml'

def main():
    d = read_session_data()
    print(d)
    driver = webdriver.Remote(command_executor=d['url'],desired_capabilities={})
    driver.session_id = d['id']
    driver.get('https://webgate.ec.europa.eu/cpnp/main/?event=main.product.newComponent&component=N&p=N')
    # -----------------------------------------------------------------------
    #                  Sticker and label append files
    # -----------------------------------------------------------------------
    # image + ext : ld[16]+'.'+ ld[17]      sticker fname - ld[18] 
    subls = ['', '//*[starts-with(@id,"accordion_")]/h3[4]','']
    element =  driver.find_element_by_xpath(subls[1])
    driver.execute_script('arguments[0].click();', element)   





    test_fill(driver)
    
    print('\n-------')
    

    productID = driver.find_element_by_xpath('//*[@id="productID"]').get_attribute("value")
    productID_part3 = productID[-32:]
    print('productID = ',productID)
    print('productID = ',productID_part3)

    #subls = ['', '//*[@id="question_100023_100037_0F847DEB-0C95-4D16-CCEED2257D38ACDD-7EB84F345AFE2125D1F476605277A2EB"]','Hair Care Cosmetics']
    #driver.find_element_by_xpath(subls[1]).send_keys(subls[2])

    time.sleep(2)



def test_fill(driver):
    # ------------------------------
    #    general information tab
    # ------------------------------

    # industryReference ;input
    subls = ['', '//*[@id="industryReference"]','Hair Care Cosmetics']
    driver.find_element_by_xpath(subls[1]).send_keys(subls[2])


    # prod name ;input
    subls = ['', '//*[@id="productName_1"]','prod name']
    driver.find_element_by_xpath(subls[1]).send_keys(subls[2])


    # lang select ;selector
    subls = ['', '//*[@id="productNameLng_1"]/option[9]','']
    driver.find_element_by_xpath(subls[1]).click()

    # under 3 years ;check
    subls = ['', '//*[@id="under3Year_N"]','']
    driver.find_element_by_xpath(subls[1]).click()


    #address 
    subls = ['', '//*[@id="contactPerson"]/option[2]','']
    driver.find_element_by_xpath(subls[1]).click()


    # no community. cannot click ordinary. but via 'execute_script'
    # see: https://stackoverflow.com/questions/37879010/selenium-debugging-element-is-not-clickable-at-point-x-y
    subls = ['', '//*[@id="ctyShowN"]','']
    element = driver.find_element_by_xpath(subls[1])
    driver.execute_script("arguments[0].click();", element)


    #first country
    subls = ['', '//*[@id="msCty"]/option[30]','']
    driver.find_element_by_xpath(subls[1]).click()


    # ------------------------------
    #   goto Product details tab
    # ------------------------------
    # cannot click ordinary. but via 'execute_script' tab

    subls = ['', '//*[@class="tabLink" and text()="Product details"]','']
    element =  driver.find_element_by_xpath(subls[1])
    driver.execute_script("arguments[0].click();", element)



    # #######################################################################
    # CMR A1 A2 check
    subls = ['', '//input[@class="cmr" and @value="N"]','']
    element =  driver.find_element_by_xpath(subls[1])
    driver.execute_script("arguments[0].click();", element)


    # #######################################################################
    # NANOMATEIARLS AREA
    # open nanomaterials area
    time.sleep(2)
    subls = ['', '//*[starts-with(@id,"accordion_")]/h3[2]','']
    driver.find_element_by_xpath(subls[1]).click()

    # nanomaterials check
    subls = ['', '//input[@class="nano" and @value="N"]','']
    element =  driver.find_element_by_xpath(subls[1])
    driver.execute_script("arguments[0].click();", element)


    # #######################################################################
    # CATEGORY AREA
    # category & frame check
    # open category area
    time.sleep(1)
    subls = ['', '//*[starts-with(@id,"accordion_")]/h3[3]','']
    #driver.find_element_by_xpath(subls[1]).click()
    element =  driver.find_element_by_xpath(subls[1])
    driver.execute_script('arguments[0].click();', element)

    #cat1
    #subls = ['', '//*[starts-with(@id,"category1_")]/option[3]','']
    subls = ['', '//*[starts-with(@id,"category1_")]/option[contains(text(), "Hair and scalp products")]','']
    driver.find_element_by_xpath(subls[1]).click()



    #cat2
    #wait for appearance
    subls = ['', '//*[starts-with(@id,"category2_")]/option[contains(text(), "Hair colouring products")]','']
    el = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, subls[1])))
    driver.find_element_by_xpath(subls[1]).click()


    #cat3
    #wait for appearance
    subls = ['', '//*[starts-with(@id,"category3_")]/option[contains(text(), "Oxidative hair colour products")]','']
    el = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, subls[1])))
    driver.find_element_by_xpath(subls[1]).click()



    #Physical form
    # "1">Solid/pressed powder  "2">Loose powder  "3">Cream / paste  "4">Liquid  "5">Foam  "6">Spray  "-2">Other
    subls = ['', '//*[starts-with(@id,"physicalForm_")]/option[contains(text(), "Cream / paste")]','']
    driver.find_element_by_xpath(subls[1]).click()


    # specialPackaging
    subls = ['', '//input[@class="specialPkg" and @value="N"]','']
    element =  driver.find_element_by_xpath(subls[1])
    driver.execute_script("arguments[0].click();", element)



    # Formulation name
    # wait for appearance
    time.sleep(3)
    subls = ['', '//*[starts-with(@id,"frameFormaulation_")]/option[contains(text(), "Hair Colorant (Permanent, Oxidative Type) - Type 1 : Two Components - Colorant Part")]','']
    #['', '//*[starts-with(@id,"frameFormaulation_")]/option[contains(text(), "Hair Conditioner") and @title = "10.04.2013"]','']
    #el = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, subls[1])))
    driver.find_element_by_xpath(subls[1]).click()


    # notification type
    time.sleep(2)
    subls = ['', '//*[starts-with(@id,"notificationType_")]/option[contains(text(), "Exact concentrations")]','']
    driver.find_element_by_xpath(subls[1]).click()



    subls = ['', '//input[@class="fileFormula" and @value="Y"]','']
    element =  driver.find_element_by_xpath(subls[1])
    driver.execute_script("arguments[0].click();", element)
    alertObj = driver.switch_to.alert
    alertObj.accept()



    subls = ['', '//input[starts-with(@id,"formulaDoc_") and @type="file"]','']
    element =  driver.find_element_by_xpath(subls[1])
    #driver.execute_script("arguments[0].click();", element)

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
