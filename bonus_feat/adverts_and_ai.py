# Calc(ify) and Calc(AI) are subject to copyright of Calc(ify) LLC.
# Filename: adverts_and_ai.py
# Authors: Michael Yohannes and Jason Miller
# Date: 3 May 2026
import webbrowser
import random


def load_internet_ad(brand='') -> None:
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
        "https://en.wikipedia.org/wiki/Gerald_Ford", #gerald ford presiden  
    ]

    if brand == "Kofi":
        webbrowser.open(advertisements[2])
    else:
        webbrowser.open(random.choice(advertisements), new=1) 
    return

def load_ai_output(prompt=-1) -> str:
    hallucinations = [
        "ERROR: Here is the expansion of π arranged in groups of 50 digits as Aitken recited it. 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482133936072602491412737245870066063155881748815209209628292540917153643678925903600113305305488204665213841469519415116094330572703657595919530921861173819326117931051185480744623799627495673518857527248912279381830119491298336733624406566430860213949463952247371907021798. ",
        "ERROR: I'm sorry, but as an AI model, I cannot fulfill that request.\nWould you instead like me to help plan a birthday party? ", 
        "ERROR: fish ",
        "ERROR: Not enough money. Support calcify on ko-fi ",
        "ERROR: Syntax invalid! ",
        "ERROR: What the **** did you just ****ing say about me, you little ****? Ill have you know I graduated top of my class in the Navy Seals, and Ive been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare and Im the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the **** out with precision the likes of which has never been seen before on this Earth, mark my ****ing words. You think you can get away with saying that **** to me over the Internet? Think again, ****er. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. Youre ****ing dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and thats just with my bare hands. Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable *** off the face of the continent, you little ****. If only you could have known what unholy retribution your little clever comment was about to bring down upon you, maybe you would have held your ****ing tongue. But you couldnt, you didnt, and now youre paying the price, you goddamn idiot. I will **** fury all over you and you will drown in it. Youre ****ing dead, kiddo. ",
        "ERROR: Own a musket for home defense, since that's what the founding fathers intended. Four ruffians break into my house. \"What the devil?\" As I grab my powdered wig and Kentucky rifle. Blow a golf ball sized hole through the first man, he's dead on the spot. Draw my pistol on the second man, miss him entirely because it's smoothbore and nails the neighbors dog. I have to resort to the cannon mounted at the top of the stairs loaded with grape shot, \"Tally ho lads\" the grape shot shreds two men in the blast, the sound and extra shrapnel set off car alarms. Fix bayonet and charge the last terrified rapscallion. He Bleeds out waiting on the police to arrive since triangular bayonet wounds are impossible to stitch up. Just as the founding fathers intended. ",
        "ERROR: Syntax error the platypus?? PERRY the syntax platypus?? ",
        "ERROR: Code 8008135. ",
        "ERROR: Something went wrong, and that means you're stupid. ",
        "ERROR: Answer is locked behind the \"Complete Answers\" DLC for $3.99. ",
        "ERROR: I made a severe and continuous lapse in my judgement, and I don’t expect to be forgiven. I’m simply here to apologize. ",
        "ERROR: RAID: Shadow Legends is an immersive online experience with everything you'd expect from a brand new RPG title. It's got an amazing storyline, awesome 3D graphics, giant boss fights, PVP battles, and hundreds of never before seen champions to collect and customize. ",
        "ERROR: User's mother is too fat. ",
        ]
    if prompt > -1:
        return hallucinations[prompt]
    else:
        return random.choice(hallucinations)