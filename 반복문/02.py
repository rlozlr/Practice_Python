# '*'를 이용해서 다양한 모양을 출력

for i in range(1, 6):
    print('*' * i)
print('-' * 50)

for i in range (1, 6):
    for j in range (6 - i - 1):
        print (' ', end ='')
    for k in range (i):
        print ('*', end='')
    print()
print('-' * 50)

for i in range (5, 0, -1):
    print ('*' * i)
print('-' * 50)

for i in range (5, 0, -1):
    for j in range (6 - i - 1):
        print (' ', end ='')
    for k in range (i):
        print ('*', end='')
    print()
print('-' * 50)

for i in range(1, 10):
    if ( i < 5):
        print('*' * i)
    else:
        print('*' * (10 - i))
print('-' * 50)

for i in range (1, 6):
    for j in range (1, 6):
        if (i == j):
            print('*', end='')
        else:
            print(' ', end='')
    print()
print('-' * 50)

for i in range (5, 0, -1):
    for j in range (1, 6):
        if (i == j):
            print('*', end='')
        else:
            print(' ', end='')
    print()
print('-' * 50)

for i in range(1, 11):
    if i < 6:
        for j in range(5 - i):
            print(" ", end="")
        for j in range(2 * i - 1):
            print("*", end="")
        print()
    else:
        for j in range(i - 6):
            print(" ", end="")
        for j in range((11 - i) * 2 - 1):
            print("*", end="")
        print()
print('-' * 50)