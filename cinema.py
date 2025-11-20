class Movie:
    """Класс, описывающий фильм."""
    def __init__(self, movie_id, title, year, genres):
        self.movie_id = movie_id
        self.title = title
        self.year = year
        self.genres = genres
        self.reviews = []

    def add_review(self, user_id, rating, comment=""):
        if not (1 <= rating <= 10):
            raise InvalidRatingError(f"Рейтинг {rating} должен быть от 1 до 10")
        self.reviews.append({"user_id": user_id, "rating": rating, "comment": comment})

    def avg_rating(self):
        if not self.reviews:
            return 0.0
        return sum(r["rating"] for r in self.reviews) / len(self.reviews)

    def __str__(self):
        return f"Фильм {self.title} ({self.year})"


class User:
    """Класс, описывающий пользователя."""
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.watchlist = []

    def add_to_watchlist(self, movie):
        if not isinstance(movie, Movie):
            raise TypeError("Можно добавлять только объекты Movie")
        self.watchlist.append(movie)


class CinemaSystem:
    """Основной класс онлайн-кинотеатра."""
    def __init__(self, name):
        self.name = name
        self.movies = []
        self.users = []
        self.next_movie_id = 1
        self.next_user_id = 1

    def add_movie(self, title, year, genres):
        movie = Movie(self.next_movie_id, title, year, genres)
        self.movies.append(movie)
        self.next_movie_id += 1
        return movie

    def add_user(self, name):
        user = User(self.next_user_id, name)
        self.users.append(user)
        self.next_user_id += 1
        return user

    def find_movie_by_id(self, movie_id):
        for movie in self.movies:
            if movie.movie_id == movie_id:
                return movie
        raise MovieNotFoundError(f"Фильм с ID {movie_id} не найден")

    def find_user_by_id(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                return user
        raise UserNotFoundError(f"Пользователь с ID {user_id} не найден")


class MovieNotFoundError(Exception):
    pass


class UserNotFoundError(Exception):
    pass


class InvalidRatingError(Exception):
    pass