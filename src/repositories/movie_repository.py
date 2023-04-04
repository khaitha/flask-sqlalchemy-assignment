from src.models import Movie
from src.models import db
class MovieRepository:

    def get_all_movies(self):
        # Query the movie table to get all movies
        movies = Movie.query.all()
        return movies

    def get_movie_by_id(self, movie_id):
        # Query the movie table to get the movie with the specified id
        movie = Movie.query.filter_by(movie_id=movie_id).first()

        return movie

    def create_movie(self, title, director, rating):
        # Create a new Movie object
        movie = Movie(title=title, director=director, rating=rating)

        # Add the new movie to the session and commit the transaction
        db.session.add(movie)
        db.session.commit()

        return movie

    def search_movies(self, title):
            # Query the movie table to get all movies that contain the title as a substring (case-insensitive)
            movies = Movie.query.filter(Movie.title.ilike(f'%{title}%')).all()
            return movies   


# Singleton to be used in other modules
movie_repository_singleton = MovieRepository()
