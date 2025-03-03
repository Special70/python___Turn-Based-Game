from pynput import keyboard

from system.functions.boot_global_functions import tprint
from core.program_variables import keyhitRequest

print("KEYHIT READER ACTIVATED")

def fillKeyhitRequests(char: str):
    #print(keyhitRequest.keyhit_requests)
    for obj in keyhitRequest.keyhit_requests:
        obj.setVal(char)
        del obj
    keyhitRequest.keyhit_requests.clear()

# ==============================================================
def on_press(key):
    try:
        #tprint(key.char)
        fillKeyhitRequests(key.char)
    except AttributeError:
        #tprint('special key {0} pressed'.format(key))
        pass
def on_release(key):
    #tprint('{0} released'.format(key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)

# ==============================================================