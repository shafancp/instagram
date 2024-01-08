# Instagram Followers Count Extractor

## Overview

This Python script uses the `instaloader` library to extract the follower count of a given Instagram user. It's a straightforward tool that helps you retrieve the number of followers for a specified Instagram username.

## Prerequisites

1. [Python](https://www.python.org/downloads/) installed on your machine.
2. Install required dependencies using the following command:
   ```bash
   pip install instaloader
   ```

## Usage

1. Open the `instagram_followers.py` file.
2. Replace `'target_username'` with the Instagram username you want to get the followers count for.
3. Run the script using the following command:
   ```bash
   python instagram_followers.py
   ```

## Example

```python
# Replace 'target_username' with the Instagram username you want to get followers count for
target_username = 'example_user'

followers_count = get_instagram_followers_count(target_username)

if followers_count is not None:
    print(f"The Instagram user '{target_username}' has {followers_count} followers.")
```

## Error Handling

- If the specified profile does not exist, a `ProfileNotExistsException` will be caught and an error message will be displayed.
- Any other exceptions will be caught as `InstaloaderException` with a corresponding error message.

## Notes

- This script does not require Instagram API access but uses the `instaloader` library to scrape public profile information.
- Use responsibly and be aware of Instagram's terms of service.

## License

This project is licensed under the [MIT License](LICENSE).
