number= int(input())

for i in range (number):
    code=int (input())
    if code == 88:
        print('Hello')
    if code == 86:
        print('How are you?')
    if code !=88 and code != 86 :
        if code < 88 :
            print ('GREAT!')
    if code > 88 :
        print('Bye.')

