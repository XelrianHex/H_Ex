from rooms.DawnBrick_Intro import scene1
from dictionaries import town
from dictionaries import inventory
if __name__ == "__main__":
    user = ""
    print("""**You wake up in a strange room, on a small bed. 
    your head is throbbing and the light pouring in isn't helping.
    you sit up on and look around the room.**""")
    print("--North, South, East or West--\n")

    while user != "exit":
        user = input().lower()
        if "south" in user:
            print(town["roomnews"]["south"])
        elif "east" in user:
            print(town["roomnews"]["east"])
        elif "west" in user:
            print(town["roomnews"]["west"])
        elif "north" in user:
            print(town["roomnews"]["north"])
        elif "bed" in user:
            print(town["room"]["bed"])
        elif "search" in user and "footlocker" in user:
            print(town["room"]["flitems"])
            inventory.append("gold.5")
        elif "footlocker" in user:
            print(town["room"]["footlocker"])
        elif "table" in user:
            print(town["room"]["table"])
        elif "door" in user:
            print(town["room"]["door"])
        elif "paper" in user:
            print(town["room"]["paper"])
        elif "wall" in user:
            print(town["room"]["wall"])
        elif "window" in user:
            print(town["room"]["window"])
        elif "inventory" in user or "inv" in user:
            print(inventory)
        elif "exit" == user:
            break
        else:
            print("invalid trick ass bitch")

print("\n")
print("**Someone walks in to the room just before your hand touched the knob**")
print("""**A burly man with a serious look walks in, setting a packet on the :table:.\n
Stranger: Brought some bits of meat and a few bread slices. Ain't much but its better than nothing.
Come on out when you're ready, I'll explain what I can.""")
print("**The stranger walks out leaving you to :eat: or follow behind him.**")

user = ""
while user != "exit":

    user = input().lower()
    if "eat" in user:
        print("You quickly scarfed down the meal. The smell of it having reminded you how hungry you were!")
    elif "follow" in user:
        break
    elif "exit" in user:
        break
    else:
        print("We dont have time for that")

scene1()
