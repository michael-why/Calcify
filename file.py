import os


# hello, world!
"""
xp system: 10 xp per level
level 0/1: addition and subtraction, nothing else
level 3: adds multiplication and division
"""


def initialize() -> None:
    os.system('cls') #clears the screen every time it initializes
    print(""" 
                    ÷÷             ≠≠≠  ++    ++++        ≠≠   
    ÷÷÷÷     ×××    ÷÷    ===     ≠≠         ++            ≠≠  
  ÷÷    ÷÷       ×  ÷÷  ==    =  ≠≠   +++  ++++++ ++  ++   ≠≠  
  ÷         ××××××  ÷÷ ==        ≠     ++    +    ++ ++    ≠≠  
  ÷÷    ÷  ×     ×  ÷÷  =     =  ≠≠    +    ++     + +     ≠   
    ÷÷÷÷÷   ×××× ×  ÷÷   =====   ≠≠    +++  ++     ++    ≠≠    
                                   ≠       ++    +++    ≠ 
          """) #print logo

    input("Welcome to calc(ify)! \n \nPlease press any key to start: ")
    return

def print_menu() -> None:
    os.system('cls') #clears the screen every time the menu is drawn
    # print the XP bar at the top
    return


def take_input():
    
    valid_variables = ["+", "-", "*", "/"]
    equation_components = [""]

    valid_equation = False

    
    while valid_equation == False:
        temp_equation = input("Enter your equation: ")
        
        
        for value in temp_equation:
            try:
                float(value)
                if type(equation_components[-1]) == str:
                    equation_components.append(float(value))
                else:
                    equation_components[-1] = float(str(equation_components[-1]) + value)
            except ValueError:
                if value not in valid_variables:
                    print(f"Invalid character: {value}")
                else:
                    equation_components.append(value)


        
    return equation_components


    
    
    


def adverts() -> None:
    
    return


def main() -> None:

    print(take_input())

    return


initialize()

main()

"""
BASIC FEATURES: 
take in user input for number of operands (1,2,16,3.4) & operations between operands ( + - * / )
output to terminal.

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