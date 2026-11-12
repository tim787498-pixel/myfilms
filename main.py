import json
import os

# Загружаем фильмы из файла
def load_movies():
    if not os.path.exists("movies.json"):
        print("❌ Файл movies.json не найден!")
        return []
    
    with open("movies.json", "r", encoding="utf-8") as f:
        return json.load(f)

# Показываем список
def show_movies(movies):
    print("\n" + "=" * 40)
    print("🎬 КАТАЛОГ ФИЛЬМОВ")
    print("=" * 40)
    for i, movie in enumerate(movies, 1):
        print(f"{i}. {movie['title']} ({movie['year']}) ⭐ {movie['rating']}")
    print("=" * 40)

# Показываем детали
def show_details(movies):
    show_movies(movies)
    try:
        choice = int(input("\nВведи номер фильма для подробностей (0 - выход): "))
        if choice == 0:
            return
        if 1 <= choice <= len(movies):
            movie = movies[choice - 1]
            print("\n" + "-" * 40)
            print(f"🎥 {movie['title']} ({movie['year']})")
            print(f"⭐ Рейтинг: {movie['rating']}")
            print(f"📝 Описание: {movie['description']}")
            print("-" * 40)
        else:
            print("⚠️ Такого номера нет.")
    except ValueError:
        print("⚠️ Введи число!")

# Главный цикл
def main():
    movies = load_movies()
    if not movies:
        return
    
    while True:
        show_details(movies)
        again = input("\nПосмотреть другой фильм? (д/н): ").lower()
        if again != 'д' and again != 'y':
            print("До встречи! 👋")
            break

if __name__ == "__main__":
    main()
