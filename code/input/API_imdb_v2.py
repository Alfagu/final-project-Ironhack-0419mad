# importing the module
import imdb
from PIL import Image
import requests as re
from io import BytesIO

# creating instance of IMDb
ia = imdb.IMDb()

# Ask about any movie that you want    
movies = ia.search_movie(input("input movie:"))

# We get the ID of the movie requested
movie_ID = (movies[0].movieID)
  
# getting information
query = ia.get_movie(movie_ID)

#Trying to get the movie poster
url = re.get(query['cover url'])            

img = Image.open(BytesIO(url.content))
"""
img.show()
"""
# printing the query name or Title
"""
print("Title:",query)
"""
# get and print released year of the movie
year = query['year']
"""
print("Year:", year)
"""
# getting rating of the movie and printed
rating = query.data['rating']
"""
print("Rating:", rating)
"""
# Here we ask the API for the director of the movie and we printed 
"""
for director in query['directors']:
    print("Directors:",director['name'])
"""
# An genre
genre = query['genre']
"""
print("Genre:", genre)

# Then we want to have the plot displaid 
plot = query['plot'][0]
if plot == []: 
    print("Plot: No Data")
else:
    print("Plot:", plot)
"""
def movie_func():
    img.show()
    print("Title:",query)
    print("Year:", year)
    print("Rating:", rating)
    for director in query['directors']:
        print("Directors:",director['name'])
    print("Genre:", genre)
    plot = query['plot'][0]
    if plot == []:
        print("Plot: No Data")
    else:
        print("Plot:", plot)

movie_func()
quit()

