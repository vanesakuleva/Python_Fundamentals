integer_N = int(input())

for i in range (0, integer_N) :
    for k in range (0, integer_N) :
        for j in range (0, integer_N) :
            print(f'{chr( 97 + i)}{chr( 97 + k)}{chr( 97 + j)}')
