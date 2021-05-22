'''
Create a Planet class that models attributes and methods of
a planet object.

Use the appropriate dunder method to get informative output with print()

'''

class Planet():
    pass

# take in a number 0-2 from the user that represents their hand
# generate a random number 0-2 to use for the computer's hand
# call the function get_hand to get the string representation of the user's hand
# call the function get_hand to get the string representation of the computer's hand
# call the function determine_winner to figure out who won
# print out the player hand and computer hand
# print out the winner

hand = int(input("Please enter a number between 0 - 2: "))
import random
def get_hand(hand):
    scissor = 0
    rock = 1
    paper = 2
    hand_computer = random.randint(0, 2)
    hand_player = hand
    return hand_player, hand_computer
print(get_hand(hand))

def determine_winner(get_hand):
    scissor = 0
    rock = 1
    paper = 2
    hand_computer = random.randint(0, 2)
    hand_player = hand
    if hand_player > hand_computer and hand_player != 2:
        winner = hand_player
    elif: hand_player < hand_computer and hand_computer != 0:
        winner = hand_computer
    elif: hand_player == hand_computer:
        print("Computer wins")
    return winner

print(determine_winner(get_hand))