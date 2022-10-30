# import only system from os 
from os import system, name 
# import sleep to show output for some time period 
from time import sleep 
import sys



def run_menu():

    s = ("************MAIN MENU**************")
    menu= { "1": "only login and open cpnp page",
            "2": "add notification script semiautomated",
            "3": "add notification script",
            "4": "dublicate notification script",
            "q": "Quit/Log Out"
    }
    for k, v in menu.items():
        s = s + '\n' + '\t {k} : {v}'.format(k=k,v=v)
    s = s + '\nPlease enter your choice: '
    choice = input(s)
    if choice in menu:
        return(choice)
    elif choice.upper()=="Q":
        sys.exit()
    else:
        print("You must only select number from menu")
        print("Please try again")
        run_menu()



# define our clear function 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 