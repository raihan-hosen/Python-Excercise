n=18
guess=1
while(guess<=9):
    a=int(input("Enter your guess: "))
    if(a<n):
        print("Too low")
    elif(a>n):
        print("Too high")
    else:
        print("You win!")
        break
    guess=guess+1
    guessleft=9-guess
    if(guess>9):
        print("You lose! The number is",n)
    
if(guessleft>=0):
    print("You had",guessleft,"guesses left")
    

elif(guessleft<=0):
    print("You used all your guesses")
    

