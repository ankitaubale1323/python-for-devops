import requests
import json


API_URL = "https://jsonplaceholder.typicode.com/posts"
OUTPUT_FILE = "output.json"


def fetch_api_data(url):
    """
    Fetch data from API and return JSON response.
    Handles network-related errors.
    """
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        print("✅ API request successful")
        return response.json()

    except requests.exceptions.RequestException as error:
        print(f"❌ API request failed: {error}")
        return None


def process_posts(posts, limit=5):
    """
    Extract meaningful fields from API response.
    """
    processed_data = []

    for post in posts[:limit]:
        post_info = {
            "post_id": post.get("id"),
            "title": post.get("title"),
            "user_id": post.get("userId"),
        }
        processed_data.append(post_info)

    return processed_data


def save_to_file(data, filename):
    """
    Save processed data into JSON file safely.
    """
    try:
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
        print(f"✅ Data saved to {filename}")

    except IOError as error:
        print(f"❌ File write failed: {error}")


def main():
    print("Fetching data from API...\n")

    posts = fetch_api_data(API_URL)

    if not posts:
        print("⚠️ Exiting script due to API failure.")
        return

    processed_data = process_posts(posts)

    print("\n--- Processed Output ---")
    for item in processed_data:
        print(item)

    save_to_file(processed_data, OUTPUT_FILE)


if __name__ == "__main__":
    main()