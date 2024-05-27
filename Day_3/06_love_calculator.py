print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
combined_name = (name1 + name2).lower()
true_count = 0
love_count = 0
for i in combined_name:
  if i == "t" or i == "r" or i == "u" or i == "e":
    true_count += 1
  if i == "l" or i == "o" or i == "v" or i == "e":
    love_count += 1

total = str(true_count) + str(love_count)
love_score = int(total)

if love_score > 90 or love_score < 10:
  print(f"Your score is {total}, you go together like coke and mentos.")
elif love_score > 40 and love_score < 50:
  print(f"Your score is {total}, you are alright together.")
else:
  print(f"Your score is {total}.")