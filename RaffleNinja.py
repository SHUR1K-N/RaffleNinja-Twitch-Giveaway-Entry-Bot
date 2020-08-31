import time; import os
from colorama import init
from termcolor import colored
from tqdm import tqdm
import random; import winsound
import pynput

keyboard = pynput.keyboard.Controller()
key = pynput.keyboard.Key

BANNER1 = colored('''
             ██▀███   ▄▄▄        █████▒ █████▒██▓    ▓█████  ███▄    █  ██▓ ███▄    █  ▄▄▄██▀▀▀▄▄▄
            ▓██ ▒ ██▒▒████▄    ▓██   ▒▓██   ▒▓██▒    ▓█   ▀  ██ ▀█   █ ▓██▒ ██ ▀█   █    ▒██  ▒████▄
            ▓██ ░▄█ ▒▒██  ▀█▄  ▒████ ░▒████ ░▒██░    ▒███   ▓██  ▀█ ██▒▒██▒▓██  ▀█ ██▒   ░██  ▒██  ▀█▄
            ▒██▀▀█▄  ░██▄▄▄▄██ ░▓█▒  ░░▓█▒  ░▒██░    ▒▓█  ▄ ▓██▒  ▐▌██▒░██░▓██▒  ▐▌██▒▓██▄██▓ ░██▄▄▄▄██
            ░██▓ ▒██▒ ▓█   ▓██▒░▒█░   ░▒█░   ░██████▒░▒████▒▒██░   ▓██░░██░▒██░   ▓██░ ▓███▒   ▓█   ▓██▒
            ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░ ▒ ░    ▒ ░   ░ ▒░▓  ░░░ ▒░ ░░ ▒░   ▒ ▒ ░▓  ░ ▒░   ▒ ▒  ▒▓▒▒░   ▒▒   ▓▒█░
              ░▒ ░ ▒░  ▒   ▒▒ ░ ░      ░     ░ ░ ▒  ░ ░ ░  ░░ ░░   ░ ▒░ ▒ ░░ ░░   ░ ▒░ ▒ ░▒░    ▒   ▒▒ ░
              ░░   ░   ░   ▒    ░ ░    ░ ░     ░ ░      ░      ░   ░ ░  ▒ ░   ░   ░ ░  ░ ░ ░    ░   ▒
               ░           ░  ░                  ░  ░   ░  ░         ░  ░           ░  ░   ░        ░  ░
               ''', 'blue')
BANNER2 = colored('''                                RaffleNinja: The Twitch Giveaway/Raffle Entry Bot''', 'red')
BANNER3 = colored('''                               ---------------------------------------------------''', 'blue')


def printBanner():
    init()
    print(BANNER1), print(BANNER2), print(BANNER3)


def windowChange():
    keyboard.press(key.alt)
    repetitions = 1
    for iterations in range(1, windows):
        while repetitions <= iterations:
            (keyboard.press(key.tab))
            (keyboard.release(key.tab))
            time.sleep(0.2)
            repetitions += 1
    keyboard.release(key.alt)


def enter(element):
    if keyword == "":
        space = ""
    else:
        space = " "
    keyboard.type(keyword + space + element)
    keyboard.press(key.enter)
    keyboard.release(key.enter)
    time.sleep(0.1)


def generate(minunit, maxunit):
    top = maxunit - minunit
    tempList = []
    while (len(tempList) < top):
        randNum = str(random.randrange(minunit, maxunit, 1))
        if randNum not in tempList:
            tempList.append(randNum)
    return(tempList)


def countdown():
    clrscr()
    print("\nPress Enter when ready to begin a 10 second countdown...")
    if (windows == 1):
        print(f"Use this countdown time to initialize the {windows} text field by clicking once in it.", end="")
    else:
        print(f"Use this countdown time to initialize the {windows} text fields by clicking once in each of them.", end="")
    input()
    for int in range(1, 10):
        winsound.Beep(350, 800)
        time.sleep(0.2)
    winsound.Beep(800, 800)
    time.sleep(0.2)


def clrscr():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')
    printBanner()


############### Main ###############

if __name__ == "__main__":

    printBanner()

    while (True):
        try:
            windows = int(input("\nInput the number of accounts (windows) entering through (Default = 1): ") or 1)
            delay = float(input("Input the chat delay in seconds (Default = 0.3s): ") or 0.3)

            if (windows < 1):
                windows = 1
            break
        except:
            clrscr()
            print("\nInvalid entry (not a float/integer). Please try again.\n")
            continue

    keyword = input(("Input the chat keyword (Default = blank): ") or "")

    while (True):
        print("\n\nMethods:-")
        print("1. Enter a custom range of integers\n2. Supply a dictionary file")
        decision = input("\nSelect method number: ")

        if (decision == "1"):
            while (True):
                try:
                    minunit = int(input("\nEnter the minimum value (Default = 1): ") or 1)
                    maxunit = int(input("Enter the maximum value: "))
                    break

                except:
                    clrscr()
                    print("\nInvalid entry (not an integer). Please try again.\n")
                    continue

            if maxunit > minunit:
                maxunit += 1 # To include the maxunit integer as well (added this far in to not interfere with file naming string)
                tempList = generate(minunit, maxunit)

                countdown()
                for index, element in enumerate(tempList, start=1):
                    enter(element)
                    if (windows > 1):
                        windowChange()
                        time.sleep(0.1)
                    if ((index) % windows == 0):
                        time.sleep(delay)
                    elif (windows == 1):
                        continue

            elif (minunit == maxunit):
                clrscr()
                print("\nThe minimum value cannot be equal to the maximum value.")
                continue

            elif (minunit > maxunit):
                clrscr()
                print("\nThe minimum value cannot be greater than the maximum value.")
                continue

        elif (decision == "2"):
            while (True):

                dict = input("\nEnter dictionary file path here: ")
                tempList = []

                if (os.path.isfile(dict) is True):
                    break
                else:
                    clrscr()
                    print("\nEither file does not exist or invalid path entered. Try again.\n")
                    continue

            with open(dict, "r") as file:
                for line in file:
                    line = line.strip()
                    tempList.append(line)
            countdown()
            for index, element in enumerate(tempList, start=1):
                enter(element)
                windowChange()
                time.sleep(0.15)
                if ((index) % 2 == 0):
                    time.sleep(delay)
                else:
                    continue

        else:
            clrscr()
            print("\nInvalid entry. Choose either option 1 or 2. Try again.\n")
            continue
        break

    clrscr()
    print("\n\nThe task completed successfully.")
    print("Press Enter to exit.")
    input()
