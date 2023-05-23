import random

players = ["Martin", "Craig", "Sue", "Claire", "Dave", "Alice", "Luciana",
           "Harry", "Jack", "Rose", "Lexi", "Maria", "Thomas", "James", "William",
           "Ada", "Grace", "Jean", "Marissa", "Alan"]

print("Welcome to Team Allocator!")
numplayers = input("How many players on each team? ")

while True:

    random.shuffle(players)
    teams = players
    numteams = len(players)/int(numplayers)
    if (len(players)%int(numplayers)>0):
        remainder = len(players)%int(numplayers)
    firstplayer = 0
    for counter in range (0, int(numteams)):
        print("Team " + str(counter+1) + ": ")
        for counter2 in range(firstplayer,int(numplayers)+firstplayer):
            print(teams[counter2])
        firstplayer=firstplayer+int(numplayers)
    print("Team " + str(counter+2) + ": ")
    print(remainder)           

    response = input("Pick teams again? Type y or n: ")
    if response == "n":
        break
