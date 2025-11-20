from cinema import CinemaSystem, InvalidRatingError, MovieNotFoundError, UserNotFoundError
from data_manager import save_movies_to_json, load_movies_from_json, save_movies_to_xml, load_movies_from_xml

def main():
    # Создание системы
    cinema = CinemaSystem("My Cinema")

    # Добавление фильмов
    movie1 = cinema.add_movie("Dune", 2021, ["Sci-Fi"])
    movie2 = cinema.add_movie("Interstellar", 2014, ["Sci-Fi", "Drama"])

    # Добавление пользователей
    user1 = cinema.add_user("Антон")
    user2 = cinema.add_user("Алиса")

    # Добавление отзывов
    try:
        movie1.add_review(user1.user_id, 9, "Отличная адаптация!")
        movie1.add_review(user2.user_id, 8, "Очень понравилось")
        movie1.add_review(user1.user_id, 11, "Слишком длинный")
    except InvalidRatingError as e:
        print("Ошибка при добавлении отзыва:", e)

    # Сохранение в JSON и XML
    save_movies_to_json(cinema.movies)
    save_movies_to_xml(cinema.movies)
    print("Данные сохранены в library_system.json и library_system.xml")

    # Загрузка из JSON
    loaded_movies = load_movies_from_json()
    print(f"Загружено фильмов: {len(loaded_movies)}")
    for m in loaded_movies:
        print(f"{m} — средний рейтинг: {m.avg_rating():.1f}")

if __name__ == "__main__":
    main()