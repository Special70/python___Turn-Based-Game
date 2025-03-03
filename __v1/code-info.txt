run main.py to run the entire thing

Code Explanations:
main.py: Heart of the code. Runs the major functions in it
func_lib.py: Stores majority of the major functions
locale_EN.py: Stores majority of the words/sentences that appear from the code
settings.py: Stores keybinds
stats.py: Stores Player classes and more
system_lib.py: Hosts the important variables that are used across py files

custom_mechanics/effects.py: Stores custom functions related to status effects and cooldowns
custom_mechanics/skills.py: Stores skill classes that will be used later at gamemodes/multiplayer.py

gamemodes/multiplayer.py: Hosts both the singleplayer and the multiplayer session
computer_opponent: Hosts the functions that gives the opponent randomly selected skills and have it randomly execute skills considering the current energy points the opponent has