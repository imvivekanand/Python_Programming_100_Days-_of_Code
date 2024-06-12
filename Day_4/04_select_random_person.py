names = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]

randomInt = random.randint(0, len(names)-1)
ran_names = names[randomInt]
print(f"{ran_names} is going to buy the meal today!")