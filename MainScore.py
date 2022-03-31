from flask import Flask, render_template, request, redirect, url_for
import Score, GuessGame, MemoryGame

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    return redirect('index.html')

@app.route("/guess", methods=['GET', 'POST'])
def guess():
    try:
        if request.method == 'POST':
            guess = request.form['input']
            diff = request.form['diffuculity']
            secret = GuessGame.generate_number(int(diff))
            if GuessGame.play(guess,secret):
                score = Score.add_score(int(diff))
                return render_template("guess.html", output=f"You won! You now have {score} points!")
            else:
                return render_template("guess.html", output=f"You lost, no points for you loser")
        else:
            return render_template("guess.html")

    except BaseException as e:
        return render_template("error.html", error=str(e))


@app.route("/memorydiff", methods=['GET', 'POST'])
def memorydiff():
    if request.method == 'GET':
        return render_template("memorydiff.html")
    else:        
        diff = request.form['diffuculity']
        list = MemoryGame.generate_sequence(int(diff))
        return redirect(url_for('memory', list=list, diffuculity=diff))
    

@app.route("/memory", methods=['GET', 'POST'])
def memory():
    try:
        if (request.method == 'POST') and (request.args.getlist("list") != 0):
            user_list = request.args.getlist("list")
            gen_list = request.form['user_guess']
            print(gen_list, type(gen_list))
            print(user_list,type(user_list))
            if MemoryGame.is_list_equal(gen_list,user_list):
                score = Score.add_score(int(request.form['diffuculity']))
                return render_template("memory.html", output=f"You won! here's {score} points!")
            else:
                return render_template("memory.html", output=f"You lost, no points for you loser")
        elif (request.method == 'GET') and (len(request.args.getlist("diffuculity")) != 0):
            gen_list = request.args.getlist("list")
            return redirect(url_for('memory', list = gen_list))
        elif request.method == 'GET':
            return render_template("memory.html")
        else:
            return redirect(url_for('index.html'))
    except BaseException as e:
        return render_template("error.html", error=str(e))   

@app.route("/index.html")
def index():
        return render_template("index.html", score=Score.get_score())

@app.route("/error.html")
def error():
    return render_template("error.html", error=Score.Utils.BAD_RETURN_CODE)

app.run(host='0.0.0.0')