def rps():
  #Inputs
  import random
  import re
  choice = input("Please choose either rock, paper, or scissors: ").lower() 
  if not bool(re.match("[rock|paper|scissors|]", choice)):
    print("You're dumb.")
    return None
  #Processes
  result = ""
  pc_choice = ""
  n = random.randint(1,3)
  if n == 1:
    pc_choice = "rock"
  elif n == 2:
    pc_choice = "scissors"
  else:
    pc_choice = "paper"
  if choice == pc_choice:
    result = "It's a tie!"
  elif choice == "rock" and pc_choice == "scissors":
    result = "You win!"
  elif choice == "scissors" and pc_choice == "paper":
    result = "You win!"
  elif choice == "paper" and pc_choice == "rock":
    result = "You win!"
  else:
    result = "You lose!"
  #Outputs
  print(result)

rps()