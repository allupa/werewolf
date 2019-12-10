from villager import Villager


class Seer(Villager):

    def detect(self, target):
        print(target)

    def __repr__(self):
        return f'PlayerBase({self.name}, {self.bluff})'

    def __str__(self):
        return "Seer"
