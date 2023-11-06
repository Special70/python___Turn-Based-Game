import msvcrt
import threading

#Custom libraries
import textlib
import difficulty
import sys_settings
# Contains the following settings
# - Keybind Settings


#UI State
board_clearer = "\n"*30 #For pushing previous console output upwards
state_inputThread = True
state_mainThread = True #If this goes False, all loops will cease to work
state_userInput = ""

#Main Thread Start
print(board_clearer)
# ---------------------------------------------------------------------
def mainThread():
# ---------------------------------------------------------------------
    global board_clearer
    global state_inputThread
    global state_mainThread
    global state_userInput

    global keybinds
    global keybinds2
# --------------------------------------------------------------------
    mainFrame = True #Main loop that handles the entire system
    boardStatus001 = True
    while mainFrame and state_mainThread:
        boardStatus001 = True #Re-enables the main menu just in case any loops tries to go back to the main menu
        while boardStatus001 and state_mainThread:
            textlib.text_mainmenu()
            #Wait for the user to input something
            while True:
                if state_userInput == "e": #Exit
                    state_userInput = ""
                    boardStatus001 = False
                    state_inputThread = False
                    state_mainThread = False
                    break
                elif state_userInput == "p": #Play
                    print(board_clearer)
                    boardStatus001 = False
                    state_userInput = ""
                    break
                elif state_userInput == "s": #Settings
                    print(board_clearer)
                    state_userInput = ""
                    textlib.text_settingsMenu()
                    while True: #Settings Editor
                        if state_userInput == "k":
                            print(board_clearer)
                            state_userInput = ""

                            settingsFrame = True
                            while settingsFrame: #Settings: Keybinds
                                print(board_clearer)
                                print("""
----------------------
Keybind Editor:
Player1 Key1 [{a}] : "1"
Player1 Key2 [{b}] : "2"
Player1 Key3 [{c}] : "3"
Player2 Key1 [{d}] : "4"
Player2 Key2 [{e}] : "5"
Player2 Key3 [{f}] : "6"

Back: "b"
----------------------
""".format(a=sys_settings.keybinds[0],
           b=sys_settings.keybinds[1],
           c=sys_settings.keybinds[2],
           d=sys_settings.keybinds2[0],
           e=sys_settings.keybinds2[1],
           f=sys_settings.keybinds2[2]))
                                while True:
                                    if state_userInput == "1" or state_userInput == "2" or state_userInput == "3":
                                        selectedIndex = int(state_userInput)-1
                                        state_userInput = ""
                                        print(board_clearer)
                                        print("Hit a keybind to change the input")
                                        while True:
                                            if not state_userInput == "":
                                                sys_settings.keybinds[selectedIndex] = state_userInput.lower()
                                                state_userInput = ""
                                                break
                                        break
                                    elif state_userInput == "b":
                                        settingsFrame = False
                                        break
                                
                        elif state_userInput == "b":
                            print(board_clearer)
                            state_userInput = ""
                            textlib.text_mainmenu()
                            break
        # Game Selection
        textlib.text_selectGamemode()
        boardStatus002 = True
        while boardStatus002 and state_mainThread: # Select Difficulty
            if state_userInput == "c": #Computer
                print(board_clearer)
                state_userInput = ""
                textlib.text_selectDifficulty()
                while True:
                    if state_userInput == "b": #Back
                        state_userInput = ""
                        boardStatus002 = False
                        print(board_clearer)
                        break
                    elif state_userInput == "e":
                        continue

            elif state_userInput == "b": #Back
                print(board_clearer)
                boardStatus002 = False
                break
    print("[!] mainThread has ended [!]") #Debug Message
        
        
            
#Input Thread Start
# ---------------------------------------------------------------------
def inputThread():
# ---------------------------------------------------------------------
    global board_clearer
    global state_userInput
# ---------------------------------------------------------------------
    while state_inputThread:
        if msvcrt.kbhit():
            state_userInput = str(msvcrt.getch())[-2]
            print("Debug:",state_userInput) #Debug Message
    print("[!] inputThread has ended [!]") #Debug Message
# ---------------------------------------------------------------------










































mainThread = threading.Thread(target=mainThread)
inputThread = threading.Thread(target=inputThread)

mainThread.start()
inputThread.start()

mainThread.join()
inputThread.join()
