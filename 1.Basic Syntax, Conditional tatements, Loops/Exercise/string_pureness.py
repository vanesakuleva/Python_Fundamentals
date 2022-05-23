rows = int(input())

for i in range(rows):
    words= input()
    if ',' in words or '.' in words or '_' in words :
        print(f"{words} is not pure!")
    else:
        print(f"{words} is pure.")
