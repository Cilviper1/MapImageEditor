import os
import json
from bs4 import BeautifulSoup

# Path to the HTML file
HTML_FILE = '../LoginPage.html'
USERS_DIR = '../users'

def parse_login_page(html_file):
    with open(html_file, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
        username = None
        password = None
        # Find input fields by type or name
        for input_tag in soup.find_all('input'):
            if input_tag.get('type') == 'text' or input_tag.get('name') == 'username':
                username = input_tag.get('value', '')
            elif input_tag.get('type') == 'password' or input_tag.get('name') == 'password':
                password = input_tag.get('value', '')
        return username, password

def create_user(username, password):
    if not os.path.exists(USERS_DIR):
        os.makedirs(USERS_DIR)
    user_file = os.path.join(USERS_DIR, f"{username}.json")
    if os.path.exists(user_file):
        print("User already exists.")
        return False
    user_data = {
        'username': username,
        'password': password  # In production, hash the password!
    }
    with open(user_file, 'w', encoding='utf-8') as f:
        json.dump(user_data, f)
    print(f"User '{username}' created.")
    return True

def main():
    username, password = parse_login_page(HTML_FILE)
    if not username or not password:
        print("Username or password not found in HTML.")
        return
    create_user(username, password)

if __name__ == '__main__':
    main()