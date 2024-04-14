import random
number_of_turn = 3
secret_number= random.randint(1,10)

print(f"From 1 to 10, You have {number_of_turn} turns to guess the secret number!")
while number_of_turn >= 1:
    x = int(input("Your Guess: "))
    if x == secret_number:
        print(f"Congrats! The secret number is {secret_number} and you still have {number_of_turn} turn left!")
        break
    else:
        if x < secret_number:
            print(f"The secret number is larger than {x}.")
        else:
            print(f"The secret number is smaller than {x}.")
    print("try it again!")
    number_of_turn = number_of_turn -1
    print(f"You still have {number_of_turn} turns!")
else:
    print(f"Sry you didnt guess it! The answer is {secret_number}.")

