import requests, json


class YoutubeAPI:
    def __init__(self, text):
        self.current_key = 1

        self.key = self.get_key()

        self.text = text

    def get_key(self):
        key = ''

        with open('youtube/keys.txt') as keys_file:
            for _ in range(self.current_key):
                key = keys_file.readline()

        return key

    def get_first_from_search(self):
        url = f'https://www.googleapis.com/youtube/v3/search?part=snippet&q={self.text}&key={self.key}&type=video'

        response = requests.get(url)

        res = response.json()

        return res['items'][0]['id']['videoId']
