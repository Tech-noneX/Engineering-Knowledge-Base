import os
import random
from greetings_function import greetings
from md_paths import methods_paths, function_paths


class PythonCheatSheet:


    def __init__(self):
        self.cheat_sheet = {'functions & methods': {'append': methods_paths['append'],
                                                    'extend': methods_paths['extend'],
                                                    'sort': methods_paths['sort'],
                                                    'sorted': function_paths['sorted'],
                                                    'split': methods_paths['split'],
                                                    'insert': methods_paths['insert'],
                                                    'index': methods_paths['index'],
                                          }
                                          }


    def main_menu(self):
        pass

    
    def functions_menu(self):
        find_function = input(f"{random.choice(greetings)}\n:")
        if find_function in self.cheat_sheet['functions & methods']:
            os.startfile(self.cheat_sheet['functions & methods'][find_function])
        else:
            print("Function not found!")



pychsh = PythonCheatSheet()
pychsh.functions_menu()