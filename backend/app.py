# run this in your terminal
# export FLASK_APP=app.py
# export FLASK_ENV=development
# flask run
import pymongo
from flask import Flask
from pymongo import MongoClient
import requests


client = pymongo.MongoClient('mongodb+srv://anooj101:rowdyhacks@cluster0-v8p0t.gcp.mongodb.net/test?retryWrites=true&w=majority')

# database
db = client['rowdyhacks']

# documents
meetings = db['meetings']
users = db['users']

app = Flask(__name__)

def get_zoom_id():
    response = requests.get(
        'https://api.github.com/search/repositories',
        params={'q': 'requests+language:python'},
        headers={'Accept': 'application/vnd.github.v3.text-match+json'},
    )

    # View the new `text-matches` array which provides information
    # about your search term within the results
    json_response = response.json()
    repository = json_response['items'][0]
    print(f'Text matches: {repository["text_matches"]}')
    return 1
# @app.route('/view/<variable>/')
# def view(variable):
#     pass
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
    #meeting_name, host_name, description, time, tags
    # id = get_zoom_id()
    # get geolocation
    meeting = {
        'zoom_id': 2,
        'meeting_name': 'meeting 2',
        'tags': ["Fun", "Reading"],
        'time':"10:34",
        'host_name': "John",
        'description': "description",
        'geolocation_lat':0,
        'geolocation_long':0
    }
    result = meetings.insert_one(meeting)

    print('One meeting scheduled: {0}'.format(result.inserted_id))
    return "<h1>Hello</h1>"

# @app.route('/zoom_meeting', methods=[]
# def home():
#     return ''
#
# @app.route('/zoom_meeting', methods=[])
# def home():
#     return ''


# @app.route('/createcm')
# def createcm():
#    summary  = request.args.get('summary', None)
#    change  = request.args.get('change', None)
