import instaloader

def get_instagram_followers_count(username):
    loader = instaloader.Instaloader()

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

if __name__ == "__main__":
    # Replace 'target_username' with the Instagram username you want to get followers count for
    target_username = 'fs_beatzz'

    followers_count = get_instagram_followers_count(target_username)

    if followers_count is not None:
        print(f"The Instagram user '{target_username}' has {followers_count} followers.")