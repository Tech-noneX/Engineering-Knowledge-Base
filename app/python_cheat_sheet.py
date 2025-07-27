import os
import random
from greetings_function import greetings
from md_paths import lists_methods_paths, lists_function_paths,dict_methods_paths, string_methods,built_in, modules, set_method


class PythonCheatSheet:


    def __init__(self):
        self.builtin_sheet = {'functions':{'min': built_in['min'],
                                           'max': built_in['max'],
                                           'len': built_in['len'],
                                           'sum': built_in['sum'],
                                           'range': built_in['range'],
                                           'reversed': built_in['reversed'],
                                           'round': built_in['round'],
                                           'enumerate': built_in['enumerate'],
                                           'print': built_in['print'],
                                           'type': built_in['type'],
                                           'input': built_in['input'],
                                           'zip': built_in['zip'],
                                           'map': built_in['map'],
                                           'filter': built_in['filter'],
        }}


        self.lists_sheet = {'functions & methods': {'append': lists_methods_paths['append'],
                                                    'extend': lists_methods_paths['extend'],
                                                    'sort': lists_methods_paths['sort'],
                                                    'sorted': lists_function_paths['sorted'],
                                                    'split': lists_methods_paths['split'],
                                                    'insert': lists_methods_paths['insert'],
                                                    'index': lists_methods_paths['index'],
                                                    'remove': lists_methods_paths['remove'],
                                                    'count': lists_methods_paths['count'],

                                                    }}
        
        
        self.string_sheet = {'functions & methods': {'upper': string_methods['upper'],
                                                      'lower': string_methods['lower'],
                                                      'title': string_methods['title'],
                                                      'lstrip': string_methods['lstrip'],
                                                      'rstrip': string_methods['rstrip'],
                                                      'strip': string_methods['strip'],
                                                      'removeprefix': string_methods['removeprefix'],
                                                      'removesuffix': string_methods['removesuffix'],
                                                      'replace': string_methods['replace'],
                                                      'capitalize': string_methods['capitalize'],
                                                      'join': string_methods['join'],
                                                      'find': string_methods['find'],

                                                    }}
        
        
        self.dict_sheet = {'functions & methods': {'get': dict_methods_paths['get']}}
        
        
        self.set_sheet = {'method': {'add': set_method['add'],
                          
                          }}
        

        self.modules_in = {'functools': {'reduce': modules['functools module']['reduce'],
                                         'functools': modules['functools module']['functools'],
                                        }}


        
    def main_menu(self):
        pass

    
    def functions_menu(self):
        while True:
            find_function = input(f"{random.choice(greetings)}\n:").lower().strip()
            if "q" == find_function:
                break
            if find_function in self.lists_sheet['functions & methods']:
                os.startfile(self.lists_sheet['functions & methods'][find_function])
                continue
            elif find_function in self.dict_sheet['functions & methods']:
                os.startfile(self.dict_sheet['functions & methods'][find_function])
                continue
            elif find_function in self.string_sheet['functions & methods']:
                os.startfile(self.string_sheet['functions & methods'][find_function])
                continue
            elif find_function in self.builtin_sheet['functions']:
                os.startfile(self.builtin_sheet['functions'][find_function])
                continue
            elif find_function in self.set_sheet['method']:
                os.startfile(self.set_sheet['method'][find_function])
                continue
            for modules,functions in self.modules_in.items():
                if find_function in functions:
                    os.startfile(self.modules_in[modules][find_function])
                    continue
            print("Function not found!")



pychsh = PythonCheatSheet()
pychsh.functions_menu()
