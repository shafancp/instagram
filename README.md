# Instagram Follower Scraper

## Description
This Python script extracts Instagram follower counts from a list of URLs provided in a CSV file.

## Requirements
- Python 3.x
- Pandas
- Instaloader

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/shafancp/instagram.git
   cd instagram
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
1. Prepare your CSV file (`urls.csv`) with a list of Instagram profile URLs.
   - Each URL should be in a separate row under the column header 'URL'.

2. Edit `login()` function in the script with your Instagram credentials:
   ```python
   loader.login("your_instagram_username", "your_instagram_password")
   ```

3. Run the script:
   ```
   python instafollowerscraper.py
   ```

4. Output:
   - The script will extract followers count for each profile URL and save the results in `result.csv`.

## Example CSV Format (urls.csv)
```
URL
https://www.instagram.com/profile1/
https://www.instagram.com/profile2/
https://www.instagram.com/profile3/
```

## Notes
- Ensure your Instagram account has appropriate permissions for scraping.
- Adjust the `time.sleep()` interval in the script to comply with Instagram's rate limits.
