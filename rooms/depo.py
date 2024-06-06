from characterlist import Character_List


def depo():
    options = ["1", "2", "3"]
    print(":Your walk to the depo was filled with thoughts of who you were,")
    print("where you were from or how you even got there.")
    print(":You arrived soon enough and found your self just outside of the castle walls at a horse stable:")
    print(":Several horses were in their stalls and even more were outside,")
    print("lined up and ready to haul goods to their destinations:")
    print("%s: Welcome to the depo! Here we ship out and bring back all the" % Character_List[1])
    print("finest goods with in the dominion.")
    print("And today you and I are going to take this fine steed to Downslett.")
    print(":%s gestured to one of the horses attached to a cart." % Character_List[1])
    print("Already packed and waiting for them to go.")
    
    print("options:1.Wait! why am I being thrown in to all this so fast?")
    print("options:2.Is this going to be a long trip?")
    print("options:3.:You look nervously at the horses, but get on the carriage anyway.")
    
    user_input = ""
    
    while user_input not in options:
        print(":Who knows what will happen, make a choice!")
        user_input = input()
        
        if user_input == "1":
            print(":%s gives you a stern look: Not here, not now..." % Character_List[0])
            print(":%s places a hand on your shoulder and guides you to the cart." % Character_List[0])
        # scene2()
        if user_input == "2":
            print(":%s sighs: Listen kid we can't be worried about these type of things." % Character_List[0])
            print("But if it's really of concern, you can sleep through most of it...")
        # scene2()
        if user_input == "3":
            print("%s: Its a fair distance, but there's plenty to look at along the way!" % Character_List[0])
