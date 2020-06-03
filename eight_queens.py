import time

from solvers import find_solutions_brute, find_solutions_less_brute
from utils import initialize_solutions_json

def main():
    N = 1
    while True:
        input("Press ENTER to begin solving {0}x{0} board: ".format(N))
        initialize_solutions_json(N)
        starttime = time.time()
        find_solutions_less_brute(N)
        time_elapsed = time.time() - starttime
        print("\tTook {0} seconds to solve the {1}x{1} board. \n".format(time_elapsed, N))
        ans = input("Press ENTER to continue, or type anything here to exit: ")
        if (ans == ""):
            N += 1
        else:
            break
        
if __name__ == '__main__':
    main()