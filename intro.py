from rooms.scene1 import scene1

if __name__ == "__main__":

    print("You wake up in a strange bed within a rather small room.")
    print("A foot locker sits at the end of the bed and a little table just to your right.")
    print("Across to the left of the table is the door")
    print("\n")
    print(":Someone walks in to the room:")
    print("Stranger: with a raised eyebrow he ask 'You got a name? we're gonna get you started today'")
    name = input()
    print("Stranger: 'We'll, %s we've got some packages to get delivered." % name)
    print("So come on...I'll explain everything on the way.")
    scene1()
