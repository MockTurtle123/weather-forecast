import requests
API_KEY = 'f44235074891bca99ffd9fdcc749a3ac'


def get_data(place, days=None):
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={place}&units=metric&appid={API_KEY}'
    response = requests.get(url)
    data = response.json()
    filtered_data = data['list'][:days*8]
    return filtered_data


if __name__ == '__main__':
    print(get_data('Tokyo', days=3))