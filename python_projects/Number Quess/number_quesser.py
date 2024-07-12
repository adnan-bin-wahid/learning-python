import random

#random.randrange(start,end)  end is exclusive
# random.randint(start, end)  end is not inclusive

top_of_range = input("Enter the top of range : ")

if(top_of_range.isdigit()):
    top_of_range = int(top_of_range)
    if(top_of_range <= 0):
        print("Please type a number greater than 0 next time")
        quit()
else:
    print("Please type a nubmer next time")
    quit()

random_number = random.randint(0,top_of_range)

print(random_number)
guesses = 0

while(True):
    guesses += 1
    user_guess = input("Make a guess :")
    if(user_guess.isdigit()):
        user_guess = int(user_guess)
    else:
        print("Next time type a digit")
        continue
    if(user_guess == random_number):
        print("You got it ! ")
        break
    elif(user_guess > random_number):
        print("You are above of the number")
    else:
        print ("You are below of the number !")

print("You have completed with",guesses,"guesses")

    



