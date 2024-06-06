Character_List = []


def info():
    for (name, title) in char.items():
        print("%s is a %s" % (name, title))


Characters = {
    "Names": {
        "Don": "Villain",
        "Jax": "Medic",
        "Ann": "Mechanic"
    },
    "Locations": {
        "Depo": "Dawn-brick",
        "Medic Hall": "Fast-wind",
        "Alter": "Hairpin"
    }
}
char = Characters["Names"]

info()
