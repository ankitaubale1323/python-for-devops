import requests
import json


def fetch_api_data():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        print("✅ API call successful")
        return response.json()
    else:
        print("❌ Failed to fetch data")
        return None


def process_data(data):
    processed = []

    for item in data[:5]:  # Take first 5 posts only
        post_info = {
            "Post ID": item["id"],
            "Title": item["title"],
            "User ID": item["userId"]
        }
        processed.append(post_info)

    return processed


def save_to_json(data):
    with open("output.json", "w") as file:
        json.dump(data, file, indent=4)

    print("✅ Data saved to output.json")


def main():
    data = fetch_api_data()

    if data:
        processed_data = process_data(data)

        print("\n--- Processed Output ---")
        for post in processed_data:
            print(post)

        save_to_json(processed_data)


if __name__ == "__main__":
    main()