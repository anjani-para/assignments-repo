# title: imdb assignment.
import json
from pprint import pprint
data = None
with open("imdb_movies.json") as f:
    data = json.load(f)
# pprint(data)

# 1) Print the top director with maximum number of movies.
from collections import Counter
directors_list = []
for i in data:
    directors_list.append(i['director'])
director_counter = Counter(directors_list)
print("top director with max no.of movies is:", (max(director_counter.items(), key=lambda x: x[1]))[0])

# 2) Print the popular genere watched by most of the audiance.
genere_list = []
for i in data:
    genere_list.extend(i['genre'])
# print(genere_list)
genere_counter = Counter(genere_list)
print("the popular genere watched by most of the audiance is:", (max(genere_counter.items(), key=lambda x: x[1]))[0])

# 3) Print out the top ten movies, according to imdb score.
imdbscore_list = []
for i in data:
    imdbscore_list.append(i['imdb_score'])
count = 0
top10_score = []
for i in sorted(imdbscore_list, reverse=True):
    count += 1
    if count <= 10:
        top10_score.append(i)
print("top 10 movies according to the imdb_score is: ")
for i in data:
    if i["imdb_score"] in top10_score:
        print(i['name'])

# 4) print the least watched movie based on their imdb_score
for i in data:
    if i['imdb_score'] == min(imdbscore_list):
        print("least watched movie based on their imdb_score is: ", i['name'])

# 5) Print the best director in the first hundred movies.
popularity_list = []
count = 0
for i in data:
    count += 1
    if count <= 100:
        popularity_list.append(i['99popularity'])
for i in data:
    if i['99popularity'] == max(popularity_list):
        print("the best director in the first hundred movies is: ", i['director'])
