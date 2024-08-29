from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = 'supersecretkey'

def roll_dice():
    return random.randint(1, 6)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        session['player1'] = request.form['player1']
        session['player2'] = request.form['player2']
        session['player1_score'] = 0
        session['player2_score'] = 0
        session['current_score'] = 0
        session['turn'] = 'player1'
        return redirect(url_for('game'))
    return render_template('index.html')

@app.route('/game', methods=['GET', 'POST'])
def game():
    dice_value = None
    
    if 'player1' not in session or 'player2' not in session:
        return redirect(url_for('index'))

    if request.method == 'POST':
        action = request.form['action']
        if action == 'roll':
            dice_value = roll_dice()
            if dice_value == 1:
                session['current_score'] = 0
                session['turn'] = 'player2' if session['turn'] == 'player1' else 'player1'
            else:
                session['current_score'] += dice_value
        elif action == 'hold':
            if session['turn'] == 'player1':
                session['player1_score'] += session['current_score']
                if session['player1_score'] >= 20:
                    return render_template('winner.html', winner=session['player1'])
            else:
                session['player2_score'] += session['current_score']
                if session['player2_score'] >= 20:
                    return render_template('winner.html', winner=session['player2'])
            session['current_score'] = 0
            session['turn'] = 'player2' if session['turn'] == 'player1' else 'player1'

    dice_value = dice_value if dice_value is not None else 1

    return render_template('game.html', dice_value=dice_value, session=session)

@app.route('/restart')
def restart():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
