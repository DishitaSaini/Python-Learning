import random
# Rock
rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

# person = input("Choose rock, paper or scissors? ").lower()
# if person == "rock":
#     print(Rock)
# elif person == "paper":
#     print(Paper)
# elif person == "scissors":
#     print(Scissors)
# else:
#     print("Value not applicable.")

# game = ["rock", "paper", "scissors"]
# computer = random.choice(game)

# print("Computer chose:", computer)

# if computer == "rock":
#     print(Rock)
# elif computer == "paper":
#     print(Paper)
# elif computer == "scissors":
#     print(Scissors)

# if computer == "rock" and person == "paper":
#     print("Computer Wins!")
    
# elif computer == "scissors" and person == "paper":
#     print("Computer Wins!")

# elif computer == "paper" and person == "rock":
#     print("Computer Wins!")
# elif computer == person:
#     print("Game is Draw.")
# else:
#     print("Person Wins!")

#professors code
game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors: "))

computer_choice = random.randint(0, 2)

# Check if user's choice is valid
if user_choice >= 3 or user_choice < 0:
    print("You have typed an invalid number. YOU LOSE!")

else:
    # Print user's choice
    print("You chose:")
    print(game_images[user_choice])

    # Print computer's choice
    print("Computer chose:")
    print(game_images[computer_choice])

    # Decide the winner
    if user_choice == 0 and computer_choice == 2:
        print("You Win!")

    elif computer_choice == 0 and user_choice == 2:
        print("You Lose!")

    elif computer_choice > user_choice:
        print("You Lose!")

    elif user_choice > computer_choice:
        print("You Win!")

    else:
        print("It's a Draw!")