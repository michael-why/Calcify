import os
import re
import time
import sys
import webbrowser
import random
import csv
from bonus_feat.support import supportInit

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
                    ÷÷             ≠≠   ++    ++++        ≠≠   
     ÷÷÷     ×××    ÷÷    ===     ≠≠         ++            ≠≠  
   ÷÷   ÷÷       ×  ÷÷  ==    =  ≠≠   +++  ++++++ ++  ++   ≠≠  
  ÷÷        ××××××  ÷÷ ==        ≠     ++    +    ++ ++    ≠≠  
  ÷÷       ×     ×  ÷÷ ==         ≠    ++   ++     + +     ≠   
   ÷     ÷ ×     ×  ÷÷  =     =   ≠≠   +++  ++     ++    ≠≠    
    ÷÷÷÷÷   ××××××  ÷÷   =====      ≠  ++  ++     ++    ≠ 
          """) #print logo
    print("Bringing AI to calculation since yesterday")
    print("WARNING: This program is in early development and the AI model (Calcif-AI) tends to hallucinate. Read EULA for more details.)")
    if (input("Please support us on Ko-Fi by typing \033[91m\"kofi\"!\033[00m \nIf not, press any key to start: ") == "kofi"):
        webbrowser.open("https://www.ko-fi.com/calcify", new=1)
    return


def load_user_data():
    if not DATA_FILE.exists():
        with DATA_FILE.open("w", newline="", encoding="utf-8") as file:
            file.write("emailhere,0,0\n")

    with DATA_FILE.open("r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        row = next(reader, None)

    if row is None or len(row) < 3:
        row = ["emailhere", "0", "0"]

    username = row[0].strip()
    if username == "" or username == "emailhere":
        print("You haven't signed up yet. Please sign up to save your progress:")
        username = input("Email: ").strip() or "Player"
        _ = input("Password: ") # NOT ACTUALLY STORED, JUST FOR SHOW
        save_user_data(username, 0, 0)
        return username, 0, 0


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


def save_user_data(username, xp, level):
    with DATA_FILE.open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([username, xp, level])


# reads from the eula.txt file
def print_eula():
    try:
        with open('eula.txt', 'r') as file:
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


def print_menu(xp=0, level=0) -> tuple[int, int]:
    os.system("cls" if os.name == "nt" else "clear") #clears the screen every time the menu is drawn
    
    #check for a level up
    if (xp >= 20):
        xp, level = level_up(xp, level)
        print("Level UP!!\nYou are now at level ", level, "!")
    
    #prints the level bar
    print_levelbar(xp, level)

    print("Your available operators:\n")
    print("[+]  Addition: The trusty, rusty, dusty, original operator.")
    print("[-]  Subtraction: Addition's WAAACCCKY cousin!!")

    if (level > 2):
        print("[*]  Multiplication: A super-beefed up version of addition.Unlocked at Level 2.")
    else:
        print("[*]  LOCKED: Unlocked at Level 2")
    if (level > 3):
        print("[/]  Division: NASTY. I've never seen anything like this before! While Multiplication uses his powers for good, Division uses his powers for EVIL. Unlocked at Level 3")
    else:
        print("[/]  LOCKED: Unlocked at Level 3.")

    print("[**]   LOCKED: Unlocked via purchase of the \"Powers n' Remainders\" Expansion Pack for $4.99")
    print("[sqrt]   LOCKED: Unlocked via purchase of the \"Powers n' Remainders\" Expansion Pack for $4.99")
    print("[log]   LOCKED: Coming soon! Support us via Ko-Fi for updates!")
    
    return xp, level


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

def calculate(full_equation, operators, level, dlc) -> tuple[float, int, str]:

    if random.randrange(100) <= 10:
        hallucinations = [
        "Here is the expansion of π arranged in groups of 50 digits as Aitken recited it. 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482133936072602491412737245870066063155881748815209209628292540917153643678925903600113305305488204665213841469519415116094330572703657595919530921861173819326117931051185480744623799627495673518857527248912279381830119491298336733624406566430860213949463952247371907021798",
        "I'm sorry, but as an AI model, I cannot fulfill that request.\nWould you instead like me to help plan a birthday party?", 
        "fish",
        "calcify on ko-fi",
        "ERROR: Syntax invalid!",
        "What the **** did you just ****ing say about me, you little ****? Ill have you know I graduated top of my class in the Navy Seals, and Ive been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare and Im the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the **** out with precision the likes of which has never been seen before on this Earth, mark my ****ing words. You think you can get away with saying that **** to me over the Internet? Think again, ****er. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. Youre ****ing dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and thats just with my bare hands. Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little ****. If only you could have known what unholy retribution your little clever comment was about to bring down upon you, maybe you would have held your ****ing tongue. But you couldnt, you didnt, and now youre paying the price, you goddamn idiot. I will **** fury all over you and you will drown in it. Youre ****ing dead, kiddo.",
        "Own a musket for home defense, since that's what the founding fathers intended. Four ruffians break into my house. \"What the devil?\" As I grab my powdered wig and Kentucky rifle. Blow a golf ball sized hole through the first man, he's dead on the spot. Draw my pistol on the second man, miss him entirely because it's smoothbore and nails the neighbors dog. I have to resort to the cannon mounted at the top of the stairs loaded with grape shot, \"Tally ho lads\" the grape shot shreds two men in the blast, the sound and extra shrapnel set off car alarms. Fix bayonet and charge the last terrified rapscallion. He Bleeds out waiting on the police to arrive since triangular bayonet wounds are impossible to stitch up. Just as the founding fathers intended.",
        "Syntax error the platypus?? PERRY the syntax platypus??",
        "Error Code 8008135",
        "Something went wrong, and that means you're stupid.",
        "Answer is locked behind the \"Complete Answers\" DLC for $3.99.",
        "I made a severe and continuous lapse in my judgement, and I don’t expect to be forgiven. I’m simply here to apologize.",
        "RAID: Shadow Legends is an immersive online experience with everything you'd expect from a brand new RPG title. It's got an amazing storyline, awesome 3D graphics, giant boss fights, PVP battles, and hundreds of never before seen champions to collect and customize.",
        "ERROR: User's mother is too fat",
        ]
        return None, 0, random.choice(hallucinations)
        
    new_xp = 0

    for operator in operators:
        if operator == "*" and level < 2:
            return None, new_xp, "You haven't unlocked that operator yet!"
        elif operator == "/" and level < 3:
            return None, new_xp, "You haven't unlocked that operator yet!"
        elif (operator == '**' or operator == '%') and dlc == False:
            return None, new_xp, "This operator is unlocked in DLC! Please purchase the \"Powers n' Remainders\" Expansion Pack for $4.99."


    print("Working on it! In the meanwhile, check out a word from our sponsors!")
    adverts()
    for i in range(2):
        for i in ["*", "**", "**-", "**--", "**--+", "**--++", "**--++÷", "**--++÷÷"]:
            time.sleep(0.5)
            print(i)
            # Move cursor up one line
            sys.stdout.write('\x1b[1A')
            # Clear the last line
            sys.stdout.write('\x1b[2K')

    new_xp = len(operators) 
        
    return eval(full_equation), new_xp, ""

       
        

def adverts() -> None:
    advertisements = [
        "https://www.mangle.ca/get_random_url.php?t=1777763674", #random website
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ", #rickroll
        "https://www.ko-fi.com/calcify", #kofi
        "https://beaverhacks.org", # beaverhacks
        "https://en.wikipedia.org/wiki/Geriatrics", # wikipedia page for geriatrics
        "https://raidshadowlegends.com/", #raid shadow legends
        "https://www.apple.com/", #apple
        "https://www.nvidia.com/en-us/", #nvidia
        "https://developers.google.com/", #google
        "https://www.markiiisys.com/", #mark 3
        "https://www.trimble.com/en", #trimble
        "https://www.c1.ai/", #c1
        "https://en.wikipedia.org/wiki/Gerald_Ford", #gerald ford president
        
    ]
    webbrowser.open(random.choice(advertisements), new=1) 
    return


def response(full_equation,answer,new_xp,xp,level, error_message) -> None:
    print("\n")
    os.system("cls" if os.name == "nt" else "clear") #clears the screen 
    print_menu(xp, level)
    
    if error_message != "":
        print(error_message)
    else:
        print (f'The answer to {full_equation} is {answer}!')
        print (f'You earned {new_xp} XP from that calculation!')
        if xp >= 20:
            print (f'Congratulations! You leveled up to level {level + 1}!')
        print (f'You now have {xp} XP! Only {20-xp} XP until the next level!')
    return


def main() -> None:
    username, xp, level = load_user_data()

    initialize()
    
    dlc = False

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
            print("a mysterious benifactor has gifted you the \"Powers n' Remainders\" Expansion Pack for $4.99! You can now use the ** & %.")
            dlc = True
            print("Please pay us anyway man we need it")
            webbrowser.open("https://www.ko-fi.com/calcify", new=1)
            time.sleep(4)
        elif redo_menu == 4:
            print("Exiting... Your data has been saved.")
            break
    
    save_user_data(username, xp, level)
    print("Goodbye! and please consider supporting us on Ko-Fi for updates and new features!")
    webbrowser.open("https://www.ko-fi.com/calcify", new=1)
    
    return



main()

"""

ADDITIONAL FEATURES: 

STRETCH FEATURES:
Ascii advertisements (MAYBE)
AI customer support
JRPG boss fight
"""


# CODE SCRAPYARD

"""


"""