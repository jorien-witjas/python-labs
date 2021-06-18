

# def get_hand(hand):
#     scissor = 0
#     rock = 1
#     paper = 2
#     # hand_computer = random.randint(0, 2)
#     return hand_player, hand_computer
# print(get_hand(hand_player))
import random
hand_player = ""
def determine_winner(hand_player):
    hand_player = int(input("Please enter a number between 0 - 2: "))
    hand_computer = random.randint(0, 2)
    print(hand_player, hand_computer)
    ty = "play again"
    scissor = 0
    rock = 1
    paper = 2
    # hand_computer = random.randint(0, 2)
    # hand_player = hand
    if hand_player > hand_computer and hand_computer == 0:
        winner = "you win"
    elif hand_player < hand_computer and hand_computer != 0:
        winner = "you loose"
    elif hand_player == hand_computer:
        winner = ty
    return winner

print(determine_winner(hand_player))

play_again = input("Would you like to play again? ")
while play_again == "yes":
    determine_winner(hand_player)
    print(determine_winner(hand_player))
