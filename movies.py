import requests


url = "https://imdb.iamidiotareyoutoo.com/search?q=something"
response = requests.get(url)


data = response.json()


movie_lists = []

for movie in data["description"]:
    movie_lists.append({
        "title": movie["#TITLE"],
        "year": movie["#YEAR"],
        "poster": movie["#IMG_POSTER"]
    })
