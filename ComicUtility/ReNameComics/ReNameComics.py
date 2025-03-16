# ReNameComics.py

""" This Python Script Will re-name Comic files """

# Import Statement
from ComicUtility.ComicUtilities import FileHandlingUtilities

import os
import re
import shutil

REGEX = r"[A-Za-z!'., -]{0,}[0-9]{0,4}"
REGEX_NAME = r"[A-Za-z!'., -]{0,}"
REGEX_NBR = r"\D"
REGEX_OTHER = r"[_][0-9]{1,4}"


def rename_comic_files(input_folder, output_folder):
    """
    Will Rename comics to the given format: Issue_Number Comic_Name Vol_Number.

    :param input_folder: Folder where original comics are.
    :param output_folder: Folder where the re-named comics will be saved.
    :return: None
    """

    abs_input_folder = os.path.abspath(input_folder)
    abs_output_folder = os.path.abspath(output_folder)
    FileHandlingUtilities.copy_files_to_destination_folder(abs_input_folder, abs_output_folder)
    rename_comic(output_folder)
    if len(os.listdir(input_folder)) == len(os.listdir(output_folder)):
        FileHandlingUtilities.remove_files_from_input_folder(input_folder)
    else:
        print("Output files does not match input files, input directory was not cleaned")


def rename_comic(output_folder):
    for fileName in os.listdir(output_folder):
        if ("._" not in fileName) and ('.DS_Store' != fileName):
            src = os.path.join(output_folder, fileName)
            comic_name = re.match(REGEX, fileName)
            comic_title = re.match(REGEX_NAME, comic_name[0])
            comic_issue_nbr = re.sub(REGEX_NBR, "", comic_name[0]).replace("_", "") + " "
            # Regex if the normal name format from a downloaded comic is unusual
            # comic_issue_nbr = re.findall(REGEX_OTHER, fileName)[0].replace("_", "") + " "
            new_comic_file_name = comic_issue_nbr + comic_title[0].strip() + '.pdf'
            print('Re-naming Comic From: ' + fileName + ' To: ' + new_comic_file_name.strip())
            dst = os.path.join(output_folder, new_comic_file_name.strip())
            try:
                os.rename(src, dst)
            except OSError as e:
                print("Error: %s" % e)
                exit(2)
