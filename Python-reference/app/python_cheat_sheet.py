import os
import random
from greetings_function import greetings
from md_paths import (lists_methods_paths, datatypes_paths,
             lists_function_paths, dict_methods_paths,
             string_methods, built_in, set_method,
             modules, PYTHON_DOCS,
                     )


class PythonCheatSheet:


    def __init__(self):

        self.datatypes_sheet = {'list': datatypes_paths['list'],
                                'bool': datatypes_paths['bool'],
                                'dict': datatypes_paths['dict'],
                                'float': datatypes_paths['float'],
                                'int': datatypes_paths['int'],
                                'set': datatypes_paths['set'],
                                'str': datatypes_paths['str'],
                                'tuple': datatypes_paths['tuple'],
        }


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
                                                    'insert': lists_methods_paths['insert'],
                                                    'index': lists_methods_paths['index'],
                                                    'remove': lists_methods_paths['remove'],
                                                    'count': lists_methods_paths['count'],
                                                    'reverse': lists_methods_paths['reverse'],
                                                    'pop': lists_methods_paths['pop'],

                                                    }}
        
        
        self.string_sheet = {'functions & methods': {'upper': string_methods['upper'],
                                                      'split': string_methods['split'],
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
                                                      'partition': string_methods['partition'],
                                                      'endswith': string_methods['endswith'],
                                                      'format': string_methods['format'],

                                                    }}
        
        
        self.dict_sheet = {'functions & methods': {'get': dict_methods_paths['get']}}
        
        
        self.set_sheet = {'method': {'add': set_method['add'],
                                     'union': set_method['union'],
                          
                          }}
        

        self.modules_in = {'functools': {'reduce': modules['functools module']['reduce'],
                                         'functools': modules['functools module']['functools'],
                                        }}

        self.menu_categories = {
            '1': ('BUILT-IN FUNCTIONS', self.builtin_sheet['functions']),
            '2': ('DATA TYPES', self.datatypes_sheet),
            '3': ('LIST FUNCTIONS & METHODS', self.lists_sheet['functions & methods']),
            '4': ('STRING METHODS', self.string_sheet['functions & methods']),
            '5': ('DICTIONARY METHODS', self.dict_sheet['functions & methods']),
            '6': ('SET METHODS', self.set_sheet['method']),
            '7': ('MODULES', {
                name: path
                for module in self.modules_in.values()
                for name, path in module.items()
            }),
        }


    def display_menu(self, title, menu_lines):
        menu_width = 60

        print("+" + "-" * (menu_width - 2) + "+")
        print("|" + title.center(menu_width - 2) + "|")
        print("+" + "-" * (menu_width - 2) + "+")
        for line in menu_lines:
            print(f"|  {line}".ljust(menu_width - 1) + "|")
        print("+" + "-" * (menu_width - 2) + "+\n")


    def main_menu(self):
        card_count = sum(1 for _ in PYTHON_DOCS.rglob("*.md"))

        while True:
            self.display_menu("PYTHON REFERENCE BROWSER", [
                f"{card_count} reference cards available",
                "",
                "1  Built-in functions",
                "2  Data types",
                "3  List functions and methods",
                "4  String methods",
                "5  Dictionary methods",
                "6  Set methods",
                "7  Modules",
                "",
                "s  Search all cards",
                "q  Quit",
            ])

            menu_choice = input("Choose a menu: ").lower().strip()

            if menu_choice == "q":
                break
            if menu_choice == "s":
                self.functions_menu()
                continue
            if menu_choice in self.menu_categories:
                title, cards = self.menu_categories[menu_choice]
                self.category_menu(title, cards)
                continue
            print("Menu option not found. Choose 1-7, s or q.\n")


    def category_menu(self, title, cards):
        card_names = sorted(cards)
        menu_lines = [f"{len(card_names)} cards available", ""]

        for index in range(0, len(card_names), 3):
            row = "".join(
                f"{name:<17}" for name in card_names[index:index + 3]
            ).rstrip()
            menu_lines.append(row)

        menu_lines.extend([
            "",
            "Type a listed name to open its card.",
            "b  Back to main menu",
        ])
        self.display_menu(title, menu_lines)

        while True:
            card_choice = input("Choose a card: ").lower().strip()

            if card_choice == "b":
                break
            if card_choice in cards:
                os.startfile(cards[card_choice])
                print(f"Opened: {card_choice}\n")
                continue
            print("Card not found. Choose a listed name or enter b.\n")

    
    def functions_menu(self):
        self.display_menu("SEARCH ALL CARDS", [
            "Search examples: append, enumerate, list, dict, reduce",
            "",
            "help  Show available topics",
            "b     Back to main menu",
        ])

        while True:
            find_function = input(f"{random.choice(greetings)}\nSearch: ").lower().strip()
            if "b" == find_function:
                break
            if "help" == find_function:
                print("Available topics: built-ins, data types, dictionaries, "
                      "lists, modules, sets and strings.\n")
                continue
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
            elif find_function in self.datatypes_sheet:
                os.startfile(self.datatypes_sheet[find_function])
                continue
            module_found = False
            for modules, functions in self.modules_in.items():
                if find_function in functions:
                    os.startfile(self.modules_in[modules][find_function])
                    module_found = True
                    break
            if module_found:
                continue
            print("Function not found!")



if __name__ == "__main__":
    pychsh = PythonCheatSheet()
    pychsh.main_menu()
