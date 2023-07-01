# user.py
from authentication import *
# from menu import main_menu

logged_in = False
user_id = None
def create_new_user():
    username = input('Enter username: ')
    password = input('Enter password: ')
    fullname = input('Enter Full Name: ')
    email = input('Enter Email: ')
    phone = input('Enter Phone Number: ')
    bio = input('Enter Bio: ')
    create_user(username, password, fullname, email, phone, bio)
    print('User created successfully!')

def login():
    global logged_in, user_id
    username = input('Enter username: ')
    password = input('Enter password: ')
    user_id = authenticate_user(username, password)
    if user_id:
        logged_in = True
        user_id = user_id
        print('Login successful!')
        return True, user_id
    else:
        print('Invalid credentials.')
        return False, None

def logout():
    global logged_in, user_id  # Access the global logged_in variable
    if logged_in:
        logged_in = False  # Set logged-in status to False
        user_id = None # Reset the current user ID
        return False
        print('Logout successful!')
    else:
        print('You are not currently logged in.')

def get_user_details(user_id):
    
    print('User details:')


def get_posts_by_user(user_id):
    # Retrieve posts by the provided user ID
    # ...
    print('Posts by user:')
    # Print the posts
    # ...

def get_comments_by_user(user_id):
    # Retrieve comments by the provided user ID
    # ...
    print('Comments by user:')
    # Print the comments
    # ...
