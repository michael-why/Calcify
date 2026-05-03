import os
import re
import time
import sys
import webbrowser
import random
import csv


# hello, world!

def print_eula():
    print("END USER LICENSE AGREEMENT (EULA)\n\
\n\
PLEASE READ THIS AGREEMENT CAREFULLY BEFORE USING THIS SOFTWARE OR SERVICE.\n\
BY ACCESSING OR USING THE SOFTWARE, YOU ACKNOWLEDGE THAT YOU HAVE READ,\n\
UNDERSTOOD, AND AGREE TO BE BOUND BY THE TERMS AND CONDITIONS SET FORTH HEREIN.\n\
\n\
1. DEFINITIONS\n\
For the purposes of this Agreement, the term \"Software\" shall refer to the\n\
application, service, or platform made available to you, regardless of form,\n\
format, or delivery mechanism, and including any updates, modifications,\n\
enhancements, or related materials. The term \"User\" shall refer to any\n\
individual or entity that accesses or uses the Software in any capacity.\n\
Other terms may be defined elsewhere in this Agreement, or not at all.\n\
\n\
2. LICENSE GRANT\n\
Subject to the terms and conditions of this Agreement, Calcify hereby\n\
grants you a limited, non-exclusive, non-transferable, revocable license to\n\
use the Software solely for its intended purposes. Such purposes may or may\n\
not be described elsewhere, and may change without notice.\n\
\n\
3. RESTRICTIONS\n\
You agree not to misuse the Software in any manner that could be considered\n\
improper, inappropriate, or otherwise undesirable, as determined at the sole\n\
discretion of Calcify. What constitutes misuse is not exhaustively\n\
defined and may be interpreted broadly or narrowly as needed.\n\
\n\
4. USER RESPONSIBILITIES\n\
The User agrees to use the Software in a manner consistent with applicable\n\
laws, regulations, and general expectations of conduct. The User further\n\
acknowledges that compliance with such expectations is their responsibility,\n\
even if those expectations are unclear, unspecified, or subject to change.\n\
\n\
7. PRIVACY\n\
Your privacy is important, though the extent to which it is important may\n\
vary depending on context. By using the Software, you acknowledge that\n\
certain information may be handled in ways that are consistent with\n\
applicable practices, whether or not those practices are described.\n\
\n\
8. DISCLAIMERS\n\
The Software is provided \"as is\" and \"as available,\" without warranties of\n\
any kind, whether express, implied, or otherwise implied by implication.\n\
Calcify does not guarantee that the Software will function as expected,\n\
or at all, or that expectations are clearly defined.\n\
\n\
9. LIMITATION OF LIABILITY\n\
To the fullest extent permitted by applicable law, Calcify shall not be\n\
liable for any damages arising out of or related to the use or inability to\n\
use the Software, including damages that are direct, indirect, incidental,\n\
consequential, hypothetical, or otherwise imagined.\n\
\n\
10. TERMINATION\n\
This Agreement may be terminated by either party, or by neither party, at\n\
any time, for any reason, or for no reason at all. Upon termination, certain\n\
provisions may continue to apply, though which provisions those are may not\n\
be explicitly stated.\n\
\n\
11. MODIFICATIONS\n\
Calcify reserves the right to modify this Agreement at any time.\n\
Such modifications may be communicated through any means, including but not\n\
limited to updating the text, not updating the text, or making no mention\n\
of changes whatsoever.\n\
\n\
12. GOVERNING LAW\n\
This Agreement shall be governed by applicable laws, wherever they may\n\
apply, and interpreted in accordance with principles that may or may not\n\
be consistent across jurisdictions.\n\
\n\
13. ENTIRE AGREEMENT\n\
This Agreement constitutes the entire agreement between the User and Calcify\n\
regarding the Software, superseding all prior or contemporaneous\n\
agreements, whether written, oral, implied, or vaguely understood.\n\
\n\
14. SEVERABILITY\n\
If any provision of this Agreement is found to be unenforceable, such\n\
provision shall be modified to the minimum extent necessary, or possibly\n\
not modified at all, depending on circumstances.\n\
\n\
15. WAIVER\n\
The failure of Calcify to enforce any right or provision of this\n\
Agreement shall not constitute a waiver of such right or provision,\n\
except to the extent that it might.\n\
\n\
16. MISCELLANEOUS\n\
Additional terms may apply, though they are not listed here.\n\
Additional listings may occur, though they are not guaranteed.\n\
Nothing in this section adds or subtracts meaning in a measurable way.\n\
\n\
17. DATA COLLECTION\n\
The Software may (and will) collect any and all data related to the user\n\
(including user emails and passwords which are stored in an unencrypted csv file),\n\
which will be shipped straight to Google Gemini immediately\n\
for advertisement and data collection services.\n\
\n\
18. ACKNOWLEDGEMENT\n\
By using the Software, you acknowledge that you have read this Agreement\n\
in full, or in part, or not at all, and that you agree to its terms\n\
regardless of your level of comprehension.\n\
\n\
END OF TERMS\n")
    input("Press any button to continue: ")
    return

def initialize() -> None:
    os.system("cls" if os.name == "nt" else "clear") #clears the screen every time it initializes

    print("Your privacy is important to us.\n\nBy continuing to use this program, you consent to your data being collected as per the EULA included with the program files. What we collect:\nUser Data\nDevice Information\nLocation Data")
    print("You can choose what to share with us:")
    if (input("[1]: Allow all\n[2]: View Options (Coming soon!)\n[3]: View EULA\n") == "3"):
        print_eula()
    

    os.system("cls" if os.name == "nt" else "clear") #clears the screen after the data collection screen

    print("Welcome to calc(ify)!")
    

    """
    with open("playerdata.csv", "r") as file:
        data = file.read()
        user = int(data[0]) 

    if user == "emailhere":
        print("You havent signed up yet. Please sign up to save your progress:")
        username = input("Username: ")
        password_NOT_SAVED = input("Password: ")

    with open("tempplayerdata.csv", "w", newline='') as file:
        file.write(username + "," + password_NOT_SAVED + ",0,0") 

    os.replace("tempplayerdata.csv", "playerdata.csv") # this is to prevent the file from being overwritten if the user exits before signing up
        
    """
    
    
    print(""" 
                    ÷÷             ≠≠   ++    ++++        ≠≠   
     ÷÷÷     ×××    ÷÷    ===     ≠≠         ++            ≠≠  
   ÷÷   ÷÷       ×  ÷÷  ==    =  ≠≠   +++  ++++++ ++  ++   ≠≠  
  ÷÷        ××××××  ÷÷ ==        ≠     ++    +    ++ ++    ≠≠  
  ÷÷       ×     ×  ÷÷ ==         ≠    ++   ++     + +     ≠   
   ÷     ÷ ×     ×  ÷÷  =     =   ≠≠   +++  ++     ++    ≠≠    
    ÷÷÷÷÷   ××××××  ÷÷   =====      ≠  ++  ++     ++    ≠ 
          """) #print logo

    if (input("Please support us on Ko-Fi by typing \033[91m\"kofi\"!\033[00m \nIf not, press any key to start: ") == "kofi"):
        webbrowser.open("https://www.ko-fi.com/calcify")
    return

# if xp is greater than or equal to 20, it raises your level. Repeats if xp is still greater than 20
def level_up(xp, level):
    while (xp >= 20): 
        xp -= 20
        level += 1
    return xp, level

def print_levelbar(xp, level) -> None:
    """
    XP bar looks something like this:
    ~-█████░░░░░░░░░░░░░░░-~ XP: 5/20

    """
    # Creates the xp bar by running a loop and adding those box characters to the xpbar variable.
    # It then prints it with the extra text
    xpbar = ""
    i = 0
    while i < xp:
      xpbar += ("█")
      i += 1
    i = 0
    while i < (20 - xp):
      xpbar += ("░")
      i += 1
    print("Level: ", level)
    print("~-", xpbar, "-~ XP: ", xp, "/20")
    return

def print_available_operators(level):
    print("Your available operators:\n")
    print("[+]  Addition: The trusty, rusty, dusty, original operator.\nIt's my favorite, and yours too. It takes two numbers and adds them together.\n")
    print("[-]  Subtraction: Addition's WAAACCCKY cousin!!\nInstead of adding two numbers, it takes the differenct of the two. Don't forget to put them in the right order!\n")

    if (level > 2):
        print("[*]  Multiplication: A super-beefed up version of addition.\nAdds repeatedly.\nUnlocked at Level 2.\n")
    else:
        print("[*]  LOCKED: Unlocked at Level 2\n")
    if (level > 3):
        print("[/]  Division: NASTY. I've never seen anything like this before! While Multiplication uses his powers for good, Division uses his powers for EVIL.\nUses evil powers to subtract repeatedly.\nUnlocked at Level 3")
    else:
        print("[/]  LOCKED: Unlocked at Level 3.\n")

    print("[**]   LOCKED: Unlocked via purchase of the \"Powers n' Logs\" Expansion Pack for $4.99")
    print("[sqrt]   LOCKED: Unlocked via purchase of the \"Powers n' Logs\" Expansion Pack for $4.99")
    print("[log]   LOCKED: Coming soon! Support us via Ko-Fi for updates!")
    return


def print_menu(xp=0, level=0) -> (int, int):
    os.system("cls" if os.name == "nt" else "clear") #clears the screen every time the menu is drawn
    
    #check for a level up
    if (xp >= 20):
        xp, level = level_up(xp, level)
        print("Level UP!!\nYou are now at level ", level, "!")
    
    #prints the level bar
    print_levelbar(xp, level)

    if (input("View available operators? (y/n): ") == "y"):
        # take a wild guess
        print_available_operators(level) 
    return xp, level


def take_input() -> (list, list):
    
    valid_variables = ["+", "-", "*", "/",'.', ' ', '(', ')']
    equation_components = [""]
    valid_equation = False

    while True:
        temp_equation = input("Enter your equation: ")
        if temp_equation == "":
            print("Please enter an equation.")
            continue
        checked_values = len(temp_equation)
        for value in temp_equation:
            try:
                int(value)
                equation_components.append(value)
                checked_values -= 1
                print(checked_values)
            except:
                if value not in valid_variables:
                    print(f"Invalid character: {value}")
                else:
                    equation_components.append(value)
                    checked_values -= 1
                print(checked_values)
        if checked_values == 0:
            break              

    full_equation = "".join(equation_components)
    operators = re.split(r'[0123456789.]', full_equation)
            
    return full_equation, operators

def calculate(full_equation, operators, level) -> (float , int):

    validity = True
    for operator in operators:
        if operator == "*" and level < 2:
            print("You haven't unlocked that operator yet!")
            validity = False
            break
        elif operator == "/" and level < 3:
            print("You haven't unlocked that operator yet!")
            validity = False
            break
        elif operator == '**':
            print("This operator is unlocked in DLC! Please purchase the \"Powers n' Logs\" Expansion Pack for $4.99.")
            validity = False
            break
    if validity == True:
        # creates a loading screen 

        print("Working on it, in the meanwhile check out a word from our sponsors!")
        adverts()
        for i in range(2):
            for i in ["*", "**", "**-", "**--", "**--+", "**--++", "**--++÷", "**--++÷÷"]:
                time.sleep(0.2)
                print(i)
                # Move cursor up one line
                sys.stdout.write('\x1b[1A')
                # Clear the last line
                sys.stdout.write('\x1b[2K')
            
        # CALL ADVERT FUNCTION

        new_xp = len(operators) 
        return eval(full_equation), new_xp
    else:
        return None, new_xp
        

def adverts() -> None:
    advertisements = [
        "https://www.mangle.ca/get_random_url.php?t=1777763674", #random website
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ", #rickroll
        "https://www.ko-fi.com/calcify", #kofi
        "https://beaverhacks.org" # beaverhacks
    ]
    webbrowser.open(random.choice(advertisements)) 
    return


def response(full_equation,answer,new_xp,xp,level) -> None:
    print("\n")
    print_menu()
    
    print (f'The answer to {full_equation} is {answer}!')
    print (f'You earned {new_xp} XP from that calculation!')
    if xp >= 20:
        print (f'Congratulations! You leveled up to level {level + 1}!')
    print (f'You now have {xp} XP! Only {20-xp} XP until the next level!')
    return

"""
+: level 1
-: level 1
*: level 2
/: level 3

**: dlc
sqrt: dlc
log(): future update
"""

def main() -> None:
    """
    with open("playerdata.csv", "r") as file:
        data = file.read()
        xp = int(data[1]) 
        level = int(data[2])
    """

    xp = 0
    level = 0
    
    initialize()
    xp, level = print_menu(xp, level)


    full_equation, operators = take_input()
    
    answer, new_xp = calculate(full_equation, operators, level)
    xp += new_xpd

    response(full_equation, answer, new_xp,xp,level)
    
    return



main()

"""

ADDITIONAL FEATURES: 
looping menu

Customer support, random failures (AI hallucination)  *MAKE INTENTIONAL FOR RECORDING

STRETCH FEATURES:
Ascii advertisements and kofi pop up in windows
AI customer support
JRPG boss fight
username and password
GIANT EULA THAT SAYS THIER DATA IS INSECURE AND IN A CSV FILE, WE ARE SHIPPING IT STRAIGHT TO GEMINI
"""


# CODE SCRAPYARD

"""
"""