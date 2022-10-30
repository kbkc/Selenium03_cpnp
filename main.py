from funcs import *
from add_product_codes import *
import time
import sys
from menu import *

class ini_data :
        task_folder = 'task04'
        task_path = 'C:/Users/mposo/Documents/MEGAsync/_Dev/_Python/Selenium03_cpnp/'+task_folder+'/'

        ffn_config = 'config/datas.xlsx'
        sheet_config_login = 'login'
        sheet_config_add = 'prod_add_init'
        sheet_config_dbl = 'prod_dbl_init'
        ffn_task = task_path + '/sbor.xlsx'
        sheet_task_data = 'datas'
        sheet_task_data_dublicate = 'datas_dbl'
        folder_img = task_path + 'img_product/'
        folder_sticker = task_path + 'img_sticker/'
        folder_ingredients = task_path + 'img_ing/'
        data_range_start_row = 2
        #table_name = 'prod_table'
        #cpnp_prod_name = 'ReformA / Gel Polish Aphrodisiac'


#task_sheet_data_files = 'flist'

def main():
        cfgs = read_settings(ini_data.ffn_config , ini_data.sheet_config_login)

        #work with tables. sample finction.
        #ltask = read_product_table(task_ffn , task_sheet_data, table_name)

        menu_selection_result = run_menu()

        driver = open_url(cfgs[0][2])

        show_data_connect_info(driver)

        if menu_selection_result=='1':
                print(f'i = {menu_selection_result}')

                # login to site
                for i in range (1, len(cfgs)):
                        run_rule(driver,cfgs[i])
                if input('"q" to exit : ').upper()=="Q":
                        sys.exit
        elif menu_selection_result=='2' or menu_selection_result=='3':
                ltask = read_settings(ini_data.ffn_task , ini_data.sheet_task_data)
                # login to site
                for i in range (1, len(cfgs)):
                        run_rule(driver,cfgs[i])
                print(f'i = {i}')

                # goto notify new product (add_new_product press button)
                add_prod_init = read_settings(ini_data.ffn_config, ini_data.sheet_config_add)
                #for i in range (0, len(add_prod_init)):
                #      run_rule(driver,add_prod_init[i])
                # add product
                for lt in ltask:
                        if ltask.index(lt) > ini_data.data_range_start_row:
                                # -------------------------------------
                                #         notify new product
                                # -------------------------------------
                                for i in range (0, len(add_prod_init)):
                                        run_rule(driver,add_prod_init[i])
                                # ----- end notify new product ---------

                                # ltask[2] - second line of table is a list of xPath names 
                                # lt - list of datas (name, sku ....)
                                run_rule_add_product(driver, ltask[2],lt,ini_data, menu_selection_result)               
        elif menu_selection_result=='4':
                ltask = read_settings(ini_data.ffn_task , ini_data.sheet_task_data_dublicate)
                # login to site
                for i in range (1, len(cfgs)):
                       pass
                       run_rule(driver,cfgs[i])
                print(f'i = {i}')
                # goto dublicate product (add_new_product press button)

                dbl_prod_init = read_settings(ini_data.ffn_config, ini_data.sheet_config_dbl)
                for lt in ltask:
                        if ltask.index(lt) > ini_data.data_range_start_row:
                                print(f'lt[19] = {lt[19]}')
                                run_rule_dublicate_product(driver, lt[19],dbl_prod_init)
                                run_rule_change_product(driver, ltask[2],lt,ini_data, menu_selection_result)
                                
                #if input('"q" to exit : ').upper()=="Q":
                #        sys.exit
        #exit(0)
        #time.sleep(3)
        #close_driver(driver)
        print('bye')
        #exit(0)



main()