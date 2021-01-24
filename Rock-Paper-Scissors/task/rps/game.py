import random
options = ["rock", "paper", "scissors"]

while True:
    user = input()
    sys = random.randint(0, 2)
    if user == "!exit":
        print("Bye!")
        break
    else:
        user = options.index(user) if user in options else None
    if user == sys:
        print(f"There is a draw ({options[sys]})")
    elif user == 0 and sys == 2 or user == 1 and sys == 0 or user == 2 and sys == 1:
        print(f"Well done. The computer chose {options[sys]} and failed")
    elif sys == 0 and user == 2 or sys == 1 and user == 0 or sys == 2 and user == 1:
        print(f"Sorry, but the computer chose {options[sys]}")
    else:
        print("Invalid input")
