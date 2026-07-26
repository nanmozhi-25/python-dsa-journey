file = open("sample.txt", "r")

count = len(file.readlines())

print("Number of lines:", count)

file.close()