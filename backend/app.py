# run this in your terminal
# export FLASK_APP=app.py
# export FLASK_ENV=development
# flask run
import pymongo
from flask import Flask, request, abort, jsonify
from pymongo import MongoClient
import requests
import random
import json
from datetime import datetime
from zoom import zoom_create_meeting, zoom_list_meetings

from bson.json_util import dumps


client = pymongo.MongoClient('mongodb+srv://anooj101:rowdyhacks@cluster0-v8p0t.gcp.mongodb.net/test?retryWrites=true&w=majority')
# database
db = client['rowdyhacks']

# documents
meetings = db['meetings']
users = db['users']

app = Flask(__name__)

@app.route('/list_tags', methods=['GET'])
def list_tags():
    # meetings_arr = (list(meetings.find()))
    tags={}
    for i in meetings.find():
        for j in i['tags']:
            if j in tags:
                tags[j].append(i)
            else:
                tags[j] = [i]
    print(tags)
    return dumps(meetings_arr)

@app.route('/list_meetings', methods=['GET'])


def list_meetings():
    meetings_arr = dumps(list(meetings.find()))

    return meetings_arr

# @app.route('/join_meeting', methods=['GET'])
# def join_meeting():
#     meeting_name='PyMongo is fun, you guys'
#     #lookup meetings_documents for zoom_id
#     #zoom api to join meeting
#     meeting = meetings.find_one({'meeting_name': meeting_name})
#     if(meeting):
#         zoom_id=meeting['zoom_id']
#         print(meeting, zoom_id)
#         #zoom join using zoom_id
#         return zoom_id
#     return "<h1>Bad meeting</h1>"

@app.route('/create_meeting', methods=['POST'])
def create_meeting():
    # headers = {'meeting_name':'value', 'host_name':'sdf', 'tags' :'', 'description' : "sadf"}
    response = request.get_json()
    # response = request.headers
    # get geolocation
    meeting_name = response['meeting_name']
    host_name = response['host_name']
    tags = response['tags'] # list of tags
    description = response['description']
    time = datetime.now()
    meeting = {
        'zoom_id': zoom_create_meeting(meeting_name, time),
        'meeting_name': meeting_name,
        'tags': tags,
        'time': time,
        'host_name': host_name,
        'description': description,
        'num_people' : random.randint(205,500),
        'geolocation_lat':0,
        'geolocation_long':0
    }
    result = meetings.insert_one(meeting)
    print('One meeting scheduled: {0}'.format(result.inserted_id))
    return "<h1>Hello</h1>"
# list_tags()
