# run this in your terminal
# export FLASK_APP=app.py
# export FLASK_ENV=development
# flask run
import pymongo
from flask import Flask
from pymongo import MongoClient

client = pymongo.MongoClient('mongodb+srv://anooj101:rowdyhacks@cluster0-v8p0t.gcp.mongodb.net/test?retryWrites=true&w=majority')

# database
db = client['rowdyhacks']

# documents
meetings = db['meetings']
users = db['users']

app = Flask(__name__)

def get_zoom_id():
    return 1

# @app.route('/join_meeting', methods=[GET])
# def join_meeting():
#     return ''

@app.route('/create_meeting', methods=['GET'])
def create_meeting():
    #meeting_name, host_name, description, time, tags
    # id = get_zoom_id()
    # get geolocation
    meeting = {
        'zoom_id': 1,
        'meeting_name': 'PyMongo is fun, you guys',
        'tags': ["Fun", "Reading"],
        'time':"10:34",
        'host_name': "John",
        'description': "description",
        'geolocation_lat':0,
        'geolocation_long':0
    }
    result = meetings.insert_one(meeting)

    print('One meeting scheduled: {0}'.format(result.inserted_id))
    return ''

# @app.route('/zoom_meeting', methods=[])
# def home():
#     return ''
#
# @app.route('/zoom_meeting', methods=[])
# def home():
#     return ''
