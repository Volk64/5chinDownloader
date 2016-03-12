import requests
import FileFetcherClass


def obtain_json(given_url):

    """
    Takes an url and returns the containing JSON in it
    :param given_url: The url to fetch the desired JSON from
    :return: The obtained JSON
    """
    return requests.get(given_url + ".json").json()

url = "http://boards.4chan.org/v/thread/330572937"
fetched_json = obtain_json(url)
board = url.split("/")[3]
url_generator = FileFetcherClass.FileFetcher()
# We feed the FileFetcher with the values from the JSON
for post in fetched_json["posts"]:
    if "filename" in post:
        url_generator.board = board
        url_generator.img_url = post["tim"]
        url_generator.file_type = post["ext"]
        prepared_url = url_generator.prepare_url()
        url_generator.download_image(prepared_url, str(post["tim"]))
