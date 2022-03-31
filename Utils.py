import click

SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = "404"

def validate(min, max, num):
    if not min <= num <= max:
        print(f"Please choose a correct number between {min} and {max}")
        return False
    return True

def Screen_cleaner():
    click.clear()