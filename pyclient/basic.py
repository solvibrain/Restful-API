import requests

endpoint = "http://localhost:8000/api/"
# endpoint = "https://httpbin.org/anything"
# endpoint = "http://httpbin.org/status/200"

get_response = requests.get(endpoint)
# print(get_response.text)
print(get_response.status_code)
# print(type(get_response))
print(get_response.json())