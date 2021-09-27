from tkinter import *
import imdb

ia = imdb.IMDb()

def movie_ID():
  for movie in ia.get_movie(input("input movie:")):
      m_ID = movie[0].m_ID
      query = ia.get_movie(m_ID)
  print(query)

movie_ID()
