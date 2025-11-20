from cinema import CinemaSystem, InvalidRatingError
from data_manager import save_movies_to_json, load_movies_from_json, save_movies_to_xml, load_movies_from_xml

def main():
    
    cinema = CinemaSystem("My Cinema")
    cinema.add_movie("Dune", 2021, ["Sci-Fi"])
    cinema.add_movie("Interstellar", 2014, ["Sci-Fi", "Drama"])
    cinema.add_movie("The Dark Knight", 2008, ["Action", "Drama"])
    cinema.add_movie("Inception", 2010, ["Sci-Fi", "Action"])
    cinema.add_movie("Spirited Away", 2001, ["Animation", "Family"])

    cinema.add_user("Антон")
    cinema.add_user("Андрей")
    cinema.add_user("Борис")
    cinema.add_user("Катя")

    try:

        cinema.movies[0].add_review(1, 9, "Отличная адаптация.")
        cinema.movies[0].add_review(2, 8, "Визуально впечатляет.")
        cinema.movies[0].add_review(3, 9, "Лучший фильм года.")

        cinema.movies[1].add_review(2, 10, "Гениально.")
        cinema.movies[1].add_review(4, 8, "Слишком длинный но красивый.")
        cinema.movies[1].add_review(1, 9, "Супер.")

        cinema.movies[2].add_review(1, 10, "Лучший супергеройский фильм.")
        cinema.movies[2].add_review(3, 9, "Легендарный.")
        cinema.movies[2].add_review(4, 8, "Напряжённый и мрачный.")

        cinema.movies[3].add_review(2, 9, "Захватывающий сюжет.")
        cinema.movies[3].add_review(1, 10, "Идеальный фильм.")
        cinema.movies[3].add_review(3, 8, "Сложно но интересно.")

        cinema.movies[4].add_review(4, 10, "Волшебная анимация.")
        cinema.movies[4].add_review(2, 9, "Трогательная история.")
        cinema.movies[4].add_review(3, 8, "Гениальный Миyадзаки.")

        cinema.movies[0].add_review(1, 12, "Слишком длинный.")
    except InvalidRatingError:
        pass  
    save_movies_to_json(cinema.movies)
    save_movies_to_xml(cinema.movies)
    loaded = load_movies_from_json()
    print(f"Загружено фильмов: {len(loaded)}")
    for m in loaded:
        print(f"{m.title} ({m.year}) — рейтинг: {m.avg_rating():.1f}")

if __name__ == "__main__":
    main()