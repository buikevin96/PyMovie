"""
- Enter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie, and 'q' to quit:

- Add Movies
- See movies
- Find a movie
- Stop running the program

Tasks:
[]: Decide where to store movies
[]: What is the format of a movie?
[x]: Show the user the main interface and get their input
[]: Allow users to add movies
[]: Show all their movies
[]: Find a movie
[x]: Stop running the program when they type 'q'
"""

def menu():
    user_input = input("Enter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie, and 'q' to quit: ")

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

        user_input = input("Enter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie, and 'q' to quit: ")


menu()
