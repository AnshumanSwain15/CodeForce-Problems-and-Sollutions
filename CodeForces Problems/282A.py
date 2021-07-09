no_of_statements = int(input())
x = 0

for i in range(no_of_statements):
    statement = input()

    if statement[0] == '+' or statement[1] == '+':
        x += 1
    else:
        x -= 1

print(x)
