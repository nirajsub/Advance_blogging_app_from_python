
from post import *
from user import logged_in, user_id

def create_new_post(user_id):
    global logged_in
    print(logged_in)
    print(user_id)
    title = input('Enter post title: ')
    content = input('Enter post content: ')
    create_post(title, content, user_id)
    print('Post created successfully!')

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

def view_post_detail():
    post_id = input("Enter post ID: ")
    post = get_single_posts(post_id)
    print(f'Post ID: {post_id}')
    print(f'Title: {title}')
    print(f'Content: {content}')
    print(f'Author: {username}')
    print(f'Timestamp: {timestamp}')
    print('---')

def create_comments(user_id):
    if logged_in:
        post_id = input('Enter the post ID to comment on: ')
        content = input('Enter your comment: ')
        create_comment(post_id, user_id, content)
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
        user_id = user_id
        user = get_user_by_id(user_id)
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

