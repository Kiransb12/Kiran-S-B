# Problem-3.py
x = int(input("Enter a number: "))

if x % 2 == 0:
    x -= 1

numbers = []
for i in range(1, x + 1, 2): 
    numbers.append(i)

print("Output:", numbers)
