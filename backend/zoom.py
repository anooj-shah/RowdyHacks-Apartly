import json
from zoomus import ZoomClient
from datetime import datetime
def setup():
    client = ZoomClient("ughCBh93TRyPCf9Xzkoy3Q","jgngXqwIQQw5gvYOEiEXLKAn4vP51byGIj1R", version=1)

    user_list_response = client.user.list()
    user_list = json.loads(user_list_response.content)
    user_id = ''
    for user in user_list['users']:
        user_id = user['id']
        print(json.loads(client.meeting.list(host_id=user_id).content))
    return user_id, client

def zoom_list_meetings():
    user_id, client = setup()
    user_list_response = client.user.list()
    user_list = json.loads(user_list_response.content)
    user_id = ''
    for user in user_list['users']:
        user_id = user['id']
    meeting_info = json.loads(client.meeting.list(host_id=user_id).content)
    # meeting_id = meeting_info['meetings'][-1]['id']
    return meeting_info

def zoom_create_meeting(topic="test", start_time=datetime.now(), type="2"):
    user_id,client=setup()
    start_time = datetime.now()
    client.meeting.create(host_id = user_id, topic = topic, type = type, start_time = start_time)
    meeting_info = json.loads(client.meeting.list(host_id=user_id).content)
    meeting_id = meeting_info['meetings'][-1]['id']
    return meeting_id


# create_meeting()
# list_meetings()
