import os
import random
from pathlib import Path
from greetings_function import greetings
from md_paths import function_paths


class PythonCheatSheet:


    def __init__(self):
        self.cheat_sheet = {'Functions': {'append': function_paths['append']}}


    def functions_menu(self):
        find_function = input(f"{random.choice(greetings)}\n:")
        if find_function in self.cheat_sheet['Functions']:
            os.startfile(self.cheat_sheet['Functions'][find_function])
        else:
            print("Function not found!")



pychsh = PythonCheatSheet()
pychsh.functions_menu()