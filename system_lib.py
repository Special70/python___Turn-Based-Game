import stats

# Core system
currentKey = "" # Stores key press for func usage
programStatus = True
disableKeyListener = True # For the keyListener() to stop resetting the key while editing the keybind

editorMode = False

currentMenu = 1 # Dictates where the program would go once the said menu ends
# Program's Loop Status
mainMenuLoop1_settings_keybindEditor = True

gamemode = ""

turnNumber = 1 # Decides who's taking the turn
turnIdentifier = stats.player01