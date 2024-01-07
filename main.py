import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}

response = requests.get(
    "https://www.zillow.com/homes/for_sale/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22isMapVisible%22%3Atrue%2C%22mapBounds%22%3A%7B%22west%22%3A-120.142035125%2C%22east%22%3A-73.560003875%2C%22south%22%3A26.969496911948504%2C%22north%22%3A48.27473098435842%7D%2C%22mapZoom%22%3A4%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D",
    headers=headers,
)


if response.status_code == 200:
    # Print the content of the response
    print(response.text)
else:
    # Print an error message if the request was not successful
    print(f"Error: {response.status_code}")
