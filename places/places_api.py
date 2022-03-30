import requests


class PlacesAPI:
    def __init__(self):
        self.key = 'AIzaSyDhdTgLhfAXcr37aiwnxe-vMX2hmAbOWpE'

    def get_place(self, text):
        url = f"https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={text}&inputtype=textquery&fields=formatted_address%2Cname%2Crating%2Copening_hours%2Cgeometry&key={self.key}"

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload).json()

        return response['candidates'][0]
