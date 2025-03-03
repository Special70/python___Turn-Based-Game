import os
from time import sleep

from system.functions.boot_global_functions import tprint
from core.program_variables import keyhitRequest

class FrontMenuKeyhitRequest():
    def __init__(self):
        self.val = ""
    def setVal(self, char: str):
        self.val = char
    def getVal(self):
        return self.val

front_menu = '''
Welcome to the turn-based-game python game!
Use keyboard inputs to interact!

[1] Select Game
[2] Settings
[3] Exit
'''

def boot():
    print("BOOTED FRONT MENU")
    
    while True:
        keyhit = FrontMenuKeyhitRequest()
        keyhitRequest.keyhit_requests.append(keyhit)
        while len(keyhit.getVal()) == 0:
            sleep(0.1)
            pass
        print(keyhit.getVal(), end='', flush=True)
boot()

print("succ")