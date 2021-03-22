import requests
url = "https://www.google.com" #need to include the http
res = requests.get(url)
# print(res.ok)
# print(res.headers)
# print(res.text) #main part

print(f"your request to {url} came back w/ status code {res.status_code}") 
#status code 2xx -> OK
#status code 4xx -> CLIENT SIDE ERROR (404 error)
print(res.text)