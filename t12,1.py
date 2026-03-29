
import requests

url = "https://api.chucknorris.io/jokes/random"

try:
    data = requests.get(url)

    if data.status_code == 200:
        fetchedData = data.json()
        print("Joke: "+ fetchedData["value"])

    else:
        print("Error")
except requests.exceptions.RequestException:
    print("Error while fetching the data")