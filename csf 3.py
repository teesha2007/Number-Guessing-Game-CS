import random

def run_game():
    """
    The main function for the Number Guessing Game.
    The player guesses a random number between 1 and 100.
    """
   
    secret_number = random.randint(1, 100)
    
    
    attempts = 0
    guess = 0
    
    print("------------------------------------------")
    print("     Welcome to the Number Guessing Game    ")
    print("------------------------------------------")
    print("I am thinking of a number between 1 and 100.")
    
    
    while guess != secret_number:
        try:
         
            guess_input = input("Enter your guess: ")
            guess = int(guess_input)
            
        
            if not 1 <= guess <= 100:
                print("Guess must be between 1 and 100. Try again.")
                continue 
            
            attempts += 1
            
            
            if guess < secret_number:
                print("➡️ Too low! Try a higher number.")
            elif guess > secret_number:
                print("⬅️ Too high! Try a lower number.")
                
        
        except ValueError:
            print("❌ Invalid input! Please enter a whole number.")
            continue
            
    
    print(f"\n🎉 CONGRATULATIONS! You guessed the number **{secret_number}**!")
    print(f"It took you **{attempts}** attempts to win.")


if __name__ == "__main__":
    run_game()