"""
- Enter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie, and 'q' to quit:

- Add Movies
- See movies
- Find a movie
- Stop running the program

Tasks:
[x]: Decide where to store movies
[x]: What is the format of a movie?
[x]: Show the user the main interface and get their input
[x]: Allow users to add movies
[]: Show all their movies
[]: Find a movie
[x]: Stop running the program when they type 'q'
"""

movies = []

"""
movie = {
    'name': ... (str),
    'director': ... (str),
    'year': ... (int)
"""

def menu():
    user_input = input("\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie, and 'q' to quit: ")

    if user_input == 'q':
        print("Exiting The program...")
        quit_movie()

    while user_input != 'q':
        if user_input == 'a':
            add_movie()
        elif user_input == 'l':
            show_movies()
        elif user_input == 'f':
            find_movie()
        else:
            print("Unknown command-please try again")
#       elif user_input == 'q':           //This will not run
#           print("Stopping Program...")  //This will not run

        user_input = input("\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie, and 'q' to quit: ")

def add_movie():
    name = input("Enter the movie name: ")
    director = input("Enter the movie director: ")
    year = int(input("Enter the movie release year: "))

    movies.append({
        'name': name,
        'director': director,
        'year': year
    })

def show_movies():
    for movie in movies:
        show_movie_details(movie)

def show_movie_details(movie):
    print(f"Name: {movie['name']}")
    print(f"Director: {movie['director']}")
    print(f"Release Year: {movie['year']}")

#def find_movie():


menu()

#print(movies)