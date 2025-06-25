import os
import random
from pathlib import Path
append_path = Path(__file__).parent.parent / 'docs' / 'append.md'


greetings = ["Hello bro, enter function?","Whats up, mate, any function?",
             "Hey dude, function?","Bro, enter function?",
             "What function are you looking for?", "Looking for something?"
            ]
cheat_sheet = {'Functions': {'append': str(append_path)}}

find_function = input(f"{random.choice(greetings)}\n:")
if find_function in cheat_sheet['Functions']:
    os.startfile(cheat_sheet['Functions'][find_function])
else:
    print("Function not found!")



    