from flask import Flask, render_template

app = Flask(__name__)

@app.route('/login')
def home():
    return render_template('login.html')
@app.route('/')
@app.route('/explore')
def explore():
    return render_template('explore.html')

@app.route('/temp')
def temp():
    return render_template('temp.html')