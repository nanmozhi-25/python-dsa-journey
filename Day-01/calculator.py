print("===== Simple Calculator =====")

num1 = float(input("Enter First Number : "))
num2 = float(input("Enter Second Number: "))

print("\n===== Results =====")

print("Addition       :", num1 + num2)
print("Subtraction    :", num1 - num2)
print("Multiplication :", num1 * num2)

if num2 != 0:
    print("Division       :", num1 / num2)
    print("Floor Division :", num1 // num2)
    print("Modulus        :", num1 % num2)
    print("Round Off      :", round(num1 / num2, 2))
else:
    print("Division       : Cannot divide by zero")
    print("Floor Division : Cannot divide by zero")
    print("Modulus        : Cannot divide by zero")
    print("Round Off      : Not Possible")

print("Power          :", num1 ** num2)