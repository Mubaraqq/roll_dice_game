import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    
    return roll

print("🎲 Welcome to the DICE ROYALE! 🎲")
print("Roll wisely... but don't get greedy!\n")


while True:
    players = input('Enter the number of players (2 - 4): ')
    
    if players.isdigit():
        players = int(players)
        
        if 2 <= players <= 4:
            break
        else:
            print('❌ Must be between 2 - 4 players')
    else:
        print('❌ Invalid, please try again!')


player_score = [0 for i in range(players)]

print(f"\n⭐ Let the games begin with {players} players! ⭐")
print("=" * 50)

#while max(player_score) < max_score:
    
for player_index in range(players):
    print(f'\n Player number {player_index + 1} turn has started!')
    #print(f'Your total score is: {player_score[player_index]}')
    print("-" * 30)
    
    current_score = 0
        
    while True:
        player_roll = input('\nWould you like to roll (y/n)? ')
            
        if player_roll.lower() != 'y':
            print(f'⏹️  Turn ended. Safe choice!')
            break
        
        value = roll()
        print(f'\n🎲 You rolled a: {value}')
        
        if value == 1:
            print('💥You rolled a 1! Your turn ends!')
            break
            
        else:
            current_score += value
            print(f'💰 Your current score is: {current_score}')
        
    player_score[player_index] += current_score
    print(f'⭐ Your total score is: {player_score[player_index]}\n')


# finding the winner 

for i, score in enumerate(player_score):
    print(f'👤 Player {i + 1}: {score} points')

winning_score = max(player_score)
winning_player = player_score.index(winning_score)
print(f'🏆 Player number {winning_player + 1} is the winner with a score of: {player_score[winning_player]}')
print("\n🎉 Thanks for playing! 🎉\n")