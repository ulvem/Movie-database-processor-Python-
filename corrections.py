from data import movies

from data import movies

def dramas(movies):
    """
    This function takes a list of movies and returns a list of titles
    of movies that have 'Drama' in their genres.

    :param movies: List of dictionaries, where each dictionary represents a movie.
    :return: List of titles of movies with 'Drama' in their genres.
    """
    drama_movies = [movie['title'] for movie in movies if 'Drama' in movie['genres']]
    return drama_movies


# Get the list of drama movies
drama_movies = dramas(movies)
print(drama_movies)

def findByGenre(genre, movies):
    """
    This function takes a genre and a list of movies, and returns a list of titles
    of movies that match the specified genre.

    :param genre: The genre to search for.
    :param movies: List of dictionaries, where each dictionary represents a movie.
    :return: List of titles of movies that match the specified genre.
    """
    genre_movies = [movie['title'] for movie in movies if genre in movie['genres']]
    return genre_movies

# Get the list of action movies
action_movies = findByGenre('Action', movies)
print(action_movies)

def longestMovie(movies):
    """
    This function takes a list of movies and returns the movie with the longest runtime.

    :param movies: List of dictionaries, where each dictionary represents a movie.
    :return: The dictionary representing the movie with the longest runtime.
    """
    if not movies:
        return None

    longest = max(movies, key=lambda movie: movie['runtime'])
    return longest

# Get the movie with the longest runtime
longest_movie = longestMovie(movies)
print(longest_movie)

def longestMovieByGenre(genre, movies):
    """
    This function takes a genre and a list of movies, and returns the movie with the longest runtime
    within the specified genre.

    :param genre: The genre to search for.
    :param movies: List of dictionaries, where each dictionary represents a movie.
    :return: The dictionary representing the movie with the longest runtime in the specified genre.
    """
    genre_movies = [movie for movie in movies if genre in movie['genres']]
    if not genre_movies:
        return None

    longest = max(genre_movies, key=lambda movie: movie['runtime'])
    return longest

