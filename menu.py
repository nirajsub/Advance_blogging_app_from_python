
from home import *
from database import *
from user import logged_in, user_id, login, logout, create_new_user
create_tables()

def home_menu():
    print("1. Register")
    print("2. Login")
    print("3. View all posts")
    print("q. Quit")

    choice = input("Enter your choice: ")
    return choice

def logged_in_menu():
    print("1. View all posts")
    print("2. Create a new post")
    print("3. Create a comment")
    print("4. View comments")
    print("5. User details")
    print("6. Posts by user")
    print("7. Comments by user")
    print("8. Logout")
    print("9. Post Detail")
    print("q. Quit")

    choice = input("Enter your choice: ")
    return choice

def main_menu():
    global logged_in  # Declare logged_in as global

    while True:
        if logged_in:
            logged_in_menus()
        else:
            home_menus()

def home_menus():
    global logged_in, user_id  # Declare logged_in as global
    while True:
        if logged_in:
            break
        else:
            choice = home_menu()
            if choice == 'q':
                break  # Exit the loop if the choice is 'q'
            elif choice == '1':
                create_new_user()
            elif choice == '2':
                logged_in, user_id = login()
            elif choice == '3':
                view_all_posts()
            else:
                print('Invalid choice.')

def logged_in_menus():
    global logged_in, user_id
    while True:
        if logged_in == False:
            break
        else:
            choice = logged_in_menu()
            if choice == 'q':
                break  # Exit the loop if the choice is 'q'
            elif choice == '1':
                view_all_posts()
            elif choice == '2':
                if logged_in:
                    user_id = user_id
                    print(user_id)
                    create_new_post(user_id)
                else:
                    print('Please login first.')
            elif choice == '3':
                if logged_in:
                    user_id = user_id
                    create_comment(user_id)
                else:
                    print('Please login first.')
            elif choice == '4':
                view_comments()
            elif choice == '5':
                user_details()
            elif choice == '6':
                posts_by_user()
            elif choice == '7':
                comments_by_user()
            elif choice == '8':
                logged_in = logout()
            elif choice == '9':
                view_post_detail()
            else:
                print('Invalid choice.')

if __name__ == '__main__':
    main_menu()

