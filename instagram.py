import requests
import json

# Replace with your Instagram Graph API access token
ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"

def download_instagram_stories(user_id):
    url = f"https://graph.instagram.com/{user_id}/stories?fields=media_url&access_token={ACCESS_TOKEN}"

    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.text)

        for story in data['data']:
            media_url = story['media_url']
            filename = media_url.split('/')[-1]

            response = requests.get(media_url, stream=True)
            if response.status_code == 200:
                with open(filename, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        if not chunk:
                            break
                        f.write(chunk)
                print(f"Downloaded {filename}")
            else:
                print(f"Failed to download {filename}")
    else:
        print("Error fetching stories")

# Replace with the Instagram user ID
user_id = "YOUR_INSTAGRAM_USER_ID"
download_instagram_stories(user_id)