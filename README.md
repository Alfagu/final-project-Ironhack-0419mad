# Movie Finder :film_projector: :file_cabinet:

**Alfonso Aguado**

**Ironhack Madrid April 2019 Part-time**

## Overview :eyes:

This has been a personal project of mine for a while now. It try to answer the questions: 

* What movie do you want to watch today at the cinema? Or what good movies are right now at the Cinema?
  * In the near future, you could go into you app and set a date and the app will recommend you which movie is better for you taking in count your preferences, and which cinema is closest to you to watch that movie.
* We want to see if the Recomendation System fro the IMDb Votes is good for recommend movies on the cinema at the moment.
  * Recommendation system use the distances between data, to locate if your input or query could be similar to others on the database.

* There are many ways of approaching this matter but now we are going to use 2:

![Resultado de imagen de recommendation systems](http://datameetsmedia.com/wp-content/uploads/2018/05/2ebah6c-1.png)

* The project can be use from 2 different displays:
  - Terminal
  - Tkinter GUI

## Data Preparation :chart_with_upwards_trend: :gear:

### Overview:

* The dataset is a list of around 45.000 movies, 26 million ratings from over 270.000 users on IMDb.
* We have take or dataset from [Kaggle](https://www.kaggle.com/rounakbanik/the-movies-dataset).
* We have use 2 datasets for this proyect for the moment:
  1. **movies_metadata.csv:** The main Movies Metadata file. Contains information on 45,000 movies featured in the Full MovieLens dataset. Features include posters, backdrops, budget, revenue, release dates, languages, production countries and companies.
  2. **links_small.csv:** Contains the TMDB and IMDB IDs of a small subset of 9,000 movies of the Full Dataset.

### Data Ingestion

* I donwload the data set into my src :file_folder: and call it from the Jupyter Notebook or .py file:

  `md = pd.read_csv('../src/movies_metadata.csv')
  md.head()`

* There are IMDb API availables for python:

  - [IMDbPY](https://pypi.org/project/IMDbPY/)
  - [OMDb](http://www.omdbapi.com/)

### Data Wrangling and Cleaning

* The Data was pretty clean and useful but we need it to make some changes to better suite the propose of the exercise:
  - Use lambda to take the names betweens the [lists brackets] they were on the datasets.
  - Drop the nulls from the vote_count columns.
  -  Split the release dates to only takes the years.
  - Change the vote_count and vote_average and transformed in to int.

## Data Analysis :chart_with_downwards_trend: :mag:

### Overview

To be able to make a Resommendation System you need to feed the system with as much numeric data as possible to be able to calculate de distances between movies, this way the query will be as accurate as possible.

### Simple Recommender

The Simple Recommender offers generalized recommnendations to every user based on movie popularity and (sometimes) genre. The basic idea behind this recommender is that movies that are more popular and more critically acclaimed will have a higher probability of being liked by the average audience. This model does not give personalized recommendations based on the user.

The implementation of this model is extremely trivial. All we have to do is sort our movies based on ratings and popularity and display the top movies of our list. As an added step, we can pass in a genre argument to get the top movies of a particular genre.

I use the TMDB Ratings to come up with our Top Movies Chart. I will use IMDB's weighted rating formula to construct my chart. Mathematically, it is represented as follows:

Weighted Rating (WR) = (vv+m.R)+(mv+m*C) where,

v is the number of votes for the movie m is the minimum votes required to be listed in the chart R is the average rating of the movie C is the mean vote across the whole report.

```python
def weighted_rating(x):    
   v = x['vote_count']    
   R = x['vote_average']    
   return (v/(v+m) * R) + (m/(m+v) * C)
 
qualified['wr'] = qualified.apply(weighted_rating, axis=1)
qualified = qualified.sort_values('wr',ascending=False).head(250)
```

### Content Based Recommende

The recommender we built in the previous section suffers some severe limitations. For one, it gives the same recommendation to everyone, regardless of the user's personal taste. If a person who loves romantic movies (and hates action) were to look at our Top 15 Chart, s/he wouldn't probably like most of the movies. If s/he were to go one step further and look at our charts by genre, s/he wouldn't still be getting the best recommendations.

To personalise our recommendations more, I am going to build an engine that computes similarity between movies based on certain metrics and suggests movies that are most similar to a particular movie that a user liked. Since we will be using movie metadata (or content) to build this engine, this also known as Content Based Filtering.

I will build two Content Based Recommenders based on:

- Movie Overviews and Taglines
- Movie Cast, Crew, Keywords and Genre

Also, as mentioned in the introduction, I will be using a subset of all the movies available to us due to limiting computing power available.

#### Movie Description Based Recommender

Let us first try to build a recommender using movie descriptions and taglines. We do not have a quantitative metric to judge our machine's performance so this will have to be done qualitatively.

```python
smd['tagline'] = smd['tagline'].fillna('')
smd['description'] = smd['overview'] + smd['tagline']
smd['description'] = smd['description'].fillna('')

tf = TfidfVectorizer(analyzer='word', ngram_range=(1, 2), min_df=0, stop_words='english')
tfidf_matrix = tf.fit_transform(smd['description'])
```

#### Cosine Similarity

```Python
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
cosine_sim[0]
array([1.        , 0.00680476, 0.        , ..., 0.        , 0.00344913,\n       0.        ])
```

We now have a pairwise cosine similarity matrix for all the movies in our dataset. The next step is to write a function that returns the 30 most similar movies based on the cosine similarity score.

```python
def get_recommendations(title):
  	idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:31]
    movie_indices = [i[0] for i in sim_scores]
    return titles.iloc[movie_indices]
```

We're all set. Let us now try and get the top recommendations for a few movies and see how good the recommendations are.

## Conclusion

* The 2 ways of building the engine are capable but the Content Based Recommende, proof to be more accurate than just the Simple Recommende.
* This is an easy way of approaching a Netflix recommendation engine throught Python code and easy to implement.
* What are the next steps?
  - Get the GUI to be fully operated.
  - Connect to a Netflix API to be able to replicate this with new and versatile input.
  - Get the Maps feature working to set the Cinema Geolocalozation.
  - To built and App that englobe all this features.
