import requests

url = "https://api.fbi.gov/wanted/v1/list"
response = requests.get(url)
data = response.json()

people_dict = data['items']

for l in people_dict:
    text = l['reward_text']
    if text is not None:
        number = int(text.split('$')[1].split(' ')[0].replace(',', ''))
        print(l['title'], '-', number)