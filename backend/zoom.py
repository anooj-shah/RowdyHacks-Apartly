import json
from zoomus import ZoomClient
from datetime import datetime
import zoomus.util
# CHAT HISTORY TOKEN eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJXNFkwclpPSFJwR2w3Umh4aUJHLVZBIn0.JQDaP2QAh_1grKHnBitKbwUoPamFYIHcbPKXGJqh1eI
user_list_response = client.user.list()
user_list = json.loads(user_list_response.content)

print(user_list)

user_id = ''
for user in user_list['users']:
    user_id = user['id']
    print(json.loads(client.meeting.list(host_id=user_id).content))

# create meeting: host_id="ID", topic="TOPIC", type="TYPE"
# list: user_id
print(user_id)
print(json.loads(client.meeting.list(host_id=user_id).content))

start_time = datetime.now()

print(start_time)

# test = client.meeting.create((json.dumps(params))
client.meeting.create(host_id=user_id, topic="anooj is gr8", type= '2', start_time="")
# print(json.loads(client.meeting.create(user_id=user_id, topic="hi", type= 2).content))

# meeting = json.loads(test.content)
# print(meeting)

print(json.loads(client.meeting.list(host_id=user_id).content))
