#sorted- returns not a copy=> sorted[lista którą chcemy sortować, key = lambda x z listy: x['co chcemy sortowac'])
users = [
	{"username": "samuel", "tweets": ["I love cake", "I love pie", "hello world!"]},
	{"username": "katie", "tweets": ["I love my cat"]},
	{"username": "jeff", "tweets": [], "color": "purple"},
	{"username": "bob123", "tweets": [], "num": 10, "color": "teal"},
	{"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
	{"username": "guitar_gal", "tweets": []}
]

# To sort users by their username
print(sorted(users,key=lambda user: user['username']))

# Finding our most active users...
# Sort users by number of tweets, descending
print(sorted(users,key=lambda user: len(user["tweets"]), reverse=True))

# ANOTHER EXAMPLE DATA SET==================================
songs = [
	{"title": "happy birthday", "playcount": 1},
	{"title": "Survive", "playcount": 6},
	{"title": "YMCA", "playcount": 99},
	{"title": "Toxic", "playcount": 31}
]

# To sort songs by playcount
print(sorted(songs, key=lambda s: s['playcount']))

def is_all_strings(list):
    # return all([iter for iter in list if iter == str(iter)]) #['a','b'] drukuje tylko str (bez all czyli określenia True/False) z all #True wszędzie, gdzie jest str
    return all([type(iter) == str for iter in list]) #tutaj działa też (iter == str(iter)...)
print(is_all_strings(['a','b',2,])) #False
print(is_all_strings(['a','b']))    #True
