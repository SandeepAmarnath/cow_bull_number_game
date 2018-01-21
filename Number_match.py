import random
def base():
    chance = 0
    l=['1','2','3','4','5','6','7','8','9','0']
    hidden=random.sample(l,3)
    hidden=''.join(hidden)
    cow=0
    bull=0
    print(hidden)
    while chance<11:
        number = logic()
        game(hidden,number,cow,bull)
        chance+=1
        print("You finished {} chances".format(chance))
        if chance==11:
            print("Sorry you lost the game")
            print("The 3 letters are "+hidden)
            break

def logic():
    number = input("Enter a 3 digit number : ")
    return number

def game(hid,num,cow,bull):

    for i in range(3):
        if num[i] in hid:
            if num[i] == hid[i]:
                bull += 1
            else:
                cow += 1
    if bull ==3:
        print("Yippeeee you won the game")
        exit()

    if bull==0 and cow==0:
        print("No match found")


    else:
        print("The bull are "+str(bull))
        print("The cows are "+str(cow))



base()
