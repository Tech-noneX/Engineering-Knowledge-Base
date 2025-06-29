import os
import random
from greetings_function import greetings
from md_paths import lists_methods_paths, lists_function_paths,dict_methods_paths, string_methods


class PythonCheatSheet:


    def __init__(self):
        self.lists_sheet = {'functions & methods': {'append': lists_methods_paths['append'],
                                                    'extend': lists_methods_paths['extend'],
                                                    'sort': lists_methods_paths['sort'],
                                                    'sorted': lists_function_paths['sorted'],
                                                    'split': lists_methods_paths['split'],
                                                    'insert': lists_methods_paths['insert'],
                                                    'index': lists_methods_paths['index'],
                                                    'upper': string_methods['upper'],
                                                    'lower': string_methods['lower'],
                                                    'title': string_methods['title'],
                                                    'lstrip': string_methods['lstrip'],
                                                    'rstrip': string_methods['rstrip'],

                                                    }}
        self.string_sheet = {'functions & methods': {'upper': string_methods['upper'],
                                                      'lower': string_methods['lower'],
                                                      'title': string_methods['title'],
                                                      'lstrip': string_methods['lstrip'],
                                                      'rstrip': string_methods['rstrip'],
                                                      'strip': string_methods['strip'],
                                                      'removeprefix': string_methods['removeprefix'],
                                                      'removesuffix': string_methods['removesuffix'],
                                                    }}
        self.dict_sheet = {'functions & methods': {'get': dict_methods_paths['get']}}

    def main_menu(self):
        pass

    
    def functions_menu(self):
        find_function = input(f"{random.choice(greetings)}\n:").lower().strip()
        if find_function in self.lists_sheet['functions & methods']:
            os.startfile(self.lists_sheet['functions & methods'][find_function])

        if find_function in self.dict_sheet['functions & methods']:
            os.startfile(self.dict_sheet['functions & methods'][find_function])
        
        if find_function in self.string_sheet['functions & methods']:
            os.startfile(self.string_sheet['functions & methods'][find_function])
        
        else:
            print("Function not found!")



pychsh = PythonCheatSheet()
pychsh.functions_menu()
