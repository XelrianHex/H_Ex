from rooms.depo import depo
from rooms.fight1 import fight1
from characterlist import Characters
stranger = "Don"



def scene1():
    options = ["1", "2"]

    print("Stranger: My name is %s I'm head of the delivery depo here in Marshlyn" % stranger)
    print("We found you unconscious and stranded out in the woods of the trade road.")
    print("What were you doing out that way any how?")
    print("\n")
    print("1. I don't know...")
    print("2. I think...I think I hit my head, I can't remember anything!")
    
    user_input = ""
    
    while user_input not in options:
        print("Please select options 1 or 2")
        user_input = input()
        if user_input == "1":
            print("%s: Ah, well I'm sure we can figure it out sooner or later" % stranger)
            print("let's just get to the depo first")
            depo()
        elif user_input == "2":
            print("%s: Hmm, Let me see.'Don looks at your head all over' " % stranger)
            print("You don't seem to be injured anywhere...")
            print("Let's get to the medics hall just in case")
            fight1()
        else:
            print("only the selections '1' or '2' will work.")
