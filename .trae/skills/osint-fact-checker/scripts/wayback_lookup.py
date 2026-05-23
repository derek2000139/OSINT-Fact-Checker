import requests

url = input("Input URL: ")

api = f"https://archive.org/wayback/available?url={url}"

r = requests.get(api)

print(r.json())
