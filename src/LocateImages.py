import requests
import FileFetcherClass
import logging


def obtain_json(given_url):

    """
    Takes an url and returns the containing JSON in it
    :param given_url: The url to fetch the desired JSON from
    :return: The obtained JSON
    """
    return requests.get(given_url + ".json").json()

logging.basicConfig(level=logging.INFO)
url = input("Type a valid 4chan thread link: ")
logging.info("Fetching url " + url)
fetched_json = obtain_json(url)
logging.info("Url " + url + " successfully fetched")
board = url.split("/")[3]
url_generator = FileFetcherClass.FileFetcher()
# We feed the FileFetcher with the values from the JSON
for post in fetched_json["posts"]:
    if "filename" in post:
        url_generator.board = board
        url_generator.img_url = post["tim"]
        url_generator.file_type = post["ext"]
        prepared_url = url_generator.prepare_url()
        logging.info("Downloading " + str(url_generator.img_url) + url_generator.file_type)
        url_generator.download_image(prepared_url, str(post["tim"]))
        logging.info("Download of file " + str(url_generator.img_url) + url_generator.file_type + " finished successfully")
logging.info("Download of thread " + url + " finished successfully")
