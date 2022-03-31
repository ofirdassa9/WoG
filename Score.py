import Utils
def add_score(difficulty):
    points_of_winning = (difficulty * 3) + 5
    try:
        with open(Utils.SCORES_FILE_NAME,"r") as f:
            score = f.read()
    except IOError:
        with open(Utils.SCORES_FILE_NAME,"w") as f:
            f.write("0")
            score = "0"
    finally:
        with open(Utils.SCORES_FILE_NAME,"w") as f:
            final_score = str(points_of_winning+int(score))
            f.write(final_score)
    return final_score

def get_score():
    try:
        with open(Utils.SCORES_FILE_NAME,"r") as f:
            score = f.read()
    except IOError:
        with open(Utils.SCORES_FILE_NAME,"w") as f:
            f.write("0")
            score = "0"
    finally:
        with open(Utils.SCORES_FILE_NAME,"w") as f:
            f.write(score)
    return score