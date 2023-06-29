
from menu import *
from user import *
from database import *
from post import *

logged_in = False
current_user_id = None
create_tables()

# User Authentication
def login():
    global logged_in, current_user_id
    username = input('Enter username: ')
    password = input('Enter password: ')
    user_id = authenticate_user(username, password)
    if user_id:
        logged_in = True
        current_user_id = user_id
        print('Login successful!')
        return True, user_id, main_menu()
    else:
        print('Invalid credentials.')
        return False, None

def create_new_user():
    username = input('Enter username: ')
    password = input('Enter password: ')
    fullname = input('Enter Full Name: ')
    email = input('Enter Email: ')
    phone = input('Enter Phone Number: ')
    bio = input('Enter Bio: ')
    create_user(username, password, fullname, email, phone, bio)
    print('User created successfully!')
    return main_menu()

def logout():
    global logged_in, current_user_id  # Access the global logged_in variable
    if logged_in:
        logged_in = False  # Set logged-in status to False
        current_user_id = None # Reset the current user ID
        print('Logout successful!')
    else:
        print('You are not currently logged in.')
    return main_menu()

def create_new_post(user_id):
    if logged_in:
        title = input('Enter post title: ')
        content = input('Enter post content: ')
        create_post(title, content, user_id)
        print('Post created successfully!')
    else:
        print('Please login first.')

def view_all_posts():
    posts = get_all_posts()
    if not posts:
        print('No posts found.')
    else:
        for post in posts:
            post_id, title, content, username, timestamp = post
            print(f'Post ID: {post_id}')
            print(f'Title: {title}')
            print(f'Content: {content}')
            print(f'Author: {username}')
            print(f'Timestamp: {timestamp}')
            print('---')

def create_comment():
    if logged_in:
        post_id = input('Enter the post ID to comment on: ')
        content = input('Enter your comment: ')
        create_comment(post_id, current_user_id, content)
        print('Comment created successfully!')
    else:
        print('Please login first.')

def view_comments():
    post_id = input('Enter the post ID to view comments: ')
    comments = get_comments_for_post(post_id)
    if not comments:
        print('No comments found for this post.')
    else:
        for comment in comments:
            comment_id, content, username, timestamp = comment
            print(f'Comment ID: {comment_id}')
            print(f'Content: {content}')
            print(f'Author: {username}')
            print(f'Timestamp: {timestamp}')
            print('---')

def user_details():
    if logged_in:
        user = get_user_details(current_user_id)
        if user:
            user_id, username, name, bio, profile_picture = user
            print(f'User ID: {user_id}')
            print(f'Username: {username}')
            print(f'Name: {name}')
            print(f'Bio: {bio}')
            print(f'Profile Picture: {profile_picture}')
        else:
            print('User not found.')
    else:
        print('Please login first.')

def posts_by_user():
    user_id = input('Enter the user ID to view their posts: ')
    posts = get_posts_by_user(user_id)
    if not posts:
        print('No posts found for this user.')
    else:
        for post in posts:
            post_id, title, content = post
            print(f'Post ID: {post_id}')
            print(f'Title: {title}')
            print(f'Content: {content}')
            print('---')

def comments_by_user():
    user_id = input('Enter the user ID to view their comments: ')
    comments = get_comments_by_user(user_id)
    if not comments:
        print('No comments found for this user.')
    else:
        for comment in comments:
            comment_id, content = comment
            print(f'Comment ID: {comment_id}')
            print(f'Content: {content}')
            print('---')

def logged_in_menus():
    choice = logged_in_menu()

    while choice != 'q':
        if choice == '1':
            view_all_posts()
        elif choice == '2':
            if logged_in:
                user_id = current_user_id
                create_new_post(user_id)
            else:
                print('Please login first.')
        elif choice == '3':
            create_comment()
        elif choice == '4':
            view_comments()
        elif choice == '5':
            user_details()
        elif choice == '6':
            posts_by_user()
        elif choice == '7':
            comments_by_user()
        elif choice == '8':
            logout()
        else:
            print('Invalid choice.')
        choice = logged_in_menu()

def home_menus():
    choice = home_menu()
    while choice != 'q':
        if choice == '1':
            create_new_user()
        elif choice == '2':
            logged_in, user_id = login()
        elif choice == '3':
            view_all_posts()
        else:
            print('Invalid choice.')
        choice = home_menu()

def main_menu():
    if logged_in == True:
        logged_in_menus()
    else:
        home_menus()

if __name__ == '__main__':
    main_menu()
