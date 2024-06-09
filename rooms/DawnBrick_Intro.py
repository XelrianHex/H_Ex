from rooms.depo import depo
from rooms.market import market
from dictionaries import Characters
from dictionaries import town


def scene1():
    user = ""
    print("""**You step outside and see now that you're in a small town or village even. Just across the way
    you see what looks like a :stable: and to the east is a couple of houses. Standing at the stable area is the
    stranger.""")

    while user != "exit":
        user = input().lower()
        if "houses" in user or "house" in user:
            print(town["streets"]["house"])
        elif "stable" in user:
            print(town["streets"]["stables"])
            break

    print("Stranger: Well, glad you decided to come on out! Name's :Don:")
    print("You got a name?")
    name = input()
    Characters["Names"][name] = "The fingers on the keys or the face behind the screen?"
    print(f"Don: Interesting name, say {name} you have any idea why we might have found you out in the woods?")
    print(f"{name}: ...")
    print("""Don: Didn't think so I had Ann take a look at you on her way through, 'bout the closest person to a medic
    we had at the time. Said you might have bumped your head or something but you seemed fine mostly.
    **Don gestures to the :stable: behind him**
    This is the :Depo: my partner and I run this place. Shipping all kinds of goods from here in :Dawnbrick: 
    all the way out to south Marshlyn.
    Now over there is the only :market: in town! it's not much but it has what we need and helps support the :Depo:
    I know you must be pretty confused but hopefully we can get all your questions answered along the way.
    
    Now I can offer you some work here at the :Depo:, or you can take a look around if you would like.""")

    user = ""
    while user != "exit":
        user = input().lower()
        if "dawnbrick" in user:
            print(Characters["Locations"]["DawnBrick"])
        elif "depo" in user:
            print(town["streets"]["stables"])
            depo()
            break
        elif "marshlyn" in user:
            print(Characters["Locations"]["Marshlyn"])
        elif "ann" in user:
            print(Characters["Names"]["Ann"])
        elif "don" in user:
            print(Characters["Names"]["Don"])
        elif "market" in user:
            print(town["streets"]["market"])
            market()
            break
        elif "houses" in user or "house" in user:
            print(town["streets"]["house"])
        else:
            print("Choose another option! Gosh!")
