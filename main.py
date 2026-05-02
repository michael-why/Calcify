import os
import re
import time
import sys

# hello, world!


def initialize() -> None:
    os.system("cls" if os.name == "nt" else "clear") #clears the screen every time it initializes

    print("Welcome to calc(ify)!")
    print(""" 
                    ÷÷             ≠≠   ++    ++++        ≠≠   
    ÷÷÷÷     ×××    ÷÷    ===     ≠≠         ++            ≠≠  
  ÷÷    ÷÷       ×  ÷÷  ==    =  ≠≠   +++  ++++++ ++  ++   ≠≠  
  ÷         ××××××  ÷÷ ==        ≠     ++    +    ++ ++    ≠≠  
  ÷÷    ÷  ×     ×  ÷÷  =     =   ≠    ++   ++     + +     ≠   
    ÷÷÷÷÷   ××××××  ÷÷   =====    ≠≠   +++  ++     ++    ≠≠    
                                    ≠  ++  ++     ++    ≠ 
          """) #print logo

    input("Please press any key to start: ")
     
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
        print("\n[*]  LOCKED: Unlocked at Level 2\n")
    if (level > 3):
        print("[/]  Division: NASTY. I've never seen anything like this before! While Multiplication uses his powers for good, Division uses his powers for EVIL.\nUses evil powers to subtract repeatedly.\nUnlocked at Level 3")
    else:
        print("\n[/]  LOCKED: Unlocked at Level 3.")
    return


def print_menu(xp=0, level=0) -> (int, int):
    os.system("cls" if os.name == "nt" else "clear") #clears the screen every time the menu is drawn
    
    #check for a level up
    if (xp >= 20):
        xp, level = level_up(xp, level)
        print("Level UP!!\nYou are now at level ", level, "!")
    
    #prints the level bar
    print_levelbar(xp, level)

    # take a wild guess
    print_available_operators(level) 
    return xp, level


def take_input() -> (list, list):
    
    valid_variables = ["+", "-", "*", "/",'.', ' ']
    equation_components = [""]
    valid_equation = False

    while True:
        temp_equation = input("Enter your equation: ")
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
            print("This character is unlocked in DLC! Please purchase the DLC to use this operator.")
            validity = False
            break
    if validity == True:
        # creates a loading screen 

        print("Calculating...")
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
        return None, xp
        

def adverts() -> None:
    
    return


def response(full_equation,answer,new_xp,xp,level) -> None:
    print (f'The answer to {full_equation} is {answer}!')
    print (f'You earned {new_xp} XP from that calculation!')
    if xp >= 20:
        print (f'Congratulations! You leveled up to level {level + 1}!')
    print (f'You now have {xp} XP! Only {20-xp} XP until the next level!')

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
    xp = 8 #sets xp to zero. Change this somehow if you don't want the xp to reset every time you initialize
    level = 0 #same here
    initialize()
    new_xp, level = print_menu(xp, level)
    xp += new_xp

    full_equation, operators = take_input()
    
    answer, xp = calculate(full_equation, operators, level)

    response(full_equation, answer, new_xp,xp,level)
    


    return



main()

"""


ADDITIONAL FEATURES: 
DLC operands ( **, sqrt(), etc)
Future updates (logarithms
leveling/xp system (start with only addition and subtraction and user unlocks other operators through calculation (user retention))
Customer support, random failures (AI hallucination)  *MAKE INTENTIONAL FOR RECORDING

STRETCH FEATURES:
Ascii advertisements and kofi pop up in windows
ascii ai art interpretation
AI customer support
JRPG boss fight
Ko-fi implementation
"""


# CODE SCRAPYARD

"""GDSKHGGAKJDSGKJSAkjGKJDSHKJSKJDHKJASHKJDHKJDSAHKJHDSKJHDSAKJHSAKJHDSKJSAHKDSAJHDSDSHDSA

 for value in range(1,len(equation_components)):
            if type(equation_components[value-1]) == int or equation_components[value-1] == ".":
                equation_components[-1] = str(equation_components[-1] + equation_components[value])
                equation_components.pop(value)


"""