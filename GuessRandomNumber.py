import random
score = 0
while True:
    n = int(input("Level: "))
    secret_number = random.randint(1, n)
    guess_count = 0
    guess_limit = 3
    
    print(f"\nGuess a number between 1 and {n}. You have 3 attempts.\n")
    while guess_count < guess_limit:
        try:
            guess = int(input("Enter the number: "))
            if guess < 1 or guess > n:
                print(f"Please enter an integer between 1 and {n}")
                continue
            guess_count += 1
            if secret_number == guess:
                print("Yayy!! You Won...")
                score += 10
                print(score)
                break
            elif secret_number < guess:
                print("Too High")
            elif secret_number > guess:
                print("Too Low")
        except ValueError:
            print("Invalid number. Please enter a valid number.")
    else:
        print("Better Luck Next Time!!")
        print(f"The Correct Number was: {secret_number}")

    play_again = input("Do you want to play again?(Yes/No): ").lower()
    if play_again != "yes":
        print(f"Your total score is {score}")
        print("Thankyou for playing. GoodBye!")
        break

