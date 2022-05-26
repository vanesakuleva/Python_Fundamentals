word = input()

while word != 'End' :
    new = ""
    if word != "SoftUni":
        for letter in word:
            new += letter *2
        print (new)

    word = input()

