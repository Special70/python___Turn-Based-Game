from enum import Enum

from system.functions.boot_global_functions import tprint

class Menus(Enum):
    FRONT_MENU = 1

class SysStatus:
    def __init__(self):
        self.system_status = True
        self.current_menu = Menus.FRONT_MENU
# ==============================================================
    def isProgramRunning(self):
        return self.system_status
    def shutdownProgram(self):
        self.system_status = False
# ==============================================================
    def getCurrentMenu(self):
        return self.current_menu
    def setCurrentMenu(self, menu):
        if isinstance(menu, Menus):
            self.current_menu = menu
        else:
            tprint("")
# ==============================================================

# put class objects with the attribute function "setVal()".
# Multiple parts of the program may compete for information about the pressed key
# so this was developed to make an attempt in solving it
class Requests():
    keyhit_requests = []

keyhitRequest = Requests()

var = SysStatus()