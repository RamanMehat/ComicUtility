# ReNameComics.py

""" This Python Script Will re-name Comic files """

# Import Statement
import os
import sys
import re
import shutil


def rename_comic_files(input_folder, output_folder):
    """
    Will Rename comics to the given format: Issue_Number Comic_Name.

    :param input_folder: Folder where original comics are.
    :param output_folder: Folder where the re-named comics will be saved.
    :return: None
    """

    abs_input_folder = os.path.abspath(input_folder)
    abs_output_folder = os.path.abspath(output_folder)
    copy_files_to_destination_folder(abs_input_folder, abs_output_folder)
    remove_unwanted_stings(abs_output_folder)
    rearrange_comic_issue_number(abs_output_folder)
    remove_temp_files(abs_output_folder)
    remove_files_from_input_folder(input_folder)


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
            shutil.copy(src_file, output_folder)


def remove_unwanted_stings(output_folder):
    """
    This function will remove any un-wanted strings from the comic name

    :param output_folder: Folder where the re-named comics will be saved.
    :return: None
    """

    for fileName in os.listdir(output_folder):
        src = os.path.join(output_folder, fileName)
        if "GetComics.INFO" in fileName:
            new_file_name = fileName.replace("GetComics.INFO", "").replace(' .pdf', '.pdf')
            dst = os.path.join(output_folder, new_file_name)
            os.rename(src, dst)

        elif "(Webrip) (The Last Kryptonian-DCP)" in fileName:
            new_file_name = fileName.replace("(Webrip) (The Last Kryptonian-DCP)", "").replace(' .pdf', '.pdf')
            dst = os.path.join(output_folder, new_file_name)
            os.rename(src, dst)

        elif "(The Last Kryptonian-DCP)" in fileName:
            new_file_name = fileName.replace("(The Last Kryptonian-DCP)", "").replace(' .pdf', '.pdf')
            dst = os.path.join(output_folder, new_file_name)
            os.rename(src, dst)

        elif "(BlackManta-Empire)" in fileName:
            new_file_name = fileName.replace("(BlackManta-Empire)", "").replace(' .pdf', '.pdf')
            dst = os.path.join(output_folder, new_file_name)
            os.rename(src, dst)

        elif "(Son of Ultron-Empire)" in fileName:
            new_file_name = fileName.replace("(Son of Ultron-Empire)", "").replace(' .pdf', '.pdf')
            dst = os.path.join(output_folder, new_file_name)
            os.rename(src, dst)

        elif "(Digital) (AnHeroGold-Empire)" in fileName:
            new_file_name = fileName.replace("(Digital) (AnHeroGold-Empire)", "").replace(' .pdf', '.pdf')
            dst = os.path.join(output_folder, new_file_name)
            os.rename(src, dst)

        elif "(Webrip)" in fileName:
            new_file_name = fileName.replace("(Webrip)", "").replace(' .pdf', '.pdf')
            dst = os.path.join(output_folder, new_file_name)
            os.rename(src, dst)

        elif "(Digital)" in fileName:
            new_file_name = fileName.replace("(Digital)", "").replace(' .pdf', '.pdf')
            dst = os.path.join(output_folder, new_file_name)
            os.rename(src, dst)

        elif "(digital)" in fileName:
            new_file_name = fileName.replace("(digital)", "").replace(' .pdf', '.pdf')
            dst = os.path.join(output_folder, new_file_name)
            os.rename(src, dst)

    for fileName in os.listdir(output_folder):
        src = os.path.join(output_folder, fileName)
        start = fileName.find('(')
        end = fileName.rfind(')')
        if start != -1:
            remove_string = fileName[start: end + 1]
            new_file_name = fileName.replace(remove_string, '').replace(' .pdf', '.pdf')
            dst = os.path.join(output_folder, new_file_name)
            os.rename(src, dst)

    for fileName in os.listdir(output_folder):
        src = os.path.join(output_folder, fileName)
        start = fileName.find('v')
        start2 = fileName.find('V')
        end = start + 2
        end2 = start2 + 2
        if start != -1 and int(start + 1):
            remove_string = fileName[start: end + 1]
            new_file_name = fileName.replace(remove_string, '').replace(' .pdf', '.pdf')
            dst = os.path.join(output_folder, new_file_name)
            os.rename(src, dst)

        elif start2 != -1 and int(start + 1):
            remove_string = fileName[start2: end2 + 1]
            new_file_name = fileName.replace(remove_string, '').replace(' .pdf', '.pdf')
            dst = os.path.join(output_folder, new_file_name)
            os.rename(src, dst)


def rearrange_comic_issue_number(output_folder):
    """
    This function will put the comic issue number at the front of the comic name

    :param output_folder: Folder where the re-named comics will be saved.
    :return: None
    """

    new_file_name = []
    for fileName in os.listdir(output_folder):
        src = os.path.join(output_folder, fileName)
        comic_issue = re.findall(r'\d+', fileName)
        if len(comic_issue) == 1:
            intermediate_file_name = fileName.replace(comic_issue[0], "").replace(' .pdf', '.pdf')
            if len(comic_issue[0]) >= 3:
                new_file_name = comic_issue[0] + ' ' + intermediate_file_name

            elif len(comic_issue[0]) == 2:
                new_file_name = '0' + comic_issue[0] + ' ' + intermediate_file_name

            elif len(comic_issue[0]) == 1:
                new_file_name = '00' + comic_issue[0] + ' ' + intermediate_file_name

            dst = os.path.join(output_folder, new_file_name)
            os.rename(src, dst)

        elif len(comic_issue) == 2:
            intermediate_file_name = fileName.replace(comic_issue[1], "").replace(' .pdf', '.pdf')
            if len(comic_issue[1]) >= 3:
                new_file_name = comic_issue[1] + ' ' + intermediate_file_name

            elif len(comic_issue[1]) == 2:
                new_file_name = '0' + comic_issue[1] + ' ' + intermediate_file_name

            elif len(comic_issue[1]) == 1:
                new_file_name = '00' + comic_issue[1] + ' ' + intermediate_file_name

            dst = os.path.join(output_folder, new_file_name)
            os.rename(src, dst)

        elif len(comic_issue) == 0:
            pass

        else:
            print("Lets Go buddy. To Many Numbers :p")


def remove_temp_files(output_folder):
    """
    Will remove temporary files ._, since they are not needed.

    :param output_folder: Folder where the re-named comics will be saved.
    :return: None
    """

    for fileName in os.listdir(output_folder):
        if "._" in fileName:
            sys.stdout.write("Removing " + fileName + '\n')
            abs_file_name = os.path.join(output_folder, fileName)
            os.remove(abs_file_name)


def remove_files_from_input_folder(input_folder):
    """
    Will remove all the files from the input folder.

    :param input_folder: Folder where original comics are.
    :return: None
    """

    for fileName in os.listdir(input_folder):
        sys.stdout.write("Removing " + fileName + '\n')
        abs_file_name = os.path.join(input_folder, fileName)
        os.remove(abs_file_name)
