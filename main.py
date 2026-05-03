# Calc(ify) and Calc(AI) are subject to copyright of Calc(ify) LLC.
# Filename: main.py
# Authors: Michael Yohannes and Jason Miller
# Date: 3 May 2026
import os
import re
import time
import sys
import webbrowser
import random
import csv
import math

from bonus_feat.support import supportInit
from bonus_feat.support import print_typed
from bonus_feat.adverts_and_ai import load_internet_ad
from bonus_feat.adverts_and_ai import load_ai_output

from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent / "userdata.csv"

# hello, world!

def initialize() -> None:
    os.system("cls" if os.name == "nt" else "clear") #clears the screen every time it initializes

    print("Your privacy is important to us.\n\nBy continuing to use this program, you consent to your data being collected as per the EULA included with the program files. What we collect:\nUser Data\nDevice Information\nLocation Data")
    print("You can choose what to share with us:")
    if (input("[1]: Allow all\n[2]: View Options (Coming soon!)\n[3]: View EULA\n") == "3"):
        print_eula()
    

    os.system("cls" if os.name == "nt" else "clear") #clears the screen after the data collection screen

    print("Welcome to calc(ify): the AI-powered calculator of tomorrow.")

    print("""                                                                          
                                               ×   ÷÷                       ×       
                         =÷=                ×××π  ÷××÷     ××××××           ××≈     
                         =÷=              √××             ××                 ××π    
      ≈≈≈≈≈     ∞∞∞∞∞    =÷=    ≈≈≈≈≈    ÷××    ××××    ×××××××× ××     ××    ××    
    ≈≈≈    ≈≈  √     ∞∞  =÷=  ≈≈∞   ≈≈≈  ××       ××      ××     ××    ××     ××    
    ≈≈          ∞∞∞∞∞∞∞  =÷= ≈≈π         ××       ××     ××÷      ××  ××      ××    
    ≈≈        ∞∞√    ∞∞  =÷= ≈≈≈         ××      ××      ××       ×× ××      ××≠    
     ≈≈   ≈≈≈ √∞∞   ∞∞∞  =÷=  ≈≈≈   ≈≈∞  ××      ××      ××       ××××      ×××     
       ≈≈≈≈     ∞∞∞√ ∞∞  =÷=    √≈≈≈      ××      ×××   √××        ××     ×××       
                                           ××=          ××       ∞××    ×××         
                                                     ××××      ×××                  
    """)
    """                                                                                              
                                                          ===                                  ===        
                                                       π+++ += =+∞++=      ÷++++++=           =+ ++=      
                               ≠-+-≠                  ÷+     = ×    =    =++      =           =    +=     
                               -   -                =++   +++= ×+  +=   ∞+   +++++=           =++   +∞    
       √=----÷≈    π∞≈≈≈≈≈∞π   +   +   ∞÷+++++÷∞   =+   ++==+++++++= =+++   ++++==++÷    =+++=  =+   +    
     √=-      π÷√ π≈       =∞π +   + ∞÷+       +=  +   +×  =      +  =          =+  +÷  ≈+   =   +   +    
    √-   ----   √ π  =≈≈≠≈   ∞ +   +∞+    +++     =+  ×-   =+++   +  =+++   ++++=+   +  +   +=   +   +    
    =   -∞  √=-=√ ∞=÷=≈≈≠=×  ≈ +   +÷   +÷∞ ∞÷+-= +   +      =+  +=    =+  +=    -+  +√+   +=    +   +    
    -  +=        π≈          ≈ +   ++   +         +   +      +   +     +   +      +   ++  +=    =+   +    
    =   -√  √=-=√∞   ÷≈≈≠=×  ≈ +   +÷   +∞   ≈×+÷∞+   +=     +   +     +   +      +   +  +=    =+   +=    
    √-   ----   √∞   ÷≈≈≠    ≈ +   +∞+   ++++≈   ∞=+   +π    +   +++= =+  +=      =+    +=   =++   +=     
     √÷        -√π≈       =  ∞ -   - ∞÷+       +÷∞ +   ≠+=   =+     = +   +       =+   +=  =++    +=      
       ≠÷-----=√   ∞≈≈≈≈≈∞∞∞∞π ≠-+-≠   ∞÷+++++÷∞   √++   +    =++++++÷+   +   =++++   +=   +    ++=       
                                                     ÷+  +        + ++   +=   +      +=    +  ++=         
                                                      =++=              +=    +    ++=     =++≠           
                                                                  -+++++=     =++++=                                                                                                                   
          """ #print logo
    print("Bringing AI to calculation since yesterday")
    print("WARNING: This program is in early development and the AI model (Calcif-AI) tends to hallucinate. Read EULA for more details.)")
    if (input("Please support us on Ko-Fi by typing \033[91m\"kofi\"!\033[00m \nIf not, press any key to start: ") == "kofi"):
        # webbrowser.open("https://www.ko-fi.com/calcify", new=1)
        load_internet_ad("Kofi")
    return


def load_user_data():
    if not DATA_FILE.exists():
        with DATA_FILE.open("w", newline="", encoding="utf-8") as file:
            file.write("emailhere,0,0,0\n")

    with DATA_FILE.open("r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        row = next(reader, None)

    if row is None or len(row) < 3:
        row = ["emailhere", "0", "0","0"]

    username = row[0].strip()
    if username == "" or username == "emailhere":
        print("You haven't signed up yet. Please sign up to save your progress:")
        username = input("Email: ").strip() or "Player"
        _ = input("Password: ") # NOT ACTUALLY STORED, JUST FOR SHOW
        save_user_data(username, 0, 0,0)
        return username, 0, 0,0


    try:
        xp = int(row[1])
    except (ValueError, IndexError):
        xp = 0
    try:
        level = int(row[2])
    except (ValueError, IndexError):
        level = 0

    print(f"Welcome back, {username}")

    return username, xp, level


def save_user_data(username, xp, level,dlc):
    with DATA_FILE.open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([username, xp, level,dlc])


# reads from the eula.txt file
def print_eula():
    eula_path = Path(__file__).resolve().parent / "eula.txt"
    try:
        with eula_path.open("r", encoding="utf-8") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("The file path does not exist.")
    input("Press any button to continue: ")
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
    print("~-", xpbar, "-~ XP: ", xp, "/ 20\n")
    return


def print_menu(xp=0, level=0, dlc=False) -> tuple[int, int]:
    os.system("cls" if os.name == "nt" else "clear") #clears the screen every time the menu is drawn
    
    #check for a level up
    if (xp >= 20):
        xp, level = level_up(xp, level)
        print("Level UP!!\nYou are now at level ", level, "!")
    
    #prints the level bar
    print_levelbar(xp, level)

    print("Your available operators:\n")
    print_typed("[+]  Addition: The trusty, rusty, dusty, original operator.")
    print_typed("[-]  Subtraction: Addition's WAAACCCKY cousin!!")

    if (level > 2):
        print_typed("[*]  Multiplication: A super-beefed up version of addition.Unlocked at Level 2.")
    else:
        print_typed("[*]  LOCKED: Unlocked at Level 2")
    if (level > 3):
        print_typed("[/]  Division: NASTY. I've never seen anything like this before! While Multiplication uses his powers for good, Division uses his powers for EVIL. Unlocked at Level 3")
    else:
        print_typed("[/]  LOCKED: Unlocked at Level 3.")
    print("\n")

    if not dlc:
        print("[**]   LOCKED: Unlocked via purchase of the \"Powers n' Roots\" Expansion Pack for $4.99")
        print("[sqrt]   LOCKED: Unlocked via purchase of the \"Powers n' Roots\" Expansion Pack for $4.99")
        print("[log]   LOCKED: Unlocked via purchase of the \"Logs n' Remainder\" Expansion Pack for $4.99")
        print("[%]   LOCKED: Unlocked via purchase of the \"Logs n' Remainder\" Expansion Pack for $4.99")
        print("\n")
    else:
        print_typed("[**]   Exponetiation: Imagine multiplication, but EXTREME")
        print_typed("[sqrt]   Square Root: A literal supervillian, cutting everything it sees in half ")
        print_typed("[log]   Logarithm: The reverse of exponentiation — finds the power that made the number.")
        print_typed("[%]   Modulo(Remainder): What’s left over after division, like the last cookie slice.")
        print("\n")
    
    return xp, level

def take_input() -> tuple[str, list[str]]:
    valid_names = {"sqrt", "log", "ln", "pi"}
    allowed_chars = re.compile(r'^[0-9A-Za-z+\-*/%.() \t]+$')
    name_tokens = re.compile(r'[A-Za-z_]\w*')

    while True:
        full_equation = input("Enter your equation: ").strip()
        if full_equation == "":
            print("Please enter an equation.")
            continue

        if not allowed_chars.match(full_equation):
            invalid_chars = sorted(set(re.findall(r'[^0-9A-Za-z+\-*/%.() \t]', full_equation)))
            print("Invalid character(s):", " ".join(invalid_chars))
            continue

        invalid_names = [
            name
            for name in name_tokens.findall(full_equation)
            if name not in valid_names
        ]
        if invalid_names:
            print("Invalid function or name:", ", ".join(dict.fromkeys(invalid_names)))
            continue
        
        operators = re.findall(r'\*\*|%|\b(?:sqrt|log|ln)\b|[+\-*/]', full_equation)
        return full_equation, operators

"""
def take_input() -> tuple[list, list]:
    valid_variables = ["+", "-", "*", "/",'.', ' ', '(', ')', '**', '%']
    equation_components = [""]

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

            except:
                if value not in valid_variables:
                    print(f"Invalid character: {value}")
                else:
                    equation_components.append(value)
                    checked_values -= 1

        if checked_values == 0:
            break              

    full_equation = "".join(equation_components)
    operators = re.split(r'[0123456789. ]', full_equation)
            
    return full_equation, operators

"""    

def calculate(full_equation, operators, level, dlc) -> tuple[float, int, str]:

    # list of named operations and associted math modules
    named_operations = {
        "sqrt": math.sqrt,
        "log": math.log10,
        "ln": math.log,
        "pi": math.pi
    }

    # random chance we "reprompt" the "AI" with new equation
    if random.randrange(100) <= 10:
        return None, 0, load_ai_output()
    
    for operator in operators:
        if operator == "*" and level < 2:
            return None, new_xp, "You haven't unlocked that operator yet!\n"
        elif operator == "/" and level < 3:
            return None, new_xp, "You haven't unlocked that operator yet!\n"

    # checking if they a trying to access a dlc operator without paying for it
    if "sqrt" in operators or "**" in operators:
        if not dlc:
            return None, new_xp, "This operator is unlocked in DLC! Please purchase the \"Powers n' Roots\" Expansion Pack for $4.99."
    if "log" in operators or "ln" in operators or "%" in operators:
        if not dlc:
            return None, new_xp, "This operator is unlocked in DLC! Please purchase the \"Logs n' Remainders\" Expansion Pack for $4.99."
        

    # presenting our loading screen, alongside a brief advertisement
    print("Working on it! In the meanwhile, check out a word from our sponsors!")
    load_internet_ad()
    for i in range(2):
        for i in ["*", "**", "**-", "**--", "**--+", "**--++", "**--++÷", "**--++÷÷"]:
            time.sleep(0.5)
            print(i)
            # Move cursor up one line
            sys.stdout.write('\x1b[1A')
            # Clear the last line
            sys.stdout.write('\x1b[2K')


    # actually calculating the equation through eval builtin, accounting for bad syntax and divide by zero
    try:
        answer = eval(full_equation, {"__builtins__": None}, named_operations)
    except ZeroDivisionError:
        return None, 0, "Division by zero is not allowed."
    except Exception:
        return None, 0, "Invalid expression. Please check your syntax."
    
    # stores the xp gained from calculation, then returns the answer with xp
    new_xp = len(operators) 
    return answer, new_xp, ""

       
        




def response(full_equation,answer,new_xp,xp,level, error_message) -> None:
    # print("\n")
    # creates a clear canvas with the users data available
    os.system("cls" if os.name == "nt" else "clear") #clears the screen 
    print_levelbar(xp, level)
    
    # checks if there was a error message, and if so prints that
    if error_message != "":
        print_typed(error_message)
    # otherwise, prints users equation, answer, gained xp, total xp, and level
    else:
        print_typed(f'The answer to {full_equation} is {answer}!')
        print_typed(f'You earned {new_xp} XP from that calculation!')
        if xp >= 20:
            print_typed(f'Congratulations! You leveled up to level {level + 1}!')
        print_typed(f'You now have {xp} XP! Only {20-xp} XP until the next level!')
    return


def main() -> None:
    # loads user data and 
    username, xp, level,dlc = load_user_data()

    initialize()

    while True:
        xp, level = print_menu(xp, level)
        
        full_equation, operators = take_input()

        answer, new_xp, error_message = calculate(full_equation, operators, level, dlc)
        xp += new_xp

        response(full_equation, answer, new_xp, xp, level, error_message)

        redo_menu = int(input(
            """What would you like to do next?\n
            [1]: Do another calculation\n
            [2]: Contact customer support\n
            [3]: Purchase DLC\n
            [4]: Exit\n
            """))

        if redo_menu == 1:
            continue
        elif redo_menu == 2:
            supportInit()
            time.sleep(15)
        elif redo_menu == 3:
            print("Alakazam! A mysterious benifactor has gifted you the \"Powers n' Remainders\" Expansion Pack for $4.99! You can now use the ** & %.")
            dlc = True
            print("Please pay us anyway man we need it")
            # webbrowser.open("https://www.ko-fi.com/calcify", new=1)
            load_internet_ad("Kofi")
            time.sleep(4)
        elif redo_menu == 4:
            print("Exiting... Your data has been saved.")
            break
    
    save_user_data(username, xp, level,dlc)
    print("Goodbye! and please consider supporting us on Ko-Fi for updates and new features!")
    load_internet_ad("Kofi")
    # webbrowser.open("https://www.ko-fi.com/calcify", new=1)
    
    return



main()




# CODE SCRAPYARD

"""


"""