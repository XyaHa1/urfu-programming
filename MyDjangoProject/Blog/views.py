import requests
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def send_response(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data

    return None


def update_data(data):
    films = data.get('films', [])
    vehicles = data.get('vehicles', [])
    starships = data.get('starships', [])
    new_films = []
    for film in films:
        film_response = send_response(film)
        new_films.append(film_response['title'])

    new_vehicles = []
    for vehicle in vehicles:
        vehicle_response = send_response(vehicle)
        new_vehicles.append(vehicle_response['name'])

    new_starships = []
    for starship in starships:
        starship_response = send_response(starship)
        new_starships.append(starship_response['name'])

    data['films'] = new_films
    data['vehicles'] = new_vehicles
    data['starships'] = new_starships

    return data


def get_luke_info(request):
    data = send_response('https://swapi.dev/api/people/1/')
    if data:
        updated_data = update_data(data)
        return render(request, 'people/person.html', updated_data)

    return HttpResponse("Failed to fetch data")
