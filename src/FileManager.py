import os
import shutil
import datetime
import distutils.dir_util


def create_new_file(fetched_obj, file_name, directory="../downloaded_images/"):

    """
    Creates a new file
    :param fetched_obj: Content that is to be put inside the new file
    :param file_name: Name of the file to be created
    :param directory: Directory where the file has to be created.
    If no value is passed, it defaults to a directory inside the current directory
    :return: String for logging purposes
    """

    now = datetime.datetime.now()
    directory += str(now.year) + "-" + str(now.month) + "-" + str(now.day)
    """
    If the directory is the default one, we save the working directory,
    so that we can work with different directories.
    This is done so we don't create a new directory for each image downloaded.
    """
    if directory == "../downloaded_images/":
        or_dir = os.getcwd()
    else:
        dir = directory
    if not exists_directory(directory):
        dir = create_directory(directory)
    os.chdir(dir)
    new_file = open(file_name, "ab")
    shutil.copyfileobj(fetched_obj, new_file)
    if directory == "../downloaded_images/":
        os.chdir(or_dir)
    new_file.close()
    return "File successfully created"

def exists_directory(directory):
    return os.path.exists(directory)

def create_directory(directory_to_create):
        if directory_to_create == "../downloaded_images/":
            dir_make = os.getcwd() + directory_to_create.replace("../", "/")
        else:
            dir_make = directory_to_create
        distutils.dir_util.mkpath(dir_make)
        return dir_make