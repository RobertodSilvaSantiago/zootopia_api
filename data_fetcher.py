import requests

API_KEY = "58UoKdXMtMUhA1fbmd8SOg==ODc6mumHWAnfBjeu"

def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns a list of animals, each animal is a dictionary:
    {
        'name': ...,
        'taxonomy': {
            ...
        },
        'locations': [
            ...
        ],
        'characteristics': {
            ...
        }
    }
    """
    url = f"https://api.api-ninjas.com/v1/animals?name={animal_name}"
    headers = {"X-Api-Key": API_KEY}
    response = requests.get(url, headers=headers)
    data = response.json()

    return data