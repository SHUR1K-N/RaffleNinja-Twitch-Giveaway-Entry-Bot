import time
from colorama import init
from termcolor import colored
from tqdm import tqdm
import random; import winsound
import pynput

keyboard = pynput.keyboard.Controller()
key = pynput.keyboard.Key
correctInput = False

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
BANNER2 = colored('''                                  RaffleNinja: The Twitch Giveaway/Raffle Entry Bot''', 'red')
BANNER3 = colored('''                                 ---------------------------------------------------''', 'blue')


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
    print("\nPress Enter when ready to begin 10 second countdown...", end="")
    input()
    for int in range(0, 3):
        winsound.Beep(350, 800)
        time.sleep(0.2)
    winsound.Beep(800, 800)
    time.sleep(0.2)


############### Main ###############

if __name__ == "__main__":

    printBanner()

    while (correctInput is False):
        try:
            windows = int(input("Input the number of accounts (windows) entering through (Default = 1): ") or 1)
            delay = float(input("Input the chat delay in seconds (Default = 0.3s): ") or 0.3)
            keyword = input(("Input the chat keyword (Default = blank): ") or "")

            print("\nMethods:-")
            print("1. Enter a custom range of integers\n2. Supply a dictionary file")
            decision = int(input("\nSelect method number: "))

            if (decision == 1):
                minunit = int(input("\nEnter the minimum value (Default = 1): ") or 1)
                maxunit = int(input("Enter the maximum value: "))

                countdown()

                if maxunit > minunit:
                    maxunit += 1 # To include the maxunit integer as well (added this far in to not interfere with file naming string)
                    tempList = generate(minunit, maxunit)

                    for index, element in enumerate(tempList, start=1):
                        enter(element)
                        if (windows > 1):
                            windowChange()
                            time.sleep(0.1)
                        if ((index) % windows == 0):
                            time.sleep(delay)
                        else:
                            continue

                elif (minunit == maxunit):
                    print("\nThe minimum value cannot be equal to the maximum value.")

                elif (minunit > maxunit):
                    print("\nThe minimum value cannot be greater than the maximum value.")

                correctInput = True

            elif (decision == 2):
                dict = input("\nEnter dictionary file path here: ")
                tempList = []

                countdown()

                with open(dict, "r") as file:
                    for line in file:
                        line = line.strip()
                        tempList.append(line)
                    file.close()
                for index, element in enumerate(tempList, start=1):
                    enter()
                    windowChange()
                    time.sleep(0.15)
                    if ((index) % 2 == 0):
                        time.sleep(delay)
                    else:
                        continue

                correctInput = True

            else:
                print("\nInvalid entry. Choose either option 1 or 2. Try again.\n")
                continue
        except:
            print(e)
            print("\nOne of more of the inputs are invalid. This can happen when any spaces or other characters have been entered instead of numbers. Please try again.\n")
            continue

    print("\n\nThe task completed successfully.")
    print("Press any key to exit.")
    input()
