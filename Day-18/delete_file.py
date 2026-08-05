import os

if os.path.exists("new_sample.txt"):
    os.remove("new_sample.txt")
    print("File deleted successfully.")
else:
    print("File does not exist.")