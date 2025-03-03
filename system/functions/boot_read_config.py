from jproperties import Properties 

print("booted")
configs = Properties() 
with open('system/functions/config.properties', 'rb') as read_prop: 
    configs.load(read_prop) 

