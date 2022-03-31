import random
import time
def generate_sequence(difficulty):
    return random.sample(range(1, 101), difficulty)

def is_list_equal(user_list, sequence):
    if user_list == sequence:
        print(f"you won, the secret list was {sequence}")
        return True
    else:
        print(f"you lost, the secret list was {sequence}")
        return False

def play(difficulty):
    sequence = generate_sequence(difficulty)
    print(sequence, end="\r")
    time.sleep(0.7)
    user_list = get_list_from_user(difficulty)
    return is_list_equal(user_list, sequence)