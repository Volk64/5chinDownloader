import FileManager
import urllib.request as Requester

class FileFetcher ():

    """
    Class used to fetch images from the internet and feed them to the FileManager
    """

    # Data needed to download the images
    board =     ""
    img_url =   ""
    file_type = ""
    prepared_url = ""

    def __init__(self):
        pass

    def prepare_url(self):

        """
        Uses the fed data to create a valid link to a 4chan image
        :return: The url ready to be used
        """
        prepared_url = "http://i.4cdn.org/{0}/{1}{2}".format(self.board, self.img_url, self.file_type)
        return prepared_url

    def download_image(self, url, file_name):

        """
        Takes its given url and downloads the image from it.
        :param url: URL that contains the desired image
        :param file_name: Name of the file
        :return:
        """
        file = Requester.urlopen(url)
        FileManager.create_new_file(file, str(self.img_url)+self.file_type, "C:/Users/Volk/Pictures/5chin/")
        return None