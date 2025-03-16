# FileHandlingUtilities.py

""" This Python script will have different methods to handle file copying, moving, deletion, and creation """

# Import Statement
import os
import shutil
import sys


def copy_files_to_destination_folder(input_folder, output_folder):
    """
    Will Copy Comic Files from Input folder to Output folder.

    :param input_folder: Folder where original comics are.
    :param output_folder: Folder where the re-named comics will be saved.
    :return: None
    """

    for fileName in os.listdir(input_folder):
        src_file = os.path.join(input_folder, fileName)
        if os.path.isfile(src_file):
            try:
                shutil.copy(src_file, output_folder)
            except shutil.Error as e:
                print("Error: %s" % e)
                exit(2)


def remove_files_from_input_folder(input_folder):
    """
    Will remove all the files from the input folder.

    :param input_folder: Folder where original comics are.
    :return: None
    """

    for fileName in os.listdir(input_folder):
        sys.stdout.write("Removing " + fileName + '\n')
        abs_file_name = os.path.join(input_folder, fileName)
        try:
            os.remove(abs_file_name)
        except OSError as e:
            print("Error: %s" % e)
            exit(2)