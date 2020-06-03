import json
import os

while True:
    available_files = ''.join(os.listdir("SOLUTIONS"))
    dimension = int(input("Choose a dimension to see solutions for: "))
    while (str(dimension) not in available_files):
        dimension = int(input("Please choose a dimension that we have calculated already: "))

    with open("SOLUTIONS/{}_solutions.json".format(dimension)) as f:
        solution_dict = json.load(f)

    solutions = list(solution_dict.keys())

    while True:
        if (len(solutions) != 0):
            print("There are {} solutions available to view.".format(len(solutions)))
            solution_choice = int(input("Which solution would you like to choose?: "))
            while solution_choice not in list(range(1,len(solutions)+1)):
                solution_choice = int(input("Please choose a solution between 1 and {}: ".format(len(solutions))))
            print('\n' + solutions[solution_choice - 1])
            keepBrowsing = input("Would you like to continue browsing solutions for this dimension? [y/n]: ").lower()
            while keepBrowsing not in ['y','n']:
                keepBrowsing = input("Please enter either y or n: ").lower()
            if (keepBrowsing == 'y'):
                continue
            elif (keepBrowsing == 'n'):
                break
        else:
            print("Sorry, there are no solutions for this board size. Please try another. ")
            break

    keepBrowsing = input("Would you like to check solutions for another dimension? [y/n]: ").lower()
    while keepBrowsing not in ['y', 'n']:
        keepBrowsing = input("Please enter either y or n: ").lower()
    
    if (keepBrowsing == 'y'):
        continue
    elif (keepBrowsing == 'n'):
        input("Press ENTER to exit and have a nice day! Also please implement a better solution than this one it is god awful")
        break

        