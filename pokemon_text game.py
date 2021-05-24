# pokemon 1 move death match
# adapted from RPS
# pls no sue nintendo, pokemon company, or gamefreak

import random, sys
print('POKEMON: ONE MOVE WILD WEST STANDOFF')
print('PKMN Trainer Simone would like to battle.')

# these variables keep track the number of wins, losses and ties
wins = 0
losses = 0
ties = 0
while True: # the main game loop
    print('%s Wins, %s Losses, and %s Ties'%(wins, losses, ties))
    while True: #player input loop
        print('Please select your pokemon: (c)harizard, (v)enusaur, (b)lastoise, or  type in q to quit')
        playerMove = input()
        if playerMove == 'q':
            print('Thanks for playing!')
            sys.exit() # quit the program
        if playerMove == 'c'or playerMove == 'v' or playerMove == 'b':
            break # break out of player input loop
        #secret pokemon
        if playerMove == 'pikachu':
            print('PIKACHU hops off your shoulder ready to fight.')
            break # break out of the input loop
        elif playerMove == 'mew':
            print('SECRET POKEMON USED! MEW has appeared to join the fight.')
            break # break the player out of the input loop
        #easter egg
        if playerMove == 'yeehaw':
            print('(Hehe you found the easter egg... yeehaw!)')
        #if playerMove == null;
            #print('Please develop some reading comprehension, Erica.')

    # display what the player chose
    if playerMove == 'c':
        print('Go! CHARIZARD!')
    elif playerMove == 'v':
        print('Go! VENUSAUR!')
    elif playerMove == 'b':
        print('Go! BLASTOISE!')
    elif playerMove == 'pikachu':
        print('Go! PIKACHU!')
    elif playerMove == 'mew':
        print('Go! Mew!')

    # display what the computer chose
    randomNumber = random.randint(1,3)
    if randomNumber == 1:
        computerMove = 'c'
        print('PKMN Trainer Simone sent out CHARIZARD.')
    elif randomNumber == 2:
        computerMove = 'v'
        print('PKMN Trainer Simone sent out VENUSAUR.')
    elif randomNumber == 3:
        computerMove = 'b'
        print('PKMN Trainer Simone sent out BLASTOISE.')

    while True: #player input loop in battle
        print('Command select: (f)ight, (b)ag, (p)okemon, (r)un, or  type in q to quit')
        playerCommand = input()
        if playerCommand == 'q':
            sys.exit() # quit the program
        elif playerCommand == 'f': # or playerMove == 'v' or playerMove == 'b':
            break # break out of player input loop
        elif playerCommand == "r":            
            print("Can't escape. It's a trainer battle you dingus.")
        elif playerCommand == 'b':
            print('You have no items!')
        elif playerCommand == 'p':
            print("Your other POKEMON don't feel like fighting.")
        #easter egg
        if playerMove == 'tiddy':
            print('(Hehe you found the easter egg... tiddy.)')
        print("Don't be like this.")    

    # display and record the win/loss/tie:

    #tie
    if playerMove == computerMove:
        print("The two POKEMON are locked in battle. Let's just call this a tie because this could take a while...")
        ties = ties + 1
    #player wins
    #standard pokemon
    elif playerMove == 'c' and computerMove == 'v':
        print('CHARIZARD used FLAMETHROWER.')
        print("It's super effective!")
        print("The opposing VENUSAUR fainted!")
        wins = wins + 1
    elif playerMove == 'v' and computerMove == 'b':
        print('VENUSAUR used RAZOR LEAF.')
        print("It's super effective!")
        print("The opposing BLASTOISE fainted!")
        wins = wins + 1
    elif playerMove == 'b' and computerMove == 'c':
        print('BLASTOISE used HYDRO PUMP.')
        print("It's super effective!")
        print("The opposing CHARIZARD fainted!")
        wins = wins + 1
    #secret pokemon winning matchups -mew
    elif playerMove == 'mew' and computerMove == 'c':
        print('MEW used HYPERBEAM.')
        print("Critical hit!")
        print("The opposing CHARIZARD fainted!")
        wins = wins + 1
    elif playerMove == 'mew' and computerMove == 'b':
        print('MEW used HYPERBEAM.')
        print("Critical hit!")
        print("The opposing BLASTOISE fainted!")
        wins = wins + 1
    elif playerMove == 'mew' and computerMove == 'c':
        print('MEW used HYPERBEAM.')
        print("Critical hit!")
        print("The opposing CHARIZARD fainted!")
        wins = wins + 1
    #secret pokemon winning matchups -pikachu
    elif playerMove == 'pikachu' and computerMove == 'c':
        print('PIKACHU used THUNDERBOLT.')
        print("It's super effective!")
        print("The opposing CHARIZARD fainted!")
        wins = wins + 1
    elif playerMove == 'pikachu' and computerMove == 'b':
        print('PIKACHU used THUNDERBOLT.')
        print("It's super effective!")
        print("The opposing BLASTOISE fainted!")
        wins = wins + 1

    #player loses
    elif playerMove == 'c' and computerMove == 'b':
        print('BLASTOISE used HYDRO PUMP.')
        print("It's super effective!")
        print("CHARIZARD fainted!")
        losses = losses + 1
    elif playerMove == 'v' and computerMove == 'c':
        print('CHARIZARD used FLAMETHROWER.')
        print("It's super effective!")
        print("VENUSAUR fainted!")
        losses = losses + 1
    elif playerMove == 'b' and computerMove == 'v':
        print('VENUSAUR used RAZOR LEAF.')
        print("It's super effective!")
        print("BLASTOISE fainted!")
        losses = losses + 1

    #secret pokemon player loses -pikachu
    elif playerMove == 'pikachu' and computerMove == 'v':
        print('VENUSAUR used EARTHQUAKE.')
        print("It's super effective!")
        print("PIKACHU fainted!")
        losses = losses + 1
