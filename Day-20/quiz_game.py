score = 0

answer = input("What is the capital of India? ")

if answer.lower() == "new delhi":
    score += 1

answer = input("How many continents are there? ")

if answer == "7":
    score += 1

print("Your Score:", score, "/2")