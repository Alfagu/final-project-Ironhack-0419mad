import imdb

ia = imdb.IMDb()

movies = ia.search_movie('matrix')

movie_ID = (movies[0].movieID)

print(movie_ID)







