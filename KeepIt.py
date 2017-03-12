import urllib.request
import shutil
import requests
import mimetypes
import re
import os

from components import *

e = 0 #Error counter.
i = 0 #Image counter.
extension = ""

def get_extension():
    response = requests.get(URL)
    content_type = response.headers['content-type']
    extension = mimetypes.guess_extension(content_type)
    return (extension)

def get_filesize():
    response = requests.get(URL)
    print(" :: [" + response.headers['content-length'] + " bytes]")

def download():
    response = requests.get(URL)
    content_type = response.headers['content-type']
    extension = mimetypes.guess_extension(content_type)
    download = urllib.request.urlopen(URL)
    output = open("downloads/" + title + extension, "wb")
    shutil.copyfileobj(download, output)

def wrapup():
    submission.unsave()
    print("[Complete.]")

for submission in reddit.redditor("skillfulcoding").saved(limit = 100):
    if os.path.exists("downloads/") == False:
        os.makedirs("downloads/")
    subreddit = submission.subreddit
    if subreddit == "EarthPorn" or subreddit == "waterporn" or subreddit == "SkyPorn" or subreddit == "CityPorn":

        title = submission.title
        URL = submission.url

        print("Now processing", title)
        print(" :: " + URL)

        extension = get_extension()

        if extension == None or extension == "":
            imgur = re.match(r".*imgur\.com\/(.*)", URL)
            flickr = re.match(r".*flickr\.com\/photos\/([^\/]+)\/([0-9^\/]+)\/", URL)

            if imgur:
                print(" :: [Imgur post.]")
                URL = "http://i.imgur.com/" + imgur.group(1) + ".jpg"

                extension = get_extension()
                print(" :: [" + extension + "]")
                # print("Using", modified_URL)

                get_filesize()
                download()
                wrapup()

            elif flickr:
                print(" :: [Flickr post.]")
                URL = "https://www.flickr.com/photos/" + flickr.group(1) + "/" + flickr.group(2) + "/sizes/o/"

                extension = get_extension()
                print(" :: [" + extension + "]")
                # print("Using", modified_URL)

                get_filesize()
                download()
                wrapup()

            else:
                e += 1
                print("[Could not determine filetype.]")
        else:
            print(" :: [Direct link.]")
            print(" :: [" + extension + "]")

            get_filesize()
            download()
            wrapup()

        i += 1
        print("-----")

print("[Processing complete.]", i, "files saved", "|", e, "errors") #After processing, print errors and images processed.

notification = str(i) + " files saved with " + str(e) + " errors."

def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))

notify("Reddit", notification)
