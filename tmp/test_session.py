from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


url = 'http://127.0.0.1:61896' 

session_id = 'ce6b1df67230a461884dff3ea2f5dc80' 


driver = webdriver.Remote(command_executor=url,desired_capabilities={})
driver.session_id = session_id



driver.get('https://webgate.ec.europa.eu/cpnp/main/?event=main.product.newComponent&component=N&p=N')



# ------------------------------
#    general information tab
# ------------------------------

# industryReference ;input
subls = ['', '//*[@id="industryReference"]','Hair']
driver.find_element_by_xpath(subls[1]).send_keys(subls[2])


# prod name ;input
subls = ['', '//*[@id="productName_1"]','prod name']
driver.find_element_by_xpath(subls[1]).send_keys(subls[2])


# lang select ;selector
subls = ['', '//*[@id="productNameLng_1"]/option[9]','']
driver.find_element_by_xpath(subls[1]).click()

# under 3 years ;check
driver.find_element_by_xpath('//*[@id="under3Year_N"]').click()


#address 
driver.find_element_by_xpath('//*[@id="contactPerson"]/option[2]').click()


# no community. cannot click ordinary. but via 'execute_script'
# see: https://stackoverflow.com/questions/37879010/selenium-debugging-element-is-not-clickable-at-point-x-y
element = driver.find_element_by_xpath('//*[@id="ctyShowN"]')
driver.execute_script("arguments[0].click();", element)


#first country
driver.find_element_by_xpath('//*[@id="msCty"]/option[30]').click()


# ------------------------------
#   goto Product details tab
# ------------------------------
# cannot click ordinary. but via 'execute_script' tab
element =  driver.find_element_by_xpath('//*[@class="tabLink" and text()="Product details"]')
driver.execute_script("arguments[0].click();", element)




# CMR A1 A2 check
element =  driver.find_element_by_xpath('//input[@class="cmr" and @value="N"]')
driver.execute_script("arguments[0].click();", element)



#open nanomaterials area
subls = ['', '//*[starts-with(@id,"accordion_")]/h3[1]','']
driver.find_element_by_xpath(subls[1]).click()
# nanomaterials check
element =  driver.find_element_by_xpath('//input[@class="nano" and @value="N"]')
driver.execute_script("arguments[0].click();", element)


# category & frame check
#open category area
subls = ['', '//*[starts-with(@id,"accordion_")]/h3[3]/a','']
driver.find_element_by_xpath(subls[1]).click()

#cat1
#subls = ['', '//*[starts-with(@id,"category1_")]/option[3]','']
subls = ['', '//*[starts-with(@id,"category1_")]/option[contains(text(), "Hair and scalp products")]','']
driver.find_element_by_xpath(subls[1]).click()



#cat2
subls = ['', '//*[starts-with(@id,"category2_")]/option[contains(text(), "Hair and scalp care and cleansing products")]','']
#wait for appearance
el = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, subls[1])))
driver.find_element_by_xpath(subls[1]).click()


#cat3
subls = ['', '//*[starts-with(@id,"category3_")]/option[contains(text(), "Hair conditioner")]','']
#wait for appearance
el = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, subls[1])))
driver.find_element_by_xpath(subls[1]).click()



#Physical form
# "1">Solid/pressed powder  "2">Loose powder  "3">Cream / paste  "4">Liquid  "5">Foam  "6">Spray  "-2">Other
subls = ['', '//*[starts-with(@id,"physicalForm_")]/option[contains(text(), "Cream / paste")]','']
driver.find_element_by_xpath(subls[1]).click()


# specialPackaging
element =  driver.find_element_by_xpath('//input[@class="specialPkg" and @value="N"]')
driver.execute_script("arguments[0].click();", element)



#Formulation name
subls = ['', '//*[starts-with(@id,"frameFormaulation_")]/option[contains(text(), "Hair Conditioner") and @title = "10.04.2013"]','']
#wait for appearance
el = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, subls[1])))
driver.find_element_by_xpath(subls[1]).click()







