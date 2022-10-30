
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException 
import time
import sys
import msvcrt
from funcs import *
#from main import ini_data

# ----------------------------------------------------------
#                   interrupt timer
# ----------------------------------------------------------
class TimeoutExpired(Exception):
    pass

def input_with_timeout(prompt, timeout, timer=time.monotonic):
    sys.stdout.write(prompt)
    sys.stdout.flush()
    endtime = timer() + timeout
    result = []
    while timer() < endtime:
        if msvcrt.kbhit():
            result.append(msvcrt.getwche()) #XXX can it block on multibyte characters?
            if result[-1] == '\r':
                return ''.join(result[:-1])
        time.sleep(0.04) # just to yield to other processes/threads
    raise TimeoutExpired


# ---------------------------------------------------------------------
#         dublicate new product initial script
# ---------------------------------------------------------------------
def run_rule_dublicate_product(driver, product_name, dbl_prod_rules):
    for s in dbl_prod_rules:
        ssubls = [s[1],s[2],product_name]
        run_subrule(driver, ssubls) 
        time.sleep(1)
       #    run_rule(driver,add_prod_init[i])
    # ----- end notify new product ---------   
    return





def run_rule_change_product(driver, lx,ld,ini_data,menu_selection_result):
    # ------------------------------
    #     get product ID key
    # ------------------------------
    productID = driver.find_element_by_xpath('//*[@id="productID"]').get_attribute("value")
    productID_part3 = productID[-32:]
    print('productID = ',productID)
    print('productID = ',productID_part3)
 
    # ------------------------------
    #    general information tab
    # ------------------------------
    # industryReference - input our artcode - ld[1]   
    col = 1
    subls = ['input', f'//*[@id="{lx[col]}"]',ld[col]]
    run_subrule(driver, subls)

    # prod name ;input   
    col = 2
    subls = ['input', f'//*[@id="{lx[col]}"]',ld[col]]
    run_subrule(driver, subls)

    #  Expand product details tab. cannot click ordinary. but via 'execute_script' tab
    subls = ['execute_script', '//*[@class="tabLink" and text()="Product details"]','']
    run_subrule(driver, subls)


    # expand category area
    subls = ['execute_script', '//*[starts-with(@id,"accordion_")]/h3[3]','']
    run_subrule(driver, subls)

    # -----------------------------------------------------------------------
    #                     Append ingredients fiile
    # -----------------------------------------------------------------------
    col = 14
    subls = ['input', f'//input[starts-with(@id,"formulaDoc_") and contains(@id,"{productID_part3}")]',ini_data.folder_ingredients+ld[col]]
    run_subrule(driver, subls)
    # -----------------------------------------------------------------------
    #                  Sticker and label append files
    # where : image + ext = ld[15]     sticker fname = ld[14]   
    # -----------------------------------------------------------------------
    # expand area
    subls = ['execute_script', '//*[starts-with(@id,"accordion_")]/h3[4]','']
    run_subrule(driver, subls)

    # -----------------------------------------------------
    #                add sticker image
    # -----------------------------------------------------
    # press add sticker file button
    subls = ['execute_script', f'//*[contains(@id,"{productID_part3}")]/fieldset[1]/div[1]/div[2]/button','']
    run_subrule(driver, subls)
    
    col = 15
    subls = ['input', f'//*[@id="document_1"]',ini_data.folder_sticker+ld[col]]
    run_subrule(driver, subls)

    # press save
    subls = ['execute_script', '//*[@id="addBtn"]','']
    run_subrule(driver, subls)
  
    # --------------------------------------------------------------
    #             press add packaging image file button  'url', 'click', 'input','execute_script'
    # --------------------------------------------------------------
    time.sleep(3)
    subls = ['execute_script', f'//*[contains(@id,"{productID_part3}")]/fieldset[2]/div[1]/div[2]/button','']
    run_subrule(driver, subls)

    col = 16
    subls = ['input', f'//*[@id="document_1"]',ini_data.folder_img +ld[col]]
    run_subrule(driver, subls)

    # press save
    subls = ['execute_script', '//*[@id="addBtn"]','']
    run_subrule(driver, subls)   

    # -----------------------------------------------------------------------------
    #                             NOTIFY PRODUCT
    # -----------------------------------------------------------------------------
    time.sleep(3)
    subls = ['execute_script', f'//*[@id="submitBtn"]','']
    run_subrule(driver, subls)

  
    # get cpnp reference
    time.sleep(3)
    log_text = f'------ PRODUCT NOTIFIED ----- \n name: {ld[2]} \n art:\t{ld[1]} \tcpnp reference:\t '
    subls = ['get_text',f'//*[@id="main-content"]/fieldset/div[1]/div[1]','']

    
    cpnp_ref = run_subrule(driver, subls)

    log_text = log_text + cpnp_ref+'\n'

    print(log_text)
    with open(ini_data.task_path + 'log'+'' +'.txt', 'a') as myfile:
        myfile.write(log_text)
    
    print_break_prompt(5)

    return


'''
lx - list of xPath code 
ld - list of data (name, sku ....)
'''
def run_rule_add_product(driver, lx,ld,ini_data,menu_selection_result):

    print('--------------ld---------------------\n')
    for i,d in enumerate(ld):
        print(f'{i}<<-->>{d}')
    print('--------------lx---------------------\n')
    for i,d in enumerate(lx):
        print(f'{i}<<-->>{d}')
    print('--------------lxld---------------------')

    # ------------------------------
    #     get product ID key
    # ------------------------------
    productID = driver.find_element_by_xpath('//*[@id="productID"]').get_attribute("value")
    productID_part3 = productID[-32:]
    print('productID = ',productID)
    print('productID = ',productID_part3)
 
    # ------------------------------
    #    general information tab
    # ------------------------------
    # industryReference - input our artcode - ld[1]   
    col = 1
    subls = ['input', f'//*[@id="{lx[col]}"]',ld[col]]
    run_subrule(driver, subls)

    # prod name ;input   
    col = 2
    subls = ['input', f'//*[@id="{lx[col]}"]',ld[col]]
    run_subrule(driver, subls)

    # lang select ;selector ,ld[2] = en = 9 
    col = 3
    subls = ['click', f'//*[@id="{lx[col]}"]/option[9]','']
    run_subrule(driver, subls)

    # under 3 years ;check
    subls = ['click', '//*[@id="under3Year_N"]','']
    run_subrule(driver, subls)

    #address select
    subls = ['click', '//*[@id="contactPerson"]/option[2]','']
    run_subrule(driver, subls)

    # no community. cannot click ordinary. but via 'execute_script'
    # see: https://stackoverflow.com/questions/37879010/selenium-debugging-element-is-not-clickable-at-point-x-y
    subls = ['execute_script', '//*[@id="ctyShowN"]','']
    run_subrule(driver, subls)

    #first country Poland = 30 Italia = ? 
    subls = ['click', '//*[@id="msCty"]/option[30]','']
    run_subrule(driver, subls)

    #  Expand product details tab. cannot click ordinary. but via 'execute_script' tab
    subls = ['execute_script', '//*[@class="tabLink" and text()="Product details"]','']
    run_subrule(driver, subls)

    #  CMR A1 A2 check
    col = 4
    subls = ['click', f'//input[@class="{lx[col]}" and @value="{ld[col]}"]','']
    run_subrule(driver, subls)

    # expand nanomaterials area
    col = 5
    subls = ['click', '//*[starts-with(@id,"accordion_")]/h3[2]','']
    run_subrule(driver, subls)

    # nanomaterials check
    subls = ['execute_script', f'//input[@class="{lx[col]}" and @value="{ld[col]}"]','']
    run_subrule(driver, subls)

    # expand category area
    subls = ['execute_script', '//*[starts-with(@id,"accordion_")]/h3[3]','']
    run_subrule(driver, subls)

    #cat1
    col = 6
    subls = ['click', f'//*[starts-with(@id,"{lx[col]}")]/option[contains(text(), "{ld[col]}")]','']
    run_subrule(driver, subls)

    #cat2
    col = 7
    subls = ['click', f'//*[starts-with(@id,"{lx[col]}")]/option[contains(text(), "{ld[col]}")]','']
    run_subrule(driver, subls)

    #cat3
    #wait for appearance
    col = 8
    subls = ['click', f'//*[starts-with(@id,"{lx[col]}")]/option[contains(text(), "{ld[col]}")]','']
    run_subrule(driver, subls)

    #Physical form  # "1">Solid/pressed powder  "2">Loose powder  "3">Cream / paste  "4">Liquid  "5">Foam  "6">Spray  "-2">Other
    col = 9
    subls = ['click', f'//*[starts-with(@id,"{lx[col]}")]/option[contains(text(), "{ld[col]}")]','']
    run_subrule(driver, subls)

    # specialPackaging
    col = 10
    subls = ['execute_script', f'//input[@class="{lx[col]}" and @value="{ld[col]}"]','']
    run_subrule(driver, subls)

    # Formulation name
    col = 11
    subls = ['click', f'//*[starts-with(@id,"{lx[col]}")]/option[contains(text(), "{ld[col]}")]','']
    run_subrule(driver, subls)

    # notification type
    subls = ['click', '//*[starts-with(@id,"notificationType_")]/option[contains(text(), "Exact concentrations")]','']
    run_subrule(driver, subls)

    #  add pH range min - cell 17  
    col = 17
    subls = ['input', f'//*[starts-with(@id,"{lx[col]}")]',ld[col]]
    run_subrule(driver, subls)

    #  add pH range  max - cell 18   
    col = 18
    subls = ['input', f'//*[starts-with(@id,"{lx[col]}")]',ld[col]]
    run_subrule(driver, subls)

    subls = ['execute_script', '//input[@class="fileFormula" and @value="Y"]','']
    run_subrule(driver, subls)

    driver.switch_to.alert.accept()
    #alertObj.accept()

    # -----------------------------------------------------------------------
    #                       SEMIAUTOMATED PRODUCT NOTIFIEING
    #                            SELECT FILES MANUALLY
    # -----------------------------------------------------------------------
    if menu_selection_result == '2':
        rep = input('Continue   y/n ?')
        if rep == 'n':
            sys.exit(0)
        elif rep == 'y':
            return()
    # -----------------------------------------------------------------------
    #                     Append ingredients fiile
    # -----------------------------------------------------------------------
    col = 14
    subls = ['input', f'//input[starts-with(@id,"formulaDoc_") and contains(@id,"{productID_part3}")]',ini_data.folder_ingredients+ld[col]]
    run_subrule(driver, subls)

    # -----------------------------------------------------------------------
    #                  Sticker and label append files
    # where : image + ext = ld[15]     sticker fname = ld[14]   
    # -----------------------------------------------------------------------
    # expand area
    subls = ['execute_script', '//*[starts-with(@id,"accordion_")]/h3[4]','']
    run_subrule(driver, subls)

    # -----------------------------------------------------
    #                add sticker image
    # -----------------------------------------------------
    # press add sticker file button
    subls = ['execute_script', f'//*[contains(@id,"{productID_part3}")]/fieldset[1]/div[1]/div[2]/button','']
    run_subrule(driver, subls)
    
    col = 15
    subls = ['input', f'//*[@id="document_1"]',ini_data.folder_sticker+ld[col]]
    run_subrule(driver, subls)

    # press save
    subls = ['execute_script', '//*[@id="addBtn"]','']
    run_subrule(driver, subls)
  
    # --------------------------------------------------------------
    #             press add packaging image file button  'url', 'click', 'input','execute_script'
    # --------------------------------------------------------------
    subls = ['execute_script', f'//*[contains(@id,"{productID_part3}")]/fieldset[2]/div[1]/div[2]/button','']
    run_subrule(driver, subls)

    col = 16
    subls = ['input', f'//*[@id="document_1"]',ini_data.folder_img +ld[col]]
    run_subrule(driver, subls)

    # press save
    subls = ['execute_script', '//*[@id="addBtn"]','']
    run_subrule(driver, subls)   

    # -----------------------------------------------------------------------------
    #                             NOTIFY PRODUCT
    # -----------------------------------------------------------------------------
    subls = ['execute_script', f'//*[@id="submitBtn"]','']
    run_subrule(driver, subls)

    print(f'------ PRODUCT NOTIFIED ----- \n name: {ld[2]} \n art: {ld[1]} \n ---------------------- ')
    print_break_prompt(6)

    return ()


def print_break_prompt(t):
    try:
        time_to_decide = t
        prompt = f'To break process press "y" + ENTER ({time_to_decide} sec to answer) \n'
        answer = input_with_timeout(prompt, time_to_decide)
    except TimeoutExpired:
        print(' process, will continue....')
    else:
        if answer == 'y':
            print ('bye.')
            sys.exit(0)
    return