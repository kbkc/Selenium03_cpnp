
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from funcs import *
from main  import task_folder
from add_product_codes import *
import sys


config_ffn = 'config/datas.xlsx'
config_sheet_login = 'login'
config_sheet_add = 'prod_add_init'
task_ffn = task_folder + '/sbor.xlsx'
task_sheet_data = 'datas'
img_folder = task_folder + '/'
sticker_folder = task_folder + '/'
data_range_start = 2

#url = 'http://127.0.0.1:49640'
#session_id = '7ba4d4e4c6cff21217ed799bedaca934'

def main():
    ltask = read_settings(task_ffn , task_sheet_data)

    d = read_session_data()

    driver = webdriver.Remote(command_executor=d['url'],desired_capabilities={})
    driver.session_id = d['id']
    #driver.manage().window().minimize()


    # goto notify new product (add_new_product press button)
    print('\nNotify new product...')
    add_prod_init = read_settings(config_ffn, config_sheet_add)
    for i in range (0, len(add_prod_init)):
        run_rule(driver,add_prod_init[i])


    # 3,
    print('\nRun rule add product...')
    run_rule_add_product(driver, ltask[2],ltask[18])
    driver.close()






main()
