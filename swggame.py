import random
def game(comp,you):
    if comp=='s':
        if you=='w':
            return False
        elif you=='g':
            return True
    elif comp=='w':
        if you=='g':
            return False
        elif you=='s':
            return True   
    elif comp=='g':
        if you=='s':
            return False
        elif you=='w':
            return True
        
print("comp turn: snake(1) water(2) or gun(3)?")

randNo=random.randint(1,3)
# print(randNo)
if randNo==1:
    comp='s'
elif randNo==2:
    comp='w'
elif randNo==3:
    comp='g'
            
you=int(input("your turn: snake(1) water(2) or gun(3)="))
a=game(comp,you)

print(f"comp chose {comp}")
print(f"you chose {you}")

if a == None:
    print("the game is tie")
elif a:
    print("you lose")
else:
    print("you win!!")        