class PlayerBase:
    def __init__(self, name, bluff):
        self.name = name
        self.bluff = bluff
        self.__protected = False

    def __repr__(self):
        return f'PlayerBase({self.name}, {self.bluff})'

    def __str__(self):
        return f'Playername: {self.name} | Bluff: {self.bluff}'

