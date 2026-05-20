import random
print("Welcome to Rock Paper Scissors Game!")
your_score=0
computer_score=0
while True:
    print("Choose:")
    print("1.Rock\n2.Paper\n3.Scissors")
    your_choice=input("Enter your choice:").lower()
    if your_choice not in ("rock","paper","scissors"):
        print("Invalid Choice")
        continue
    computer_choice=random.choice(("rock","paper","scissors"))
    print("Computer choice:",computer_choice)
    if computer_choice=="rock" and your_choice=="paper":
        result="you win"
    elif computer_choice=="paper" and your_choice=="scissors":
        result="you win"
    elif computer_choice=="scissors" and your_choice=="rock":
        result="you win"
    elif computer_choice=="rock" and your_choice=="scissors":
        result="computer wins"
    elif computer_choice=="paper" and your_choice=="rock":
        result="computer wins"
    elif computer_choice=="scissors" and your_choice=="paper":
        result="computer wins"
    elif computer_choice=="rock" and your_choice=="rock":
        result="draw"
    elif computer_choice=="paper" and your_choice=="paper":
        result="draw"
    else:
       result="draw"
    if result=="you win":
        your_score+=1
    else:
        computer_score+=1
    print("Your Score:",your_score)
    print("Computer Score:",computer_score)
    if your_score>computer_score:
        print("You Win")
    else:
        print("Computer Wins")
    choice=input("Do you want to play again(Y/N)?").lower()
    if choice=='n':
        print("Game Over")
        print("Your final Score:",your_score)
        print("Computer final Score:",computer_score)
        if your_score>computer_score:
            print("Final Winner:You")
        elif your_score<computer_score:
            print("Final Winner:computer")
        else:
            print("Draw")
        break
 
