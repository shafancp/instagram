import pandas as pd
import instaloader
from urllib.parse import urlparse
import csv
import time

loader = instaloader.Instaloader()
loader.login("username", "password")
print("Login successful!")

def get_instagram_followers_count(username):
    try:
        profile = instaloader.Profile.from_username(loader.context, username)
        followers_count = profile.followers
        return followers_count
    except instaloader.exceptions.ProfileNotExistsException:
        print(f"Error: Profile with username '{username}' not found.")
        return None
    except instaloader.exceptions.InstaloaderException as e:
        print(f"Error: {e}")
        return None

def extract_username(url):
    parsed_url = urlparse(url)
    path_parts = parsed_url.path.split('/')
    username = path_parts[1] if len(path_parts) > 1 else None
    return username

df = pd.read_csv('urls.csv')
data = []
for index, row in df.iterrows():
    url = row['URL']
    username = extract_username(url)
    if username:
        followers_count = get_instagram_followers_count(username)
        data.append([username, url, followers_count])
        time.sleep(5)

result_df = pd.DataFrame(data, columns=['Username', 'URL', 'Followers'])
result_df.to_csv('result.csv', index=False)