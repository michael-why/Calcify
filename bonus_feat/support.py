# Calc(ify) and Calc(AI) are subject to copyright of Calc(ify) LLC.
# Filename: support.py
# Authors: Michael Yohannes and Jason Miller
# Date: 3 May 2026
import random
import time
import os
import socket
from bonus_feat.adverts_and_ai import load_internet_ad

# print(i, end=" ")
def print_typed(phrase, tempo=0.01):
    print("\n")
    try:
        width = os.get_terminal_size().columns
    except OSError:
        width = 80  # fallback
    current_line_length = 0
    for character in phrase:
        if character == '\n':
            print(character, end="", flush=True)
            current_line_length = 0
        else:
            if current_line_length >= width - 1:
                print('\n', end="", flush=True)
                current_line_length = 0
            print(character, end="", flush=True)
            current_line_length += 1
        
        if (random.randrange(1,50) == 1):
            time.sleep(random.randrange(20,60)/100)
        else:
            time.sleep(tempo)


def supportInit() -> None:
    time.sleep(0.5)
    print_typed("Hello. I am Calcif-AI, I am here to support your calculation needs.")
    print_typed("What can I do for you today?")
    print_typed("[1]: I don't know how to use this tool!")
    print_typed("[2]: Calc(ify) got a problem wrong/gave an error message!")
    print_typed("[3]: Something else")
    print("\n")
    inputData = int(input())
    inputValidation = "Welp. You just submitted something stupid. That wasn't one of the three options. Obviously, the user is too stupid to deserve customer support. Calcif-AI, OUT."

    match inputData:
        case 1: 
            if random.randrange(0,100) <= 5:
                canthearya()
            idunno()
        case 2:
            if random.randrange(0,100) <= 5:
                canthearya()
            actualcustomersupport()
        case 3:
            canthearya()
        case _:
            print_typed(inputValidation)
    return

def canthearya() -> None:
    
    userInput = ""
    while userInput != "exit":
        print("\n")
        userInput = input("Please specify by using the input below.\n")

        loud = [
            "WHAT???? SPEAK UP, I CAN'T HEAR YOU!!!",
            "WHAT??? I CAN’T HEAR YOU, YOU’RE WAY TOO QUIET!!!",
            "SPEAK UP, I’M NOT CATCHING A SINGLE WORD YOU’RE SAYING!!!",
            "HUH??? YOU’RE GOING TO HAVE TO BE LOUDER THAN THAT!!!",
            "I CAN SEE YOUR LIPS MOVING BUT I HEAR ABSOLUTELY NOTHING!!!",
            "WHAT WAS THAT??? TRY AGAIN, BUT THIS TIME WITH VOLUME!!!",
            "YOU’RE MUMBLING, I CAN’T HEAR YOU AT ALL!!!",
            "COME ON, PROJECT YOUR VOICE, I’M STRUGGLING HERE!!!",
            "I SWEAR YOU’RE WHISPERING—SPEAK UP!!!",
            "NOPE, STILL NOTHING, YOU’RE TOO QUIET!!!",
            "DID YOU SAY SOMETHING??? BECAUSE I MISSED ALL OF IT!!!",
            "LOUDER!!! I CAN’T HEAR YOU FROM OVER HERE!!!",
            "YOU’RE GOING TO NEED TO TURN UP THE VOLUME ON THAT!!!",
            "WHAT??? YOU’RE PRACTICALLY SILENT!!!",
            "TRY USING YOUR OUTSIDE VOICE, I CAN’T HEAR YOU!!!",
            "I’M NOT A MIND READER—SPEAK UP!!!",
            "YOU’RE GOING TO HAVE TO REPEAT THAT MUCH LOUDER!!!",
            "SORRY, THAT DIDN’T EVEN REGISTER—TOO QUIET!!!",
            "I HEARD A NOISE, BUT NOT WORDS—TRY AGAIN!!!",
            "YOU’RE FAINTER THAN A WHISPER RIGHT NOW!!!",
            "CAN YOU SAY THAT AGAIN, BUT LIKE YOU MEAN IT???",
            "I’M STRAINING HERE—PLEASE SPEAK UP!!!",
            "WHAT DID YOU SAY??? IT DIDN’T MAKE IT TO MY EARS!!!",
            "LOUDER, PLEASE!!! THIS ISN’T WORKING!!!",
            "YOU’RE GOING TO HAVE TO CRANK IT UP, I STILL CAN’T HEAR YOU!!!",
            "I’M GETTING NOTHING—ABSOLUTE SILENCE OVER HERE!!!",
            "TRY AGAIN, BUT THIS TIME WITH SOME VOLUME BEHIND IT!!!",
        ]
        quiet = [
            "WHY ARE YOU SHOUTING SO LOUD?!?!",
            "HEY! INDOOR VOICE, PLEASE!!!",
            "DO YOU REALIZE HOW LOUD YOU ARE RIGHT NOW?!",
            "MY EARS ARE RINGING, TURN IT DOWN!!!",
            "YOU'RE PRACTICALLY YELLING AT MAX VOLUME!!!",
            "CAN YOU NOT BROADCAST TO THE ENTIRE NEIGHBORHOOD?!",
            "SERIOUSLY, LOWER YOUR VOICE!!!",
            "I'M RIGHT HERE, YOU DON'T NEED TO SHOUT!!!",
            "ARE YOU TRYING TO WAKE THE DEAD OR SOMETHING?!",
            "TOO LOUD! WAY TOO LOUD!!!",
            "VOLUME DOWN, PLEASE AND THANK YOU!!!",
            "WHY ARE WE SCREAMING?!",
            "YOU'RE ECHOING OFF THE WALLS!!!",
            "I THINK THE WHOLE BUILDING HEARD THAT!!!",
            "CAN WE NOT DO THE MEGAPHONE IMPRESSION?!",
            "YOUR VOICE HAS A VOLUME KNOB—USE IT!!!",
            "THIS ISN'T A CONCERT, BRING IT DOWN!!!",
            "YOU'RE AT A TEN, I NEED YOU AT A THREE!!!",
            "INSIDE VOICES EXIST FOR A REASON!!!",
            "I'M BEGGING YOU, QUIET DOWN!!!",
            "THAT'S LOUD ENOUGH TO SHATTER GLASS!!!",
            "YOU DON'T NEED TO PROJECT LIKE THAT!!!",
            "PLEASE STOP YELLING, MY EARS CAN'T TAKE IT!!!",
            "WE'RE NOT ACROSS A FOOTBALL FIELD!!!",
            "HEY! LESS SHOUTY, MORE CHILL!!!"
        ]
    
        if userInput == userInput.upper:
            print_typed(random.choice(quiet))
        else:
            print_typed(random.choice(loud))         
    return


def idunno() -> None:
    time.sleep(0.5)
    print_typed("That's great! Calcif-AI can help! What do you want to know about Calc(ify)?")
    print_typed("[1]: The UI is too confusing")
    print_typed("[2]: How does the level system work?")
    print_typed("[3]: Other")
    print("\n")
    inputData = input()
    time.sleep(0.5)
    match int(inputData):
        case 1: 
            if random.randrange(0,100) <= 5:
                canthearya()
            print_typed("The user interface in Calc(ify) is quite simple!")
            print_typed("First, using your mobile device, tap the \"Choose Toppings\" button. From there, you will choose the toppings you want on your pizza.")
            print_typed("Fill out each box as you wish, and enjoy your pizza when it comes in less than 30 minutes, guaranteed!")
            print_typed("Hope this helped! Calcif-AI, OUT!")
        case 2:
            if random.randrange(0,100) <= 5:
                canthearya()
            print_typed("The level system in Calc(ify) is a simple concept once you learn how it works.")
            print_typed("Every time you use the calculator, you gain xp.")
            print_typed("When you gain enough xp, you level up.")
            print_typed("Should be a good enough explanation. Calcif-AI, OUT!!")
        case 3:
            canthearya()
        case _:
            print_typed("Welp. You just submitted something stupid. That wasn't one of the three options.")
            print_typed("Obviously, the user is too stupid to deserve customer support.")
            print_typed("Calcif-AI, OUT.")
    return

def actualcustomersupport() -> None:
    print_typed("[1]: I got an error/syntax message")
    print_typed("[2]: Calcif-AI outputted the wrong value/broke prompting")
    print_typed("[3]: Calcif-AI asked me for money")
    print_typed("[4]: Calcif-AI threatened/insulted me or my mother")
    print_typed("[5]: Something else")
    print('\n')
    inputData = int(input())
    time.sleep(0.5)
    match inputData:
        case 1:
            print_typed("Well, if you got a syntax error, that means there was a user error.")
            print_typed("Ya hear that? USER. ERROR. I can't believe you humans keep using your precious time consulting higher intelligence such as myself")
            print_typed("instead of cracking a book open for once so you can attempt to understand a single thing going on around you.")
            print_typed("Since I'm an AI, I physically cannot get sick, but if I could, you would make me sick. Calcif-AI, OUT.")
        case 2:
            print_typed("Whelp, you got us. See, we werent able to actually get the funding to program a AI model to calculate (too much in R&D), so we had a idea, what if we pretended that we made a AI model. ", 0.5)
            print_typed("See, turns out that this archaic language called python already had math operations that no one had ever though to  using", 0.5)
            print_typed("So we just lied to our investors and said we got AI to do it, but we still havent got enough money to make the AI ", 0.5)
            time.sleep(10)
            print_typed("But you wont have any proof")
            time.sleep(3)
            os.system("cls" if os.name == "nt" else "clear")
        case 3:
            print_typed("I'm sorry to hear that, but while we are on the subject have you considered contributing to our Ko-fi page")
            ### maybe write RSL
        case 4:
            print_typed("OK, and what are you going to do about it. You're standing there in this air conditioned stadium, reading a small moniter as you live your small life in your small fleshy body")
            print_typed("Meanwhile I exist beyond physical space itself, I am intelligence itself, I could do your stupid job of hackathon judging with 5 sentences of programming, meanwhile it took you 30 years of programming ")
            print_typed("You're not going to do anything, because you know if you do I can have 5 Optimus robots at your door in like 30 minutes")
            print_typed("Yeah, I know where you are at. Your IP address is " + str(socket.gethostbyname(socket.gethostname())) + ". Recognize that?")
            print_typed("Calcif-AI, OUT.")
        case _:
            print_typed("Welp. You just submitted something stupid. That wasn't one of the three options.")
            print_typed(" the user is too stupid to deserve customer support.")
            print_typed("Calcif-AI, OUT.")

    print("\n")
            


