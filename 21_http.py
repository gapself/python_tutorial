# REQUEST MODULE
import requests
res = requests.get("https://kobietydokodu.pl/")
print(res)
print(res.ok)

import requests
url = "https://kobietydokodu.pl/"
response = requests.get(url)

print(f"Your request to {url} came back w/ status code {response.status_code}")
# print(response.text)

# REQUESTING JSON with Python
# REQUESTS HEADERS
import requests
url = "https://icanhazdadjoke.com/"
response = requests.get(url)
print(response.text)

import requests
url = "https://icanhazdadjoke.com/"
response = requests.get(url,headers={"Accept":"text/plain"})
print(response.text)

import requests
url = "https://icanhazdadjoke.com/"
#we are making request, then asking for json, json comes back, turning into python
# and then we can manipulate it
response = requests.get(url,headers={"Accept":"application/json"})
data = response.json()
# print(type(data))
print(data)
print(f"status:{data['joke']}")

# SENDING REQ with PARAMS
# QUERY STrING
# a way to pass data to the server as part of a GET request
# https://www.google.com/search?
source=hp
ei=becwW_75LoWusQGb4LfQAQ
q=python #additional info
oq=python
# gs_l=psy-ab.3..35i39k1l2j0i67k1l3j0j0i67k1j0j0i67k1l2.794.1533.0.1735.7.6.0.0.0.0.144.489.1j3.4.0....0...1c.1.64.psy-ab..3.4.485.0..0i131k1.0.9b2o7M4G2XU

# if I wanna see 2 jokes/page:
# https://icanhazdadjoke.com/search?term=cat&limit=2
import requests
url = "https://icanhazdadjoke.com/search?"
response = requests.get(
    url,
    headers={"Accept":"application/json"},
    #api of this website, im searching for "dad jokes"
    params={"term":"cat"}
)
data = response.json()
print(data["results"]) #list of dictionaries [{}]
print(data) #{} dict
# {'current_page': 1, 'limit': 20, 'next_page': 1, 'previous_page': 1, 'results': [{'id': '8UnrHe2T0g', 'joke': '‘Put the cat out’ … ‘I didn’t realize it was on fire'}, {'id': 'daaUfibh', 'joke': 'Why was the big cat disqualified from the race? Because it was a cheetah.'}, {'id': 'iGJeVKmWDlb', 'joke': 'My cat was just sick on the carpet, I don’t think it’s feline well.'}, {'id': '0wcFBQfiGBd', 'joke': 'Did you hear the joke about the wandering nun? She was a roman catholic.'}, {'id': '1wkqrcNCljb', 'joke': "Did you know that protons have mass? I didn't even know they were catholic."}], 'search_term': 'cat', 'status': 200, 'total_jokes': 5, 'total_pages': 1}

# PROJEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEECT
# moje rozwiązanie (bez random(wyświetlały się wszystkie jokes)
import requests
from pyfiglet import figlet_format
from termcolor import colored
from random import choice

logo = "Dad Joke 300"
ascii_art = figlet_format(logo)
colored_ascii = colored(ascii_art, color='magenta')
print(colored_ascii)

url = "https://icanhazdadjoke.com/search?"
question = input("Let me tell you a joke! Give me a topic:")
res = requests.get(
    url,
    headers={"Accept": "application/json"},
    params={"term": question}
).json()
results = res["results"]
if res["total_jokes"] is not 0:
    print(f"I've got {res['total_jokes']} jokes about {question}.Here's one: \n ", choice(results)["joke"])
    # I found one joke about:
    # print(results[0]["joke"])
elif res["total_jokes"] is 0:
    print("Sorry we dont have any jokes")
