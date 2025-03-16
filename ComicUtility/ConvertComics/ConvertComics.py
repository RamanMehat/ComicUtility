# ConvertComics.py

""" Will  Convert comics from CBZ/CBR format to PDF format using Apple scripts. """

# Import statement
import os
import subprocess


def convert_comics(input_folder):
    """
    Convert comics to PDF file format using Apple Scripts

    :param input_folder: Folder where original comics are.
    :return: None
    """

    here = os.path.abspath(os.path.dirname(__file__))
    open_parallels_apple_script = os.path.join(here, 'OpenParallelsMacOS.scpt')
    subprocess.call([open_parallels_apple_script], shell=True)




