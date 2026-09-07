import random
flag=True
comp,You,Draw=0,0,0
while flag:
    choices=["Rock","Paper","Scissors"]
    print("Welcome to Rock-Paper-Scissors game")
    s=input("Do any one from Rock paper Scissors: ")
    computer_choice=random.choice(choices)
    print("Computer Choice is ",computer_choice)
    if s=="Rock":
        if computer_choice=="Paper":
            print("You loss😓....best of luck")
            comp=comp+1
        elif computer_choice=="Scissors":
            print("You win😎.....Congratulation!!!")
            You=You+1
        else:
            print("You and computer put the same sign......")
            Draw=Draw+1;
    elif s=="Paper":
        if computer_choice=="Scissors":
            print("You loss😓....best of luck")
            comp=comp+1
        elif computer_choice=="Rock":
            print("You win😎.....Congratulation!!!")
            You=You+1
        else:
            print("You and computer put the same sign......")
            Draw=Draw+1;
    elif s=="Scissors":
        if computer_choice=="Rock":
            print("You loss😓....best of luck")
            comp=comp+1
        elif computer_choice=="Paper":
            print("You win😎.....Congratulation!!!")
            You=You+1
        else:
            print("You and computer put the same sign......")
            Draw=Draw+1;
    else:
        print("Enterthe valid one")
    
    print("Do You want to continue?")
    t=input("Enter yes or no");
    if(t=="no"):
        flag=False
        break;
ch=input("Do you want to know the score-card: ")
if ch=="yes":
    print("You: ",You," Computer: ",comp," Draws: ",Draw)
