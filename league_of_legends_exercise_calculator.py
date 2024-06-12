import random
from math import floor

def round_down(num: int) -> int:
    return int(floor(num / 10.0))

def main() -> None:
    con = input('Press Enter to start or enter -1 to end: ')

    exercise = ['Classic pushups', 'Wide pushups', 'Diamond pushups','Spiderman pushups',
                'Sit ups', 'Squats', 'Leg raises', 'Burpees', 'Lunges', 'Half crunches',
                'Full crunches', 'Alternating crunches', 'Calf raises', 'Punches']

    while True:
        if con == '-1':
            break

        deaths = input('Enter number of deaths: ')
        obj_missed = input('Enter number of objectives missed: ')

        cs_missed = round_down(int(input('Enter amount of CS missed: ')))
        reps = int(deaths) + int(obj_missed) + cs_missed

        print('For your punishment do ' + str(reps) + ' ' + exercise[random.randint(0, len(exercise) + 1)])

        con = input('Press Enter to continue or enter -1 to end: ')

if __name__ == '__main__':
    main()
