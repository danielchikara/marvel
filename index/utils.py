
import requests
import time
import hashlib
import json
from datetime import datetime, timedelta
from .models import *


def get_comic(first_item):
    now = datetime.now()
    public_key = "782bb1455fc216d51887c2d19db2b0f4"
    private_key = "8f7bdc752ba26921bc62c181e3e687799f71d2ae"
    timestamp = str(time.time())
    hash_value = hashlib.md5(
        f"{timestamp}{private_key}{public_key}".encode("utf-8")).hexdigest()
    params = {

        "apikey": public_key,
        "ts": timestamp,
        "hash": hash_value
    }
    if first_item:
        print("if items")
        time_update = now - timedelta(minutes=5)
        print("zaasasas", time_update)

        comic = Comic.objects.filter(date__gt=time_update)
        print("error", comic)
        if comic.count() > 0:
            print("if comic", comic)
            response = get_request(params)
            update_books(response)
    else:
        ("no item")
        response = get_request(params)
        create_books(response)
        return True

    return "no hay cambios por hacer"


def create_books(response):
    for comic_data in response:
        comic = Comic(id=comic_data["id"],
                      title=comic_data["title"],
                      thumbnail=comic_data["thumbnail"]["path"] + ".jpg",
                      series=comic_data["series"]["name"],
                      date = datetime.now())

        comic.save()
        for creator_data in comic_data['creators']["items"]:
            creator = Creators(
                comic=comic, name=creator_data["name"], role=creator_data["role"])
            creator.save()


def update_books(response):

    for comic_data in response:
        comic = Comic.objects.update_or_create(id=comic_data["id"],
                                               defaults={"title": comic_data["title"],
                                               "thumbnail": comic_data["thumbnail"]["path"] + ".jpg",
                                                         "series": comic_data["series"]["name"],
                                                         "date": datetime.now(), })

       
            


def get_request(params):
    response = requests.get(
        'http://gateway.marvel.com/v1/public/comics', params=params)
    if response.status_code == 200:
        response = json.loads(response.text)
        return response['data']['results']
    else:
        return response.status_code
