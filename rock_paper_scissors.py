import random


def play():
    users_move = input("What's your move - r, p or s: ")
    computers_move = random.choice(['r', 'p', 's'])

    if users_move == computers_move:
        return "That's a draw!"

    if is_win(users_move,computers_move):
        return "You won!"

    return "You lost :("


def is_win(user,computer):
    if (user == 'r' and computer == 'p') or (user == 'p' and computer == 's') or (user == 's' and computer == 'r'):
        return True


# Repeated code = bad programming
# if users_move == 'r':
#     if computers_move == 'p':
#         print("Computer chose p. You lost this round!")
#     elif computers_move == 'r':
#         print("Computer chose r. That's a draw!")
#     else:
#         print("Computer chose s. You won this round!")
# elif users_move == 'p':
#     if computers_move == 's':
#         print("Computer chose s. You lost this round!")
#     elif computers_move == 'p':
#         print("Computer chose p. That's a draw!")
#     else:
#         print("Computer chose r. You won this round!")
# else:
#     if computers_move == 'r':
#         print("Computer chose r. You lost this round!")
#     elif computers_move == 's':
#         print("Computer chose s. That's a draw!")
#     else:
#         print("Computer chose p. You won this round!")


print(play())
