import threading
from time import sleep

# boot the basic system features first
def boot_system_features():
    from system.functions import boot_read_config
    from system.functions import boot_global_functions
# then boot the listeners
def boot_keyhit():
    from system.listeners import keyhit
# and boot the actual program now
def boot_program():
    print("BOOTING PROGRAM")
    from system.functions import boot_start_program
    print("PROGRAM CLOSED")


# create threads
t1 = threading.Thread(target=boot_system_features)
t2 = threading.Thread(target=boot_keyhit)
t3 = threading.Thread(target=boot_program)

t1.start()
print("BOOTING STAGE 1")
t1.join()
print("DONE BOOTING STAGE 1")
print("BOOTING STAGE 2")
t2.start()
print("DONE BOOTING STAGE 2")
print("BOOTING STAGE 3")
t3.start()
print("DONE BOOTING STAGE 3")

t2.join()
t3.join()