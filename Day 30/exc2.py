facebook_post = [
    {'likes': 21, 'comments':2},
    {'likes': 13, 'comments':2, 'shares':3},
    {'shares': 33, 'comments':8, 'shares':5},
    {'shares': 4, 'comments':2},
    {'likes': 1, 'comments':1},
    {'likes': 19, 'comments':3},
]

total_likes = 0

for post in facebook_post:
    try:
        total_likes += post['likes']
    except KeyError:
        pass
print(total_likes)