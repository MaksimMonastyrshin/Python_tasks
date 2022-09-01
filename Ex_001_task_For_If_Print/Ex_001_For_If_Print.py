max = 10
for i in range(max+1):
    for j in range(max+1):
        if i == j or i == max - j or i in [0, max] or j in [0, max]:
            print('#', end='')
        else:
            print(' ', end='')
    print('\r')
