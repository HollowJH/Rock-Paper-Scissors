import random
options = ["rock", "paper", "scissors"]

name = input("Enter your name: ").strip()
print(f"Hello, {name}")
rating = open("rating.txt")
read = rating.readlines()
lines = [i.strip("\n").split(" ") for i in read]
names = [i[0] for i in lines]
rat = [i[1] for i in lines]
scores = dict([(names[i], rat[i]) for i in range(len(names))])
score = int(scores[name]) if name in scores.keys() else 0
rating.close()

while True:
    user = input(score).strip()
    sys = random.randint(0, 2)
    if user == "!exit":
        if name in scores.keys():
            scores[name] = score
            lines = [f"{x} {y}\n" for x in names for y in scores.values()]
            rating = open("rating.txt", "w")
            rating.writelines(lines)
            rating.close()
        else:
            rating = open("rating.txt", "a")
            rating.write(f"{name} {score}\n")
            rating.close()
        print("Bye!", scores)
        break
    elif user == "!rating":
        print(f"Your rating: {score}")
        continue
    else:
        user = options.index(user) if user in options else None
    if user == sys:
        score += 50
        print(f"There is a draw ({options[sys]})")
    elif user == 0 and sys == 2 or user == 1 and sys == 0 or user == 2 and sys == 1:
        score += 100
        print(f"Well done. The computer chose {options[sys]} and failed")
    elif sys == 0 and user == 2 or sys == 1 and user == 0 or sys == 2 and user == 1:
        print(f"Sorry, but the computer chose {options[sys]}")
    else:
        print("Invalid input")
