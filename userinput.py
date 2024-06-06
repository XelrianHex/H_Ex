town = {
    "room": {
        "bed": "A small wood framed :bed:. On top lays a squashed pillow and scratchy sheets.",
        "footlocker": "A rusted metal box. The lid is shut. I wonder what's in side?",
        "table": "A little wooden :table: on which sits an empty plate and a piece of :paper:",
        "paper": "'found you in the woods. You're safe. Be back soon.' It is not signed.",
        "door": "A wooden :door:, and apparently the only :exit:",
        "wall": "Do you stare at walls often?",
        "window": "Though hazy you can some one else's home and a few trees."
    },
    "roomnews": {
        "south": "A small :table: and wooden :door: are here",
        "east": "A :window: letting the sunlight in can be seen.",
        "west": "Just a :wall:.",
        "north": "The :bed: you're on and the :footlocker: are pressed neatly against this side."
    },
    "streets": {
        "stables": "Out front sits a sign that simply reads 'The Depo'",
        "house": "Much like the one you left, it is a small wood :house:",
        "market": "A wooden building with plenty of windows. A sign over head reads 'Market'."
    }
}

user = ""
print("""**You wake up in a strange room, on a small bed. 
your head is throbbing and the light pouring in isn't helping.
you sit up on and look around the room.""")
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
    elif "leave" == user:
        break
    else:
        print("invalid trick ass bitch")
