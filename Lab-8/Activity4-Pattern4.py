'''
Activity 3 (Problem 3)
-----
'''
for i in range(6, 0, -1):
    for b in range(6 - i):
        print(' ', end=' ')
    for a in range(1, i + 1):
        print(a, end=' ')
    print(' ')
