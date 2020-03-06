import sys, re

def main():
    if len(sys.argv) is not 2:
        print("ERROR")
        return
    try:
        nb = int(sys.argv[1])
        if nb == 0:
            print("I'm Zero.")
        elif nb % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    except ValueError:
        print("ERROR")

if __name__ == "__main__":
    main()
