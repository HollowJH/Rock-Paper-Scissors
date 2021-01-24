import random

options = ["rock", "paper", "scissors"]
user = options.index(input())
sys = random.randint(0, 2)

if user == sys:
    print(f"There is a draw ({options[sys]})")
elif user == 0 and sys == 2 or user == 1 and sys == 0 or user == 2 and sys == 1:
    print(f"Well done. The computer chose {options[sys]} and failed")
else:
    print(f"Sorry, but the computer chose {options[sys]}")
