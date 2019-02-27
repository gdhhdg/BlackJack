import random

hearts = list()
clubs = list()
spades = list()
diamonds = list()
dealer_cards = list()
player_cards = list()
deck = list()
suit_name = ""
player_blackjack = None
player_win = None
dealer_blackjack = None
dealer_win = None

def shuffle():
    for x in range(1, 14):
        hearts.append(x)

    for x in range(1, 14):
        clubs.append(x)

    for x in range(1, 14):
        diamonds.append(x)

    for x in range(1, 14):
        spades.append(x)

shuffle()
deck = [hearts, clubs, diamonds, spades]

def get_first_card_suit():
    first_card_suit = random.choice(range(0, 3))
    if first_card_suit is 0:
        suit_name = "hearts"
        # first_suit_number = 0
        return 0
    elif first_card_suit is 1:
        suit_name = "clubs"
        # first_suit_number = 1
        return 1
    elif first_card_suit is 2:
        suit_name = "diamonds"
        # first_suit_number = 2
        return 2
    elif first_card_suit is 3:
        suit_name = "spades"
        # first_suit_number = 3
        return 3

# Number of the suit to pull from
# first_suit_number = get_first_card_suit()

# card number to pop from the deck
# first_card_number = get_card_number()

def deal_a_card():
    first_suit_number = random.choice(range(0, 3))
    num = random.choice(range(1, 13))
    try:
        deck[random.choice(range(0, 3))].pop(random.choice(range(1, 13)))
    except Exception:
        #print("deal_a_card error")
        deck[random.choice(range(0, 3))].pop(random.choice(range(1, 13)))
    except Exception:
        #print("deal_a_card error 2")
        deck[random.choice(range(0, 3))].pop(random.choice(range(1, 13)))
    except Exception:
        #print("deal_a_card error 3")
        deck[random.choice(range(0, 3))].pop(random.choice(range(1, 13)))
    if first_suit_number is 0:
        suit_name = "hearts"
        # first_suit_number = 0
        # return 0
    elif first_suit_number is 1:
        suit_name = "clubs"
        # first_suit_number = 1
        # return 1
    elif first_suit_number is 2:
        suit_name = "diamonds"
        # first_suit_number = 2
        # return 2
    elif first_suit_number is 3:
        suit_name = "spades"
        # first_suit_number = 3
        # return 3
    if num is 1:
        num = "Ace"
    elif num is 11:
        num = "Jack"
    elif num is 12:
        num = "Queen"
    elif num is 13:
        num = "King"
    else:
        num = num
    # print(str(num) + " of " + suit_name)

    return {"suit_name": suit_name, "num": num}

#print(deck)

# getting dealer's cards
def get_dealer_cards():
    try:
        dealer_cards.append(deal_a_card())
        dealer_cards.append(deal_a_card())
    except IndexError:
        dealer_cards.append(deal_a_card())
        dealer_cards.append(deal_a_card())
        #print("error 1")
    except IndexError:
        dealer_cards.append(deal_a_card())
        dealer_cards.append(deal_a_card())
        #print("error 2")
    except IndexError:
        dealer_cards.append(deal_a_card())
        dealer_cards.append(deal_a_card())
        #print("error 3")
    return dealer_cards

# get_dealer_cards()
# print("dealer's cards are " + str(dealer_cards))
#print(deck)

def get_player_cards():
    try:
        player_cards.append(deal_a_card())
        player_cards.append(deal_a_card())
    except IndexError:
        player_cards.append(deal_a_card())
        player_cards.append(deal_a_card())
    except IndexError:
        player_cards.append(deal_a_card())
        player_cards.append(deal_a_card())
    except IndexError:
        player_cards.append(deal_a_card())
        player_cards.append(deal_a_card())

# get_player_cards()

def game_run():
    answer = "y"
    #while answer == "y":
    get_player_cards()
    get_dealer_cards()
    print("Dealer\'s card is " + str(dealer_cards[0].get('num'))+ " of " + str(dealer_cards[0].get('suit_name')) )
    print("your cards is " + str(player_cards[0].get('num')) + " of " + str(player_cards[0].get('suit_name')))
    player_count = None
    dealer_count = None
    answer = input("Hit or Stay?")
    card_value_list = list()
    new_card_value_list = list()
    dealer_value_list = list()
    new_dealer_value_list = list()
    ace = False
    royal = False
    global dealer_blackjack
    global player_blackjack
    dealer_bust = False
    global player_win
    global dealer_win
    i = 1
    while answer == "hit":
        try:
            player_cards.append(deal_a_card())
        except Exception:
            #print("Player Card Deal Error")
            player_cards.append(deal_a_card())

        print("Your new card is " + str(player_cards[i].get('num')) + " of " + str(player_cards[i].get('suit_name')))
        i += 1
        answer = input("Hit or Stay?")
    else:
        i += 1
        for i in range(i):
            card_value_list.append(player_cards[i].get('num'))

    #print(card_value_list)
    for c in card_value_list:
        if c == "Ace":
            new_card_value_list.append(1)
        elif c == "Jack":
            new_card_value_list.append(11)
        elif c== "Queen":
            new_card_value_list.append(12)
        elif c == "King":
            new_card_value_list.append(13)
        else:
            new_card_value_list.append(c)


    r = 0
    #print("dealer card lenght is "+ str(len(dealer_cards)))
    for r in range(len(dealer_cards)):
        dealer_value_list.append(dealer_cards[r].get('num'))
        i+=1
    c = 0
    for c in dealer_value_list:
        if c == "Ace":
            new_dealer_value_list.append(1)
        elif c == "Jack":
            new_dealer_value_list.append(10)
        elif c== "Queen":
            new_dealer_value_list.append(10)
        elif c == "King":
            new_dealer_value_list.append(10)
        else:
            new_dealer_value_list.append(c)

    #print("dealer cards are " + str(dealer_cards))
    dealer_sum = sum(new_dealer_value_list)
    print("dealer total is " + str(dealer_sum))


    for face in new_dealer_value_list:
        if face is 1:
            ace = True
        if face is 10:
            royal = True
    if ace == True and royal == True:
        dealer_blackjack = True
        dealer_sum = 21
        #print("Dealer got Blackjack!")

    for face in new_dealer_value_list:
        if face is 1 and dealer_sum <= 10:
            dealer_sum = dealer_sum + 10

    while dealer_sum <= 17:
        dealer_sum = dealer_sum + random.choice(range(1,11))
    if dealer_sum == 21:
        dealer_blackjack = True
    if dealer_sum > 21:
        dealer_bust = True
        print("Dealer got " + str(dealer_sum))
        dealer_win == False

    if dealer_blackjack is True:
        print("Dealer got Blackjack!")
    if dealer_bust is True:
        print("Dealer busted!")
    player_sum = sum(new_card_value_list)
    print("Your total is " + str(player_sum))

    if player_sum <= 21 and player_sum > dealer_sum:
        player_win == True
        print("You Win!")
        #return player_win == True

    else:
        dealer_win = True
        print("The Dealer Won!")
        #return dealer_win == True

    if dealer_blackjack == True:
        dealer_win == True
        player_win == False
        print("The Dealer Got Blackjack!")
        #return dealer_blackjack == True
    if player_win == True:
        print("You Won!")
    if player_win == False:
        print("You Lost!")
        #answer = input("Play again? y/n")

answer = "y"

#   ~~~~~~~Betting~~~~~~~~~~~~
def bet(game_run):
    player_stack = int(20)
    player_stack = player_stack-player_bet
    if player_blackjack is True:
        player_stack = player_stack*2
    elif player_win is True:
        player_stack = player_stack*1.5
    print("your stack is " + str(player_stack))



while answer is "y":
    #player_bet = int(input("enter a number"))
    #bet(game_run())
    #print(player_win)
    #print(dealer_win)
    game_run()
    answer = input("Play again? y or n    ")


