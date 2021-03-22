import requests

url = "https://icanhazdadjoke.com/"
# response = requests.get(url, headers = {"Accept":"text/plain"}) #works for this website because it has an API (for computers to talk to each other)
response = requests.get(url, headers = {"Accept":"application/json"}) #gets the JSON version of this website
# print(response.text)
# print(response.json()) #turns the string into python dictionary that can be used 

data = response.json()

# {"id":"lV8hqHexHBd",
# "joke":"Why did the worker get fired from the orange juice factory? Lack of concentration.",
# "status":200}
print(data["joke"])
print(f"status: {data['status']}")