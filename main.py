import requests


def get_film_info(film_id):
    url = f"https://swapi.dev/api/films/{film_id}/"

    response = requests.get(url)


    if response.status_code == 200:
        film_data = response.json()

        print("Фільм:", film_data['title'])

        print("Персонажі:")
        for character in film_data['characters']:
            character_info = requests.get(character).json()
            print(f"  {character_info['name']} з планети {requests.get(character_info['homeworld']).json()['name']}")

        print("Транспортні засоби:")
        for vehicle in film_data['vehicles']:
            print(f"  {requests.get(vehicle).json()['name']}")

        print("Космічні кораблі:")
        for starship in film_data['starships']:
            print(f"  {requests.get(starship).json()['name']}")

        print("Види істот:")
        for species in film_data['species']:
            print(f"  {requests.get(species).json()['name']}")
    else:
        print("Помилка при виконанні запиту до API")


film_id = input("Введіть ідентифікатор фільму: ")


get_film_info(film_id)
