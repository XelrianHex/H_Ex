import random
from characterlist import Character_List
from rooms.medichall import medic_hall
from rooms.scene1 import scene1

stranger = "Don"


def fight1():
    options = ["1", "2", "3"]
    minpt = 1
    maxpt = 100
    ch1 = (random.randint(minpt, maxpt)) * .5
    
    print(":Along the way you run into a couple of bandits:")
    print("Bandits:'Stop right there you dimwits! This section of road belongs to us!")
    print("A fee of 20g is needed to cross!!!")
    print(":%s chuckled: If you think the two of us are paying you a dime you got another thing comin'" % Character_List[0])
    print(":The Bandits readied their weapons!")
    print("1.Fight\n2.Run\n3.Cry")

    user_input = ""
    
    while user_input not in options:
        print("We don't have time for this! Make a choice!")
        user_input = input()

    if user_input == "1" and ch1 > 18:
        print(":You swing at the closest bandit")
        print(":With surprise you land an outstanding haymaker:")
        print(":As he trys to recover you look in time to see %s has already defeated the other and now turned to finish the last of them!:" % stranger)
        medic_hall()
    else:
        print(":You swing but the bandit dodges and lands a blow on your cheek with a deafing crack!:")
        print(":%s comes and finishes the guy off, picking you up and taking you the medic's hall:" % stranger)
        medic_hall()
    if user_input == "2":
        print(":You run the other way, stopping behind a tree and watching as %s gets beaten to death...:")
        scene1()
    if user_input == "3":
        print(":In the chaos you start crying! Filled with laughter the Bandit lands a blow across your face,")
        print("knocking you out.:")
        print(":You wake up in the medic's hall:")
        medic_hall()
