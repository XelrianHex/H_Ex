import random
stranger = "Don"


def fight1():
    options = ["1", "2", "3"]
    
    print(":Along the way you run into a couple of bandits:")
    print("Bandits:'Stop right there you dimwits! This section of road blongs to us! A fee of 20g is needed to cross!!!")
    print(":%s chuckled: If you think the two of us are paying you a dime you got another thing comin'" % stranger)
    print(":The Bandits readied their weapons!")
    print("1.Fight\n2.Run\n3.Cry")

    minpt = 1
    maxpt = 100
    UserInput = ""
    
    while UserInput not in options:
        print("We don't have time for this! Make a choice!")
        UserInput = input()
        CH1 = (random.randint(minpt,maxpt)) * .5
    if UserInput == "1" and CH1 > 18:
        print(":You swing at the closest bandit")
        print(":With surprise you land an outstanding haymaker:")
        print(":As he trys to recover you look in time to see %s has already defeated the other and now turned to finish the last of them!:" % stranger)
        medic_hall()
    else:
        print(":You swing but the bandit dodges and lands a blow on your cheek with a deafing crack!:")
        print(":%s comes and finishes the guy off, picking you up and taking you the medic's hall:" % stranger)
        medic_hall()
    if UserInput == "2":
        print(":You run the other way, stopping behind a tree and watching as %s gets beaten to death...:")
        scene1()
    if UserInput == "3":
        print(":In the chaos you start crying! Filled with laughter the Bandit lands a blow across your face, knocking you out.:")
        print(":You wake up in the medic's hall:")
        medic_hall()
