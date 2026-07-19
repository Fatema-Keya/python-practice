import requests

url = "https://jsonplaceholder.typicode.com/users/1"

response = requests.get(url)

if response.status_code == 200:
    print("API Call Success")
    print(response.json())

else:
    print("API Failed")