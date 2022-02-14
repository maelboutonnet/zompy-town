import random

nb_of_citizen = 40
research_completion_rate = 0
NB_OF_DAYS_MAX = 40

for day in range(NB_OF_DAYS_MAX):
    print('It\'s day #' + str(day) + ' of the zombie apocalypse')
    print('There are only ' + str(NB_OF_DAYS_MAX - day) + ' days left to find the cure')
    print('Cure completion: ' + str(research_completion_rate) + '%')

    print('How many citizen will protect the town ?')
    nb_of_defenders = int(input())

    while(nb_of_defenders > nb_of_citizen):
        print('You only have ' + str(nb_of_citizen) +' citizens, how many will protect the town ?')
        nb_of_defenders = int(input())

    nb_of_scientists = nb_of_citizen - nb_of_defenders
    print('Summary :')
    print(str(nb_of_defenders) + ' citizens will defend the town')
    print(str(nb_of_scientists) + ' will search a cure')

    nb_of_zombies = random.randint(1, day+2)
    print(str(nb_of_zombies) + ' detected nearby')

    def_score = 0
    for human_count in range(nb_of_defenders):
        def_score += random.randint(1,4)

    dead_people = nb_of_zombies - def_score

    if (dead_people > 0):
        print('Your defenses were too weak ! Zombies are in the town')
        print(str(dead_people) + ' were killed during the night')
    else:
        print('Your defenses held on during the night !')
        print('Your citizens are safe for today')

    nb_of_scientists -= dead_people

    if (nb_of_scientists > 0):
        for human_count in range(nb_of_scientists):
            research_completion_rate += random.randint(0,2)

    if (research_completion_rate >= 100):
        print('Congratulation, the cure is complete!')
        break

    if (day == NB_OF_DAYS_MAX):
        print('Sadly, you didn\'t find the cure in time :(')
