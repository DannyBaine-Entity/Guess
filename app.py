from flask import Flask, render_template
import random

app = Flask(__name__)


def generate_target_number():
    return random.randint(1, 101)

target_number = generate_target_number()

@app.route('/')
def index():
    return render_template('index.html')

@app.get("/game")
def game():
    numbers_to_guess = range(1, 101)
    return render_template("game.html", numbers=numbers_to_guess)

@app.route('/guess/<int:number>')
def guess(number):

    if number == target_number:
        feedback = "Correct"
    elif number < target_number:
        feedback = "Too Low"
    else:
        feedback = "Too High"

    return render_template('guess.html', number=number, feedback=feedback, target=target_number)

if __name__ == '__main__':
    app.run(debug=True)
