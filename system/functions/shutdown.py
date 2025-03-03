from pynput import keyboard
def shutdown():
    """Run this to terminate the program and its other processes"""
    keyboard.Listener.stop()