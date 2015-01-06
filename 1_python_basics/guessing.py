import random

#choose a random number between 1 and 10
secret_number = random.choice(range(1,11))

#to count the number of trials
count = 1

#use a loop to ask for guesses and print hints repeatedly
while count <= 5:
    #to read in a new guess use
    guess = int(input('Guess a number between 1 and 10: '))

    #store the differnce between guess and the secret number
    diff = abs(guess - secret_number)

    #if the player guesses x correctly,
    #the program prints a message and terminates
    if diff == 0:
        print('Congratulation! You guess correctly')
        break

    #if the different between x and the guess is greater than 5,
    #the program prints 'not even close'
    elif diff > 5:
        print('Not Even Close')

    #if the different between x and the guess is between 3 and 5,
    #the program prints 'close'
    elif 3 <= diff <= 5:
        print('Close')

    #if the different between x and the guess is less than 3,
    #the program prints 'almost there'
    elif diff < 3:
        print('Almost there')

    #check if this is the final trial
    if count == 5:
        print('You failed the fifth guess, the program would terminate.')

    #increment the count
    count = count + 1
