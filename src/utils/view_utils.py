import os
from colorama import Fore, Style 
import time


class ViewUtils:
    
    @staticmethod
    def display_error(error):
        ViewUtils.console_clean()
        print(f"{Style.BRIGHT}{Fore.RED}{error}{Style.RESET_ALL}")
        time.sleep(1)
        ViewUtils.console_clean()

    
    @staticmethod
    def console_clean():
        os.system('cls' if os.name=='nt' else 'clear')
        
    @staticmethod
    def display_menu_prompt(back_func):
        while True:
            choice = input(f"{Fore.YELLOW}Pressione 'b' para voltar ao Menu: {Style.RESET_ALL}")
            if choice.lower() == "b":
                os.system('cls' if os.name=='nt' else 'clear')
                back_func()
                break