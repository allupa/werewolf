from villager import Villager

class Paladin(Villager):
    def protect(self, target):
        target.be_protected()

    def __repr__(self):
        return f'PlayerBase({self.name}, {self.bluff})'

    def __str__(self):
        return "Paladin"

