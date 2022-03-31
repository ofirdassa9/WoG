import random

def generate_number(difficulty):
    return random.randint(1,difficulty)

def play(user_guess, secret_number):
    if int(user_guess) == int(secret_number):
        print(f"you won, the secret number was {secret_number}")
        return True
    else:
        print(f"you lost, the secret number was {secret_number} and your number was {user_guess}")
        return False

# def play(difficulty):
#     secret_number = generate_number(difficulty)
#     return compare_results(user_guess, secret_number)