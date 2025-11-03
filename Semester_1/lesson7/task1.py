import requests


def send_response(url: str):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()

    return None


def get_data(url):
    data = send_response(url)
    if data is None:
        print("Data not found")
        return

    return data


def get_person_characteristics(url):
    person_data = get_data(url)
    print(f"Имя: {person_data['name']}\n"
          f"Рост: {person_data['height']}\n"
          f"Масса: {person_data['mass']}\n"
          f"Цвет волос: {person_data['hair_color']}")


def get_person_country(url):
    person_data = get_data(url)
    nxt_data = send_response(person_data['homeworld'])

    print(f"{person_data['name']} родился на планете {nxt_data['name']}")


def get_pilots_cosmo(url):
    data = get_data(url)
    pilots = []
    key = "pilots"

    pilots_data = data["results"][0][key]
    for pilot_url in pilots_data:
        if pilot_url is not None:
            pilot_data = get_data(pilot_url)
            pilots.append(pilot_data['name'])

    print("Пилоты Millennium Falcon:")
    for pilot in pilots:
        print(f"- {pilot}")


if __name__ == "__main__":
    url1 = "https://swapi.dev/api/people/1/"
    get_person_characteristics(url1)
    get_person_country(url1)

    url2 = "https://swapi.dev/api/starships/?search=millennium%20falcon"
    get_pilots_cosmo(url2)
