import csv
from collections import defaultdict, namedtuple
import os
from urllib.request import urlretrieve

movie_data = 'https://raw.githubusercontent.com/pybites/challenges/solutions/13/movie_metadata.csv'
movie_csv = 'movie.csv'
urlretrieve(movie_data, movie_csv)
Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director(data=movie_csv):
    """Extracts all movies from csv and stores them in a dictionary
       where keys are directors, and values is a list of movies (named tuples)"""
    directors = defaultdict(list)
    with open(data, encoding='utf-8') as file:
        for line in csv.DictReader(file):
            try:
                director = line['director_name']
                title = line['movie_title']
                year = line['year']
                score = line['imdb_score']
            except ValueError:
                continue
            m = Movie(title=title, year=year, score=score)
            directors[director].append(m)


# def calc_mean_score(movies):
#     """Helper method to calculate mean of list of Movie namedtuples,
#        round the mean to 1 decimal place"""
#     pass
#
#
# def get_average_scores(directors):
#     """Iterate through the directors dict (returned by get_movies_by_director),
#        return a list of tuples (director, average_score) ordered by highest
#        score in descending order. Only take directors into account
#        with >= MIN_MOVIES"""
#     pass
get_movies_by_director()
