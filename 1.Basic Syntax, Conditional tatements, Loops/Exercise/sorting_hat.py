name = input()
lenght = 0
while name != "Welcome!" and name!= 'Voldemort':

    lenght+= len(name)
    if lenght < 5 :
        print (f"{name} goes to Gryffindor.")
    if lenght == 5 :
        print(f"{name} goes to Slytherin.")
    if lenght == 6 :
        print(f"{name} goes to Ravenclaw.")
    if lenght>6 :
        print (f"{name} goes to Hufflepuff.")
    name = input()
    lenght = 0

if name == 'Voldemort':
    print ('You must not speak of that name!')
else:
    print("Welcome to Hogwarts.")

