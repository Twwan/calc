num = int(input())
base = int(input("Base (2-9): "))

newNum = ''

while num > 0:
    newNum = str(num % base) + newNum
    num //= base

print(newNum)