from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/login')
def home():
    return render_template('login.html')

@app.route('/')
@app.route('/explore')
def explore():
    r = requests.get('https://apartly-backend.herokuapp.com/list_tags')
    # print(r)
    # print(r.content)
    x = json.loads(r.content)
    # print(x)
    # print(x)
    arts = {}
    music = {}
    fire = {}
    # print(x['arts'])
    for i in x['arts']:
        meeting = {
            'meeting_name': i['meeting_name'],
            'zoom_id': i['zoom_id']
        }
        arts[len(arts)] = meeting
    for i in x['music']:
        meeting = {
            'meeting_name': i['meeting_name'],
            'zoom_id': i['zoom_id']
        }
        music[len(music)] = meeting
    for i in x['fire']:
        meeting = {
            'meeting_name': i['meeting_name'],
            'zoom_id': i['zoom_id']
        }
        fire[len(fire)] = meeting
    # print(arts)
    return render_template('explore.html', arts=arts, music=music, fire=fire)

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/meeting')
def meeting():
    zid = request.args.get('id')
    print(zid)
    r = requests.get('https://apartly-backend.herokuapp.com/list_tags')
    x = json.loads(r.content)
    answ = {}
    for i in x['arts']:
        # print(x[i][0]['zoom_id'], zid)
        if int(i['zoom_id']) == int(zid):
            answ['meeting_name'] = i['meeting_name']
            answ['host_name'] = i['host_name']
            answ['description'] = i['description']
            answ['zoom_id'] = i['zoom_id']
            answ['num_people'] = i['num_people']
    print(answ)
    return render_template('meeting.html', answ=answ)

@app.route('/schedule')
def schedule():
    return render_template('schedule.html')

@app.route('/create')
def create():
    return render_template('create.html')