import random


player_array = [
    "Jose",
    "Pedro",
    "Laura",
    "Rachel",
    "Mark",
    "Frederic",
    "Juan",
    "Philip",
    "Monica",
    "Phoebe",
]


def simulate_night(villagers, werewolves, stats):
    # print(f'Simulating night with {villagers} as villagers and {werewolves} as ww')
    while True:
        choices_array = random.choices(villagers, k=len(werewolves))
        if len(set(choices_array)) == 1:
            # print(f'Goodbye {choices_array[0]} (night)')
            if stats[choices_array[0]] <= random.randint(1,100):
                villagers.remove(choices_array[0])
                break
    # print(f'Returning villagers {villagers} (night)')
    return villagers


def simulate_day(villagers, werewolves, stats):
    # print(f'Simulating day with {villagers} as villagers and {werewolves} as ww')
    all = villagers + werewolves
    while True:
        choices_array = random.choices(all, k=len(werewolves))
        if len(set(choices_array)) == 1:
            choice = choices_array[0]
            # print(f'Goodbye {choice} (day)')
            if choice in werewolves:
                if stats[choice] <= random.randint(1,100):
                    werewolves.remove(choice)
                    break
            else:
                if stats[choice] <= random.randint(1,100):
                    villagers.remove(choice)
                    break
    return werewolves, villagers

def game_logic(villagers, werewolves, stats):
    while len(werewolves) <= len(villagers):
        villagers = simulate_night(villagers, werewolves, stats)
        if not villagers:
            return "Werewolves won"
        werewolves, villagers = simulate_day(villagers, werewolves, stats)
        if not werewolves:
            return "Villagers won"
    return "Werewolves won"

def main():
    tally = {'Werewolves': 0, 'Villagers': 0}
    stats = {}
    for x in range(5):
        for x in range(1000):
            werewolves = random.sample(player_array, 2)
            villagers = [n for n in player_array if n not in werewolves]
            c_werewolves = list(werewolves) #copy
            c_villagers = list(villagers) #copy
            for n in player_array:
                stats[n] = random.randint(1,100)
            result = game_logic(villagers, werewolves, stats)
            if result == "Werewolves won":
                tally['Werewolves'] += 1
            else:
                tally['Villagers'] += 1
        print(tally)
        print(f'Wolves for this game were {c_werewolves} \n and villagers were {c_villagers}')
        print('Stats for the last game were')
        for k, v in stats.items():
            if k in werewolves or k in villagers:
                print(f'{k} {v} -- Survived')
            else:
                print(f'{k} {v} -- Died')
        print(result)
        tally = {'Werewolves': 0, 'Villagers': 0}
    return 0

main()
