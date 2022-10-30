
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from funcs import *
from add_product_codes import *
import sys

config_ffn = 'config/datas.xlsx'
config_sheet_login = 'login'
config_sheet_add = 'prod_add_init'
task_ffn = 'task01/sbor.xlsx'
task_sheet_data = 'datas'
img_folder = 'task01/'
sticker_folder = 'task01/'
data_range_start = 2

url = 'http://127.0.0.1:58908'
session_id = '58f303477b715885adab9a5e7cc86948'

def main():
    print("Hello World!")
    ltask = read_settings(task_ffn , task_sheet_data)
    '''
    for lt in ltask:
        if ltask.index(lt) > data_range_start:
            for i in range(0,20):  #len(lt)):
                print(i,'>>',ltask[2][i],'>>',lt[i])
        print('\n')
    '''
    #print(ltask[2],'\n\n',ltask[3])

    #exit(0)

    driver = webdriver.Remote(command_executor=url,desired_capabilities={})
    driver.session_id = session_id

    run_rule_add_product(driver, ltask[2],ltask[3])




def run_rule_add_product(driver, lx,ld):
 
    # ------------------------------
    #    general information tab
    # ------------------------------

    # industryReference ;input
    subls = ['', '//*[@id="industryReference"]','Hair Care Cosmetics']
    driver.find_element_by_xpath(subls[1]).send_keys(subls[2])


    # prod name ;input
    subls = ['', f'//*[@id="{lx[1]}"]',ld[1]]
    driver.find_element_by_xpath(subls[1]).send_keys(subls[2])


    # lang select ;selector ,ld[2] = en = 9 
    subls = ['', f'//*[@id="{lx[2]}"]/option[9]','']
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


    #first country Poland = 30 Italia = ?
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
    subls = ['', f'//input[@class="{lx[3]}" and @value="{ld[3]}"]','']
    element =  driver.find_element_by_xpath(subls[1])
    driver.execute_script("arguments[0].click();", element)


    # #######################################################################
    # NANOMATEIARLS AREA
    # open nanomaterials area
    time.sleep(2)
    subls = ['', '//*[starts-with(@id,"accordion_")]/h3[2]','']
    driver.find_element_by_xpath(subls[1]).click()

    # nanomaterials check
    subls = ['', f'//input[@class="{lx[4]}" and @value="{ld[4]}"]','']
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
    subls = ['', f'//*[starts-with(@id,"{lx[5]}")]/option[contains(text(), "{ld[5]}")]','']
    driver.find_element_by_xpath(subls[1]).click()



    #cat2
    #wait for appearance
    subls = ['', f'//*[starts-with(@id,"{lx[6]}")]/option[contains(text(), "{ld[6]}")]','']
    el = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, subls[1])))
    driver.find_element_by_xpath(subls[1]).click()


    #cat3
    #wait for appearance
    subls = ['', f'//*[starts-with(@id,"{lx[7]}")]/option[contains(text(), "{ld[7]}")]','']
    el = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, subls[1])))
    driver.find_element_by_xpath(subls[1]).click()



    #Physical form
    # "1">Solid/pressed powder  "2">Loose powder  "3">Cream / paste  "4">Liquid  "5">Foam  "6">Spray  "-2">Other
    subls = ['', f'//*[starts-with(@id,"{lx[8]}")]/option[contains(text(), "{ld[8]}")]','']
    driver.find_element_by_xpath(subls[1]).click()


    # specialPackaging
    subls = ['', f'//input[@class="{lx[9]}" and @value="{ld[9]}"]','']
    element =  driver.find_element_by_xpath(subls[1])
    driver.execute_script("arguments[0].click();", element)



    # Formulation name
    # wait for appearance
    time.sleep(3)
    subls = ['', f'//*[starts-with(@id,"{lx[10]}")]/option[contains(text(), "{ld[10]}")]','']
    #['', '//*[starts-with(@id,"frameFormaulation_")]/option[contains(text(), "Hair Conditioner") and @title = "10.04.2013"]','']
   # el = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, subls[1])))
    driver.find_element_by_xpath(subls[1]).click()


    # notification type
    #time.sleep(2)
    #subls = ['', f'//*[starts-with(@id,"{lx[11]}")]/option[contains(text(), "{ld[11]}")]','']
    #driver.find_element_by_xpath(subls[1]).click()

    # notification type
    time.sleep(2)
    subls = ['', '//*[starts-with(@id,"notificationType_")]/option[contains(text(), "Exact concentrations")]','']
    driver.find_element_by_xpath(subls[1]).click()



    subls = ['', '//input[@class="fileFormula" and @value="Y"]','']
    element =  driver.find_element_by_xpath(subls[1])
    driver.execute_script("arguments[0].click();", element)
    alertObj = driver.switch_to.alert
    alertObj.accept()



    #subls = ['', '//input[starts-with(@id,"formulaDoc_") and @type="file"]','']
    #element =  driver.find_element_by_xpath(subls[1])
    #driver.execute_script("arguments[0].click();", element)

    input("Press Enter to continue...")

    #print('that\'s all')


main()
