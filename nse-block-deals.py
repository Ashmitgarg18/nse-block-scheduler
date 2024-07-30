import requests
from datetime import datetime

# Get current date
current_date = datetime.now().strftime("%Y-%m-%d")

# URL of the block deals report
url = 'https://nsearchives.nseindia.com/content/equities/block.csv'

# Headers to mimic a real browser visit
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Send a GET request to the URL
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Save the content to a file with the current date in the filename
    filename = f'block_deals_{current_date}.csv'
    with open(filename, 'wb') as file:
        file.write(response.content)
    print(f"Download successful! Saved as {filename}")
else:
    print(f"Failed to download the report. Status code: {response.status_code}")
