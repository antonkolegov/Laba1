import json
import xml.etree.ElementTree as ET
from xml.dom import minidom
import os
from cinema import Movie 

def save_movies_to_json(movies, filename="library_system.json"):
    """Сохранить фильмы в JSON."""
    data = {
        "cinema": {
            "id": 1,
            "name": "My Cinema",
            "movies": [
                {
                    "id": m.movie_id,
                    "title": m.title,
                    "year": m.year,
                    "genres": m.genres,
                    "reviews": m.reviews
                }
                for m in movies 
            ]
        }
    }
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def load_movies_from_json(filename="library_system.json"):
    """Загрузить фильмы из JSON."""
    if not os.path.exists(filename):
        return []
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError:
        print("Ошибка чтения JSON-файла. Будет создан новый.")
        return []

    movies = []
    for m_data in data.get("cinema", {}).get("movies", []):
        movie = Movie(
            m_data["id"],
            m_data["title"],
            m_data["year"],
            m_data["genres"]
        )
        movie.reviews = m_data["reviews"]
        movies.append(movie)
    return movies


def save_movies_to_xml(movies, filename="library_system.xml"):
    """Сохранить фильмы в XML в формате"""
    root = ET.Element("cinema_system")
    cinema = ET.SubElement(root, "cinema", id="1", name="My Cinema")
    movies_el = ET.SubElement(cinema, "movies")
    for movie in movies:
        movie_el = ET.SubElement(movies_el, "movie",
                                 id=str(movie.movie_id),
                                 title=movie.title,
                                 year=str(movie.year),
                                 genres=",".join(movie.genres))
        reviews_el = ET.SubElement(movie_el, "reviews")
        for r in movie.reviews:
            ET.SubElement(reviews_el, "review",
                          user_id=r["user_id"],
                          rating=str(r["rating"]),
                          comment=r["comment"])

    rough = ET.tostring(root, 'utf-8')
    reparsed = minidom.parseString(rough)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(reparsed.toprettyxml(indent="  "))


def load_movies_from_xml(filename="library_system.xml"):
    """Загрузить фильмы из XML"""
    if not os.path.exists(filename):
        return []
    tree = ET.parse(filename)
    root = tree.getroot()
    movies = []
    for movie_el in root.findall(".//movie"):
        movie_id = int(movie_el.get("id"))
        title = movie_el.get("title")
        year = int(movie_el.get("year"))
        genres = movie_el.get("genres").split(",") if movie_el.get("genres") else []
        movie = Movie(movie_id, title, year, genres)
        reviews_el = movie_el.find("reviews")
        if reviews_el is not None:
            for r_el in reviews_el.findall("review"):
                review = {
                    "user_id": r_el.get("user_id"),
                    "rating": int(r_el.get("rating")),
                    "comment": r_el.get("comment") or ""
                }
                movie.reviews.append(review)
        movies.append(movie)
    return movies