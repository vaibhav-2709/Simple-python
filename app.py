def greet_user(username):
    print(f"Hello, {username}!")

if __name__ == "__main__":
    user = input("Enter your name: ")
    greet_user(user)