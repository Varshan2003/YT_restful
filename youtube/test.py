import requests

BASE_URL = "http://127.0.0.1:5000"

# Define the data to be sent in the PUT request
data = [
    {"name": "HomeTour", "views": 10000, "likes": 100},
    {"name": "DSA", "views": 100000, "likes": 100},
    {"name": "Varshan", "views": 10, "likes": 1}
]

# Send PUT requests for each data item
for idx, video_data in enumerate(data):
    response = requests.put(f"{BASE_URL}/video/{idx}", json=video_data)
    print(response.json())

# Send a GET request to retrieve a video by its ID
response = requests.get(f"{BASE_URL}/video/2")
print(response.json())
