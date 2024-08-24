import random
Computer_Guessed_Number = random.randint(1,100)
Prasad_Guessed_Number = 0
Number_of_attemps = 0
while(Prasad_Guessed_Number!=Computer_Guessed_Number):
    Prasad_Guessed_Number=int(input("Please guess the number: "))
    Number_of_attemps +=1
    if Computer_Guessed_Number>Prasad_Guessed_Number:                                    
        print("Please Guess some Higher Number")
    elif Computer_Guessed_Number<Prasad_Guessed_Number:
        print("Please Guess some Lower Number")
    else:
        print("Congratulations Buddy -- You have entered correct Number ")
print(f"Computer guessed number is {Prasad_Guessed_Number} with your {Number_of_attemps}th attempts")
