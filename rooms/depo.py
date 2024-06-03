def depo():
    options = []
    print(":Your walk to the depo was filled with thoughts of who you were, where you were from or how you even got there.")
    print(":You arrived soon enough and found your self just outside of the castle walls at a horse stable:")
    print(":Several horses were in their stalls and even more were outside, lined up and ready to haul goods to their desinations:")
    print("%s: Welcome to the depo! Here we ship out and bring back all the finest goods with in the domninon. And today you and I are going to take this fine steed to Downslett." % stranger)
    print(":%s gestured to one of the horses attatched to a cart. Already packed and waiting for them to go." % stranger)
    
    print("options:1.Wait! why am I being thrown in to all this so fast?")
    print("options:2.Is this going to be a long trip?")
    print("options:3.:You look nervously at the horses, but get on the carriage anyway.")
    
    UserInput = ""
    
    while UserInput not in options:
        print(":Who knows what will happen, make a choice!")
        UserInput = input()
        
        if UserInput == "1":
            print(":%s gives you a stern look: Not here, not now..." % stranger)
            print(":%s places a hand on your shoulder and guides you to the cart." % stranger)
            scene2()
        if UserInput == "2":
            print(":%s sighs: Listen kid we can't be worried about these type of things." % stranger)
            print("But if it's really of concern, you can sleep through most of it...")
            scene2()
        if UserInput == "3":
            print("%s: Its a fair distance, but there's plenty to look at along the way!" % stranger)