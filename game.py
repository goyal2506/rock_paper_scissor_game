import random 

a =int(input("Press 1 for rock /Press 2 for paper / Press 3 for scissor :"))
score = 0
computer_score=0
    
i=1
while a<4:
    if a==1:
        print("You choose ROCK")
    elif a==2:
        print("You choose PAPER")
    elif a==3:
        print("You choose SCISSOR")
    else:
        print("please choose only 1/2/3")

    num = random.randint(1,3)
    
    if num==1:
        print("Computer choose 'ROCK'")
    elif num==2:
        print("Computer choose 'PAPER'")
    elif num==3:
        print("Computer choose 'SCISSOR'")



    if a==1 and num ==1:
        print("tie")
    elif a== 1 and num==2:
        print("computer win")
        computer_score =computer_score+1
    elif a==1 and num == 3:
        print("you win")
        score= score+1
    if a==2 and num ==1:
        print("you win")
        score= score+1
    elif a== 2 and num==2:
        print(" tie")
    elif a==2 and num == 3:
        print("computer win")
        computer_score =computer_score+1
    if a==3 and num ==1:
            print("computer win")
            computer_score =computer_score+1
    elif a== 3 and num==2:
        print("you win")
        score= score+1
    elif a==3 and num == 3:
        print("tie")
    print("your score :",score,"computer score :",computer_score)
    print("_______________________________________________________")

    a = int(input("enter 1 for Rock /2 for Paper /3 for Scissor :"))
    
    i=i+1

print("enter wrong number")
