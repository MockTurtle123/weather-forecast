import requests
API_KEY = 'f44235074891bca99ffd9fdcc749a3ac'


def get_data(place, days=None, kind=None):
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}'
    response = requests.get(url)
    data = response.json()
    filtered_data = data['list'][:days*8]
    if kind == 'Temperature':
        filtered_data = [i['main']['temp'] for i in filtered_data]
    elif kind == 'Sky':
        filtered_data = [i['weather'][0]['main'] for i in filtered_data]
    return filtered_data


if __name__ == '__main__':
    print(get_data('Tokyo', days=3, kind='Temperature'))