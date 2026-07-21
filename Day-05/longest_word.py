text = input("Enter a sentence: ")

words = text.split()

longest = max(words, key=len)

print("Longest word:", longest)