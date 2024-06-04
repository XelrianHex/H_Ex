class Player:
    def __init__(self, name, lvl):
        self.name = name
        self.lvl = lvl

    def lvl(self):
        return self.lvl

    def __str__(self):
        return f"Stats: Name: {self.name}, Lvl: {self.lvl}"



