import requests

# Amazon product URL (replace with your desired product link)
url = "https://www.amazon.com/dp/B08N5WRWNW"

# Headers to mimic a real browser
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
#     "Accept-Language": "en-US,en;q=0.9",
#     "Referer": "https://www.google.com/"
# }

session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.google.com/"
})

response = session.get(url)

if response.status_code == 200:
    print("Page fetched successfully!")
else:
    print(f"Failed to fetch page. Status code: {response.status_code}")

# Send a GET request
# response = requests.get(url, headers=headers)

# # Check if the request was successful
# if response.status_code == 200:
#     print("Request successful! ✅")
#     html_content = response.text  # The raw HTML of the page
#     print(html_content[:500])  # Print first 500 characters for preview
# else:
#     print(f"Request failed ❌. Status code: {response.status_code}")
