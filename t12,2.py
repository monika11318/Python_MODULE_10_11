
municipality = input("Enter the municipality name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={municipality}&appid=6b0bdf87e76f070a98a8d0ef1fe3f2a8"

try:
    data = requests.get(url)

    if data.status_code == 200:
        fetchedData = data.json()
        temp_kelvin = fetchedData["main"]["temp"]
        temp_celc = temp_kelvin-273.15
        print(f"The temperature of {municipality} is {round(temp_celc)}'C")

    else:
        print("Error")
except requests.exceptions.RequestException:
    print("Error while fetching the data")