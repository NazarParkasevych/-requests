import requests


def get_film_info(film_id):
    # Визначаємо URL запиту до API SWAPI
    url = f"https://swapi.dev/api/films/{film_id}/"

    # Відправляємо запит до API
    response = requests.get(url)

    # Перевіряємо, чи успішний запит
    if response.status_code == 200:
        # Отримуємо дані про фільм з JSON відповіді
        film_data = response.json()

        # Виводимо назву фільму
        print("Фільм:", film_data['title'])

        # Виводимо персонажів
        print("Персонажі:")
        for character in film_data['characters']:
            character_info = requests.get(character).json()
            print(f"  {character_info['name']} з планети {requests.get(character_info['homeworld']).json()['name']}")

        # Виводимо транспортні засоби
        print("Транспортні засоби:")
        for vehicle in film_data['vehicles']:
            print(f"  {requests.get(vehicle).json()['name']}")

        # Виводимо космічні кораблі
        print("Космічні кораблі:")
        for starship in film_data['starships']:
            print(f"  {requests.get(starship).json()['name']}")

        # Виводимо види істот
        print("Види істот:")
        for species in film_data['species']:
            print(f"  {requests.get(species).json()['name']}")
    else:
        print("Помилка при виконанні запиту до API")


# Отримуємо ідентифікатор фільму від користувача
film_id = input("Введіть ідентифікатор фільму: ")

# Викликаємо функцію для отримання та виведення інформації про фільм
get_film_info(film_id)
