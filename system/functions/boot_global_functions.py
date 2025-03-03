import system.functions.boot_read_config as cfig

def tprint(*args, **kwargs):
    """Prints only if debug_mode is true in server/functions/config.properties"""
    if cfig.configs.get("debug_mode").data == "true":
        print(*args, **kwargs)

tprint("DEBUG MODE ENABLED")
