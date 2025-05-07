import json
import os   

file_path = 'movies.json'

if os.path.exists(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
else:
    data = {"movies": []} 
movies = data.get("movies", [])
print("current movies:")
for movie in movies:
    print(f"{movie['title']} - {movie['genres']} - {movie['rating']}") 
    
def search_movie(title):    
    for movie in movies:
        if movie["title"].lower() == title.lower():
            print("\nmovie found:")
            print(json.dumps(movie, indent=4))
            return movie
    print("movie not found.")
    return None

def add_movie(title, director, rating, genres):
    if any(m["title"].lower() == title.lower() for m in movies):
        print(f"movie '{title}' already exists. Not added.")
        return
    new_id = max((m["id"] for m in movies), default=0) + 1  
    movies.append({
        "id": new_id,
        "title": title,
        "director": director,
        "rating": rating,
        "genres": genres
    })
    print(f"movie '{title}' added.")
    
def update_rating(title, new_rating):
    movie = search_movie(title)
    if movie:
        movie["rating"] = new_rating
        print(f"updated rating of '{title}' to {new_rating}.")  

def save_movies():
    with open(file_path, "w") as file:
        json.dump({"movies": movies}, file, indent=4)
    print("changes saved to movies.json.")
          
def generate_report():
    print("\ntop 3 movies by rating:")
    top_movies = sorted(movies, key=lambda m: m["rating"], reverse=True)[:3]
    for movie in top_movies:
        print(f"- {movie['title']} ({movie['rating']})")

    print("\nmovies per genres:")
    genre_count = {}
    for movie in movies:
        genres = movie["genres"]
        genre_count[genres] = genre_count.get(genres, 0) + 1

    for genres, count in genre_count.items():
        print(f"- {genres}: {count}")         

while True:
    print("\n movie Manager Menu:")
    print("1. search for a movie")
    print("2. add a new movie")
    print("3. update movie rating")
    print("4. generate report")
    print("5. save & exit")

    choice = input("choose an option (1-5): ")

    if choice == "1":
        title = input("enter the movie title to search: ")
        search_movie(title)

    elif choice == "2":
        title = input("enter movie title: ")
        director = input("enter director name: ")
        try:
            rating = float(input("enter rating (0-10): "))
        except ValueError:
            print("invalid rating. must be a number.")
            continue
        genres_input = input("enter genres (comma-separated): ")
        genres = [g.strip() for g in genres_input.split(",")]
        add_movie(title, director, rating, genres)

    elif choice == "3":
        title = input("enter movie title to update rating: ")
        try:
            new_rating = float(input("enter new rating (0-10): "))
        except ValueError:
            print("invalid rating. must be a number.")
            continue
        update_rating(title, new_rating)

    elif choice == "4":
        generate_report()

    elif choice == "5":
        save_movies()
        print("exiting. goodbye!")
        break

    else:
        print("invalid choice. please try again.")

    
    
      
    