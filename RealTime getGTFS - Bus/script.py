# pip install google.transit


from google.transit import gtfs_realtime_pb2
import requests

headers = {
    'accept': '*/*',
    # requests won't add a boundary if this header is set when you pass files=
    # 'Content-Type': 'multipart/form-data',
}

files = {
    'token': (None, '638322713900670603'),
}

feed = gtfs_realtime_pb2.FeedMessage()
response = requests.post('https://testpcsdata.njtransit.com/api/GTFS/getVehiclePositions', headers=headers, files=files)
feed.ParseFromString(response.content)
message = feed.entity

\











print(message)

# for item in message:
#     if not item.HasField('trip_update'):
#         continue
#     tu = item.trip_update
#     for stu in tu.stop_time_update:  ## Loop over the stop_time_update repeated element
#         if stu.HasField('arrival'):
#             stu.arrival.delay = 30
#         if stu.HasField('departure'):
#             stu.departure.delay = 30

