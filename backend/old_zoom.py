import requests

r = requests.get('http://127.0.0.1:5000/create_meeting', json = {'meeting_name':'test8', 'host_name':'sdf', 'tags' :['business','hobbies','creativity'], 'description' : "sadf"})
r = requests.get('http://127.0.0.1:5000/create_meeting', json = {'meeting_name':'test9', 'host_name':'sdf', 'tags' :['DIY','creativity','c'], 'description' : "sadf"})
r = requests.get('http://127.0.0.1:5000/create_meeting', json = {'meeting_name':'test10', 'host_name':'sdf', 'tags' :['gujrati','business','hobbies'], 'description' : "sadf"})
r = requests.get('http://127.0.0.1:5000/create_meeting', json = {'meeting_name':'test11', 'host_name':'sdf', 'tags' :['creativity','business'], 'description' : "sadf"})
r = requests.get('http://127.0.0.1:5000/create_meeting', json = {'meeting_name':'test12', 'host_name':'sdf', 'tags' :['DIY','food','gujrati'], 'description' : "sadf"})


# print(r)
# print(r.content)
r = requests.get('http://127.0.0.1:5000/list_meetings')
print(r.content)
# # create meeting: host_id="ID", topic="TOPIC", type="TYPE"
# # list: user_id
# # print(user_id)
#
# # print(json.loads(client.meeting.create(user_id=user_id, topic="hi", type= 2).content))
# # meeting = json.loads(test.content)
# # print(meeting)
# # print(json.loads(client.meeting.list(host_id=user_id).content))
# print(json.loads(client.meeting.list(host_id=user_id).content))
# print(start_time, zoomus.util.date_to_str(start_time))
# # test = client.meeting.create((json.dumps(params))
#
# {'page_count': 1, 'page_number': 1, 'page_size': 30, 'total_records': 5,'meetings':
#
# [
#     {'uuid': 'oVgGtfZFRyqv73QKS+KeZA==', 'id': 132087693, 'host_id': 'W4Y0rZOHRpGl7RhxiBG-VA', 'topic': 'test', 'password': '', 'h323_password': '', 'status': 0, 'option_jbh': False, 'option_start_type': 'video', 'option_host_video': True, 'option_participants_video': True, 'option_cn_meeting': False, 'option_enforce_login': False, 'option_enforce_login_domains': '', 'option_in_meeting': False, 'option_audio': 'both', 'option_alternative_hosts': '', 'option_use_pmi': False, 'type': 2, 'start_time': '2020-03-28T20:21:32Z', 'duration': 60, 'timezone': 'America/Chicago', 'start_url': 'https://zoom.us/s/132087693?zak=eyJ6bV9za20iOiJ6bV9vMm0iLCJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJjbGllbnQiLCJ1aWQiOiJXNFkwclpPSFJwR2w3Umh4aUJHLVZBIiwiaXNzIjoid2ViIiwic3R5IjoxLCJ3Y2QiOiJhdzEiLCJjbHQiOjAsInN0ayI6IlBwcWNfeGktMl8zM1pnRzMxa1o5Y1NsbVdCbTl0cktEUHdZZ21wX2QxcG8uRWdJQUFBRnhJLWdVakFBQUhDQWdaMnc0UlVwaWJWb3hiakJCWVdwWlNHOU9kRTFMVm5ac1FrNXFjbFpHYjBFQURETkRRa0YxYjJsWlV6TnpQUU5oZHpFIiwiZXhwIjoxNTg1NDUyNTQ0LCJpYXQiOjE1ODU0NDUzNDQsImFpZCI6Ikl2OU9mTFJQUjN1NklnYk5zNlVzaHciLCJjaWQiOiIifQ.EaTL7s3mph45eC18N80Zuvt4rzrgwPqoMyTvql3jAos', 'join_url': 'https://zoom.us/j/132087693', 'created_at': '2020-03-29T01:21:32Z'},
#
#     {'uuid': 'O8+RacJbSHSmbLakU3vynQ==', 'id': 739804871, 'host_id': 'W4Y0rZOHRpGl7RhxiBG-VA', 'topic': 'test', 'password': '', 'h323_password': '', 'status': 0, 'option_jbh': False, 'option_start_type': 'video', 'option_host_video': True, 'option_participants_video': True, 'option_cn_meeting': False, 'option_enforce_login': False, 'option_enforce_login_domains': '', 'option_in_meeting': False, 'option_audio': 'both', 'option_alternative_hosts': '', 'option_use_pmi': False, 'type': 2, 'start_time': '2020-03-28T20:21:47Z', 'duration': 60, 'timezone': 'America/Chicago', 'start_url': 'https://zoom.us/s/739804871?zak=eyJ6bV9za20iOiJ6bV9vMm0iLCJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJjbGllbnQiLCJ1aWQiOiJXNFkwclpPSFJwR2w3Umh4aUJHLVZBIiwiaXNzIjoid2ViIiwic3R5IjoxLCJ3Y2QiOiJhdzEiLCJjbHQiOjAsInN0ayI6IlBwcWNfeGktMl8zM1pnRzMxa1o5Y1NsbVdCbTl0cktEUHdZZ21wX2QxcG8uRWdJQUFBRnhJLWdVakFBQUhDQWdaMnc0UlVwaWJWb3hiakJCWVdwWlNHOU9kRTFMVm5ac1FrNXFjbFpHYjBFQURETkRRa0YxYjJsWlV6TnpQUU5oZHpFIiwiZXhwIjoxNTg1NDUyNTQ0LCJpYXQiOjE1ODU0NDUzNDQsImFpZCI6Ikl2OU9mTFJQUjN1NklnYk5zNlVzaHciLCJjaWQiOiIifQ.EaTL7s3mph45eC18N80Zuvt4rzrgwPqoMyTvql3jAos', 'join_url': 'https://zoom.us/j/739804871', 'created_at': '2020-03-29T01:21:47Z'},
#
#     {'uuid': 'qcoZsfsmTdelyk5edUGRWg==', 'id': 298603392, 'host_id': 'W4Y0rZOHRpGl7RhxiBG-VA', 'topic': 'test', 'password': '', 'h323_password': '', 'status': 0, 'option_jbh': False, 'option_start_type': 'video', 'option_host_video': True, 'option_participants_video': True, 'option_cn_meeting': False, 'option_enforce_login': False, 'option_enforce_login_domains': '', 'option_in_meeting': False, 'option_audio': 'both', 'option_alternative_hosts': '', 'option_use_pmi': False, 'type': 2, 'start_time': '2020-03-28T20:27:33Z', 'duration': 60, 'timezone': 'America/Chicago', 'start_url': 'https://zoom.us/s/298603392?zak=eyJ6bV9za20iOiJ6bV9vMm0iLCJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJjbGllbnQiLCJ1aWQiOiJXNFkwclpPSFJwR2w3Umh4aUJHLVZBIiwiaXNzIjoid2ViIiwic3R5IjoxLCJ3Y2QiOiJhdzEiLCJjbHQiOjAsInN0ayI6IlBwcWNfeGktMl8zM1pnRzMxa1o5Y1NsbVdCbTl0cktEUHdZZ21wX2QxcG8uRWdJQUFBRnhJLWdVakFBQUhDQWdaMnc0UlVwaWJWb3hiakJCWVdwWlNHOU9kRTFMVm5ac1FrNXFjbFpHYjBFQURETkRRa0YxYjJsWlV6TnpQUU5oZHpFIiwiZXhwIjoxNTg1NDUyNTQ0LCJpYXQiOjE1ODU0NDUzNDQsImFpZCI6Ikl2OU9mTFJQUjN1NklnYk5zNlVzaHciLCJjaWQiOiIifQ.EaTL7s3mph45eC18N80Zuvt4rzrgwPqoMyTvql3jAos', 'join_url': 'https://zoom.us/j/298603392', 'created_at': '2020-03-29T01:27:34Z'},
#
#     {'uuid': 'gJuGA76qRhCgINlu937msA==', 'id': 775766277, 'host_id': 'W4Y0rZOHRpGl7RhxiBG-VA', 'topic': 'test', 'password': '', 'h323_password': '', 'status': 0, 'option_jbh': False, 'option_start_type': 'video', 'option_host_video': True, 'option_participants_video': True, 'option_cn_meeting': False, 'option_enforce_login': False, 'option_enforce_login_domains': '', 'option_in_meeting': False, 'option_audio': 'both', 'option_alternative_hosts': '', 'option_use_pmi': False, 'type': 2, 'start_time': '2020-03-28T20:28:33Z', 'duration': 60, 'timezone': 'America/Chicago', 'start_url': 'https://zoom.us/s/775766277?zak=eyJ6bV9za20iOiJ6bV9vMm0iLCJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJjbGllbnQiLCJ1aWQiOiJXNFkwclpPSFJwR2w3Umh4aUJHLVZBIiwiaXNzIjoid2ViIiwic3R5IjoxLCJ3Y2QiOiJhdzEiLCJjbHQiOjAsInN0ayI6IlBwcWNfeGktMl8zM1pnRzMxa1o5Y1NsbVdCbTl0cktEUHdZZ21wX2QxcG8uRWdJQUFBRnhJLWdVakFBQUhDQWdaMnc0UlVwaWJWb3hiakJCWVdwWlNHOU9kRTFMVm5ac1FrNXFjbFpHYjBFQURETkRRa0YxYjJsWlV6TnpQUU5oZHpFIiwiZXhwIjoxNTg1NDUyNTQ0LCJpYXQiOjE1ODU0NDUzNDQsImFpZCI6Ikl2OU9mTFJQUjN1NklnYk5zNlVzaHciLCJjaWQiOiIifQ.EaTL7s3mph45eC18N80Zuvt4rzrgwPqoMyTvql3jAos', 'join_url': 'https://zoom.us/j/775766277', 'created_at': '2020-03-29T01:28:33Z'},
#
#     {'uuid': 'am5G181ESlGJ9j4DD6gxPw==', 'id': 219314825, 'host_id': 'W4Y0rZOHRpGl7RhxiBG-VA', 'topic': 'test', 'password': '', 'h323_password': '', 'status': 0, 'option_jbh': False, 'option_start_type': 'video', 'option_host_video': True, 'option_participants_video': True, 'option_cn_meeting': False, 'option_enforce_login': False, 'option_enforce_login_domains': '', 'option_in_meeting': False, 'option_audio': 'both', 'option_alternative_hosts': '', 'option_use_pmi': False, 'type': 2, 'start_time': '2020-03-28T20:29:02Z', 'duration': 60, 'timezone': 'America/Chicago', 'start_url': 'https://zoom.us/s/219314825?zak=eyJ6bV9za20iOiJ6bV9vMm0iLCJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJjbGllbnQiLCJ1aWQiOiJXNFkwclpPSFJwR2w3Umh4aUJHLVZBIiwiaXNzIjoid2ViIiwic3R5IjoxLCJ3Y2QiOiJhdzEiLCJjbHQiOjAsInN0ayI6IlBwcWNfeGktMl8zM1pnRzMxa1o5Y1NsbVdCbTl0cktEUHdZZ21wX2QxcG8uRWdJQUFBRnhJLWdVakFBQUhDQWdaMnc0UlVwaWJWb3hiakJCWVdwWlNHOU9kRTFMVm5ac1FrNXFjbFpHYjBFQURETkRRa0YxYjJsWlV6TnpQUU5oZHpFIiwiZXhwIjoxNTg1NDUyNTQ0LCJpYXQiOjE1ODU0NDUzNDQsImFpZCI6Ikl2OU9mTFJQUjN1NklnYk5zNlVzaHciLCJjaWQiOiIifQ.EaTL7s3mph45eC18N80Zuvt4rzrgwPqoMyTvql3jAos', 'join_url': 'https://zoom.us/j/219314825', 'created_at': '2020-03-29T01:29:02Z'}
# ]}


#
#
# [{'_id': ObjectId('5e7fb3ad2220746aeaa93236'), 'zoom_id': 1, 'meeting_name': 'PyMongo is fun, you guys', 'tags': ['Fun', 'Reading'], 'time': '10:34', 'host_name': 'John', 'description': 'description', 'geolocation_lat': 0, 'geolocation_long': 0},
# {'_id': ObjectId('5e7fbbf87560678d95822225'), 'zoom_id': 2, 'meeting_name': 'meeting 2', 'tags': ['Fun', 'Reading'], 'time': '10:34', 'host_name': 'John', 'description': 'description', 'geolocation_lat': 0, 'geolocation_long': 0},
# {'_id': ObjectId('5e7fbc1d8f2055e43f7dc30b'), 'zoom_id': 2, 'meeting_name': 'meeting 2', 'tags': ['Fun', 'Reading'], 'time': '10:34', 'host_name': 'John', 'description': 'description', 'geolocation_lat': 0, 'geolocation_long': 0},
# {'_id': ObjectId('5e801161812a2ff4082bc843'), 'zoom_id': 157191797, 'meeting_name': 'basdf', 'tags': 'sdfdsf', 'time': datetime.datetime(2020, 3, 28, 22, 9, 20, 149000), 'host_name': 'sdf', 'description': 'sadf', 'geolocation_lat': 0, 'geolocation_long': 0},
# {'_id': ObjectId('5e8012f72133afdbca52dbd3'), 'zoom_id': 409119287, 'meeting_name': 'value', 'tags': '', 'time': datetime.datetime(2020, 3, 28, 22, 16, 6, 682000), 'host_name': 'sdf', 'description': 'sadf', 'geolocation_lat': 0, 'geolocation_long': 0},
# {'_id': ObjectId('5e8015e5d4229c9dc06bf34a'), 'zoom_id': 168867074, 'meeting_name': 'value', 'tags': '', 'time': datetime.datetime(2020, 3, 28, 22, 28, 36, 735000), 'host_name': 'sdf', 'description': 'sadf', 'geolocation_lat': 0, 'geolocation_long': 0},
# {'_id': ObjectId('5e8016079f5d01b3f8d2131d'), 'zoom_id': 190138393, 'meeting_name': 'value', 'tags': '', 'time': datetime.datetime(2020, 3, 28, 22, 29, 10, 454000), 'host_name': 'sdf', 'description': 'sadf', 'geolocation_lat': 0, 'geolocation_long': 0}]
