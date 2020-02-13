from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index1.html')

@app.route('/user_rec', methods=['POST'])
def user_rec():
    user_name = request.form.get('user_input')
    min_time = request.form.get('min_time')
    max_time = request.form.get('max_time')
    players = request.form.getlist('check')
    print(user_name, min_time, max_time, players)
    return redirect('/')

if __name__ == '__main__':
    app.run()