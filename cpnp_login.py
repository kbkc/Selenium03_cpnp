from funcs import *
from add_product_codes import *
import time
import sys

config_ffn = 'config/datas.xlsx'
config_sheet_login = 'login'
config_sheet_add = 'prod_add_init'
task_ffn = 'task01/sbor.xlsx'
task_sheet_data = 'datas'
img_folder = 'task01/'
sticker_folder = 'task01/'
data_range_start = 2
#task_sheet_data_files = 'flist'



cfgs = read_settings(config_ffn , config_sheet_login)
ltask = read_settings(task_ffn , task_sheet_data)
#ltaskfiles = read_settings(task_ffn , task_sheet_data_files)

driver = open_url(cfgs[0][2])


##################################################
# data for connect to session from other scripts #
url = driver.command_executor._url
session_id = driver.session_id
#print('url = \n', url,'\n sess id = \n',session_id)
print(f'\n\t\t===\nurl = \'{url.strip()}\'\nsession_id = \'{session_id.strip()}\' \n \t\t===\n')
##################################################

# login to site
for i in range (1, len(cfgs)):
    run_rule(driver,cfgs[i])
exit(0)
