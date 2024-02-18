import sys
import help
import practice

def main():
    
    command = sys.argv[1]

    if command == "practice":
        practice.practice()
    elif command == "game":
        practice.game()
    elif command == "game-easy":
        practice.gameEasy()
    elif command == "ls":
        help.ls()
    elif command == "cp":
        help.calc_point()
    else:
        print("error")
