import urllib.request, shutil, requests, mimetypes, re, os, os.path, json, platform
from components import *

e = 0 #Resets error counter.
i = 0 #Resets image counter.

def get_extension():
    #Identifies filetype using open "requests.get" statement below.
    content_type = response.headers['content-type']
    #Identifies extension from filetype.
    extension = mimetypes.guess_extension(content_type)
    return (extension)

def get_filesize():
    #Identifies filesize in bytes using open "requests.get" statement below.
    print(" :: [" + response.headers['content-length'] + " bytes]")

def download():
    content_type = response.headers['content-type']
    extension = mimetypes.guess_extension(content_type)
    #Writes image to new file using open "requests.get" statement below.
    with open("downloads/" + title + extension, "wb") as f:
        f.write(response.content)

def wrapup():
    #Unsaves link on Reddit.
    submission.unsave()
    print("[Complete.]")

#Uses user data and PRAW connection from components.py to collect up to 100 saved links from Reddit.
for submission in reddit.redditor(username).saved(limit = 100):
    #Creates a new directory for downloaded images if it doesn't already exist.
    if os.path.exists("downloads/") == False:
        os.makedirs("downloads/")

    #Checks subreddit against list in components.py to determine whether or not the link should be downloaded.
    subreddit = submission.subreddit
    if subreddit in subreddit_array:
        #Formats link title by trimming to acceptable length and replacing certain special characters.
        preformatted = submission.title
        truncated = (preformatted[:230] + "...") if len(preformatted) > 230 else preformatted
        title = truncated.replace("/", "").replace("[", "(").replace("]", ")")

        #Opens a connection to the link.
        URL = submission.url
        response = requests.get(URL)

        print("[Now processing \"" + title + "\"]")
        print(" :: [" + URL + "]")
        print(" :: [in " + str(subreddit) + "]")

        extension = get_extension()

        #If no extension is identified, the link provided is not a direct image link.
        if extension == None or extension == "":
            #Attempts to match link URL against known file hosts Imgur and Flickr using regular expressions.
            imgur = re.match(r".*imgur\.com\/(.*)", URL)
            flickr = re.match(r".*flickr\.com\/photos\/([^\/]+)\/([0-9^\/]+)\/", URL)

            if imgur:
                print(" :: [Imgur post.]")

                #Assembles new URL using the Imgur-assigned photo ID from original URL.
                URL = "http://i.imgur.com/" + imgur.group(1) + ".jpg"

                #Opens a connection to the new link.
                response = requests.get(URL)

                extension = get_extension()
                print(" :: [" + extension + "]")

                get_filesize()
                download()
                wrapup()

            elif flickr:
                print(" :: [Flickr post.]")

                #Sends a query to the Flickr API using the Flickr-assigned photo ID from original URL.
                URL = "https://api.flickr.com/services/rest/?method=flickr.photos.getSizes&api_key=3f575a3181a65ac624e9896b2749c1e6&photo_id=" + flickr.group(2) + "&format=json&nojsoncallback=1"

                #Imports the result of the query as a JSON string.
                result = requests.get(URL).text
                parsed = json.loads(result)

                #Identifies URL for the "Original" size of the photo.
                for size in parsed["sizes"]["size"]:
                    dimension = size.get("source")
                    if size.get("label") == "Original":
                        URL = size.get("source")
                        status = "confirmed"

                #Checks if URL for the "Original" size of the photo has been identified.
                if status == "confirmed":
                    #Opens a connection to the new URL.
                    response = requests.get(URL)

                    extension = get_extension()
                    print(" :: [" + extension + "]")

                    get_filesize()
                    download()
                    wrapup()
                else:
                    print("[Could not identify a source URL for the original resolution.]")
                    e += 1

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

#Returns processing data to the user.
print("[Processing complete.]", i, "files saved", "|", e, "errors")

#If the user is on a Mac, script sends an integrated MacOS notification through AppleScript with the the processing data.
if platform.system() == "Darwin":
    notification = str(i) + " files saved with " + str(e) + " errors."
    def notify(title, text):
        os.system("""osascript -e 'display notification "{}" with title "{}"'""".format(text, title))
    notify("Reddit, KeepIt", notification)
