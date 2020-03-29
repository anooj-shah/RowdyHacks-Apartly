from flask import Flask, render_template

app = Flask(__name__)

@app.route('/login')
def home():
    return render_template('login.html')
@app.route('/')
@app.route('/explore')
def explore():
    return render_template('explore.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/meeting')
def meeting():
    return render_template('meeting.html')

@app.route('/schedule')
def schedule():
    return render_template('schedule.html')