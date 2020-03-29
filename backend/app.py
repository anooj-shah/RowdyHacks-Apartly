# run this in your terminal
# export FLASK_APP=app.py
# export FLASK_ENV=development
# flask run
import pymongo
from flask import Flask, request, abort, jsonify
from pymongo import MongoClient
import requests
from datetime import datetime
from zoom import zoom_create_meeting, zoom_list_meetings


client = pymongo.MongoClient('mongodb+srv://anooj101:rowdyhacks@cluster0-v8p0t.gcp.mongodb.net/test?retryWrites=true&w=majority')
# database
db = client['rowdyhacks']

# documents
meetings = db['meetings']
users = db['users']

app = Flask(__name__)

@app.route('/join_meeting', methods=['GET'])
def join_meeting():
    meeting_name='PyMongo is fun, you guys'
    #lookup meetings_documents for zoom_id
    #zoom api to join meeting
    meeting = meetings.find_one({'meeting_name': meeting_name})
    if(meeting):
        zoom_id=meeting['zoom_id']
        print(meeting, zoom_id)
        #zoom join using zoom_id
        return zoom_id
    return "<h1>Bad meeting</h1>"

@app.route('/create_meeting', methods=['GET'])
def create_meeting():
    # headers = {'meeting_name':'value', 'host_name':'sdf', 'tags' :'', 'description' : "sadf"}
    print("h1")
    response = request.get_json()
    # response = request.headers
    # get geolocation
    meeting_name = response['meeting_name']
    host_name = response['host_name']
    tags = response['tags'] # list of tags
    description = response['description']
    time = datetime.now()
    print("h2")
    meeting = {
        'zoom_id': zoom_create_meeting(meeting_name, time),
        'meeting_name': meeting_name,
        'tags': tags,
        'time': time,
        'host_name': host_name,
        'description': description,
        'geolocation_lat':0,
        'geolocation_long':0
    }
    print("h3")
    result = meetings.insert_one(meeting)
    print('One meeting scheduled: {0}'.format(result.inserted_id))
    return "<h1>Hello</h1>"

# @app.route('/createcm')
# def createcm():
#    summary  = request.args.get('summary', None)
#    change  = request.args.get('change', None)
