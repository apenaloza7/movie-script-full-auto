import pyautogui
import time

# ----------------------------------------------------------------------------------------
# Program that spams someone with a movie script word for word using the pyautogui library
#
# Author: Alejandro Penaloza and the Internet
#
# Last updated May 14, 2020
#
# STEPS:
# 1. OPEN WINDOW WHERE U WISH TO SEND THE MESSAGES
# 2. RUN THE PROGRAM AND THEN CLICK THE MESSAGE BOX
# 3. SIT BACK AND RELAX
# ----------------------------------------------------------------------------------------


""" Rapid fires the movie script """
def fireCannon(scriptBeingUsed):

    # Reads the given movie script and assigns it to the script variable
    with open(scriptBeingUsed, "r") as file:
        content = file.read()

    script = content

    for x in script.split():
        pyautogui.write(x)
        pyautogui.press("enter")


""" Launches the program """
def run():

    # Change this variable to the movie script of your choice
    movieScript = "zuckerberg.txt"

    print("Warming up....")

    # allows you time to get to your message window
    time.sleep(7)

    fireCannon(movieScript)

# LAUNCH!
run()
