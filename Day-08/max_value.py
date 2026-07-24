marks = {
    "Math": 85,
    "Science": 92,
    "English": 78
}

subject = max(marks, key=marks.get)

print("Highest Mark Subject:", subject)
print("Marks:", marks[subject])