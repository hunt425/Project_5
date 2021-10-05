########################################################################
##
## CS 101 Lab
## Program # 5
## Hunter Tysdal
## htt4kk@umsystem.edu


def play_again() -> bool:
    choice = 'start'
    valid_yes = ['YES', 'Y']
    valid_no = ['NO', 'N']
    while not (choice in valid_no) or not (choice in valid_yes):

        choice = input('Would you like to play again?\n')
        choice = choice.upper()
        if choice in valid_yes:
            return True
        elif choice in valid_no:
            print('Have a good day!')
            return False

        else:
            print('That is not an acceptable answer')
            choice = input('Would you like to play again?\n')
            choice = choice.upper()
    ''' Asks the user if they want to play again, returns False if N or NO, and True if Y or YES.  Keeps asking until they respond yes '''


def get_wager(bank: int) -> int:
    wager = int(input('How many chips do you want to wager?\n'))
    if wager < 1 or wager > 100:
        while wager < 1:
            print('Too low of a value, you can only choose 1-100 chips')
            wager = int(input('How many chips do you want to wager?\n'))
            continue
        while wager > 100:
            print('Too low of a value, you can only choose 1-100 chips')
            wager = int(input('How many chips do you want to wager?\n'))
            continue

    ''' Asks the user for a wager chip amount.  Continues to ask if they result is <= 0 or greater than the amount they have '''

    return wager


def get_slot_results() -> tuple:
    ''' Returns the result of the slot pull '''
    import random

    reel1 = random.randint(1, 10)
    reel2 = random.randint(1, 10)
    reel3 = random.randint(1, 10)

    return reel1, reel2, reel3


def get_matches(reela, reelb, reelc) -> int:
    ''' Returns 3 for all 3 match, 2 for 2 alike, and 0 for none alike. '''
    if reel1 == reel2 or reel1 == reel3 or reel2 == reel3:
        matches = 2
    if reel1 == reel2 and reel2 == reel3:
        matches = 3
    if reel1 != reel2 and reel1 != reel3:
        matches = 0
    return matches


def get_bank() -> int:
    ''' Returns how many chips the user wants to play with.  Loops until a value greater than 0 and less than 101 '''
    bank = int(input('How many chips do you want to start with?\n'))
    while bank < 1 or bank > 100:
        if bank < 1:
            print('Too low of a value, you can only choose 1-100 chips')
            bank = int(input('How many chips do you want to wager?\n'))
        elif bank > 100:
            print('Too high of a value, you can only choose 1-100 chips')
            bank = int(input('How many chips do you want to wager?\n'))
    return bank


def get_payout(wager, matches):
    ''' Returns how much the payout is.. 10 times the wager if 3 matched, 3 times the wager if 2 match, and negative wager if 0 match '''
    if matches == 2:
        wager = wager * 3
    elif matches == 3:
        wager = wager * 10
    elif matches == 0:
        wager = -(wager)

    return wager


if __name__ == "__main__":

    playing = True
    while playing:
        bank = get_bank()
        original_bank = bank
        money_list = [original_bank]
        rounds = 0
        while bank > 0:
            wager = get_wager(bank)

            reel1, reel2, reel3 = get_slot_results()

            matches = get_matches(reel1, reel2, reel3)
            payout = get_payout(wager, matches)
            bank = bank + payout

            print("Your spin: {} {} {}".format(reel1, reel2, reel3))
            print("You matched {} reels".format(matches))
            print("You won/lost", payout)
            print("Current bank", bank)
            print()
            money_list.append(bank)
            rounds += 1
        maximum = max(money_list)
        print("You lost all", original_bank, "in", rounds, "spins")
        print("The most chips you had was", maximum)
        playing = play_again()