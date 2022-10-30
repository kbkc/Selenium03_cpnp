from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


url = 'http://127.0.0.1:58908'
session_id = '58f303477b715885adab9a5e7cc86948'

driver = webdriver.Remote(command_executor=url,desired_capabilities={})
driver.session_id = session_id



driver.get('https://webgate.ec.europa.eu/cpnp/main/?event=main.product.newComponent&component=N&p=N')



# ------------------------------
#    general information tab
# ------------------------------
'''
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
'''

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
subls = ['', '//*[starts-with(@id,"category2_")]/option[contains(text(), "Hair and scalp care and cleansing products")]','']
el = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, subls[1])))
driver.find_element_by_xpath(subls[1]).click()


#cat3
#wait for appearance
subls = ['', '//*[starts-with(@id,"category3_")]/option[contains(text(), "Hair conditioner")]','']
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
subls = ['', '//*[starts-with(@id,"frameFormaulation_")]/option[contains(text(), "Hair Conditioner")]','']
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


print('that\'s all')







