# ComicUtility.py

"""  """

# Import statement
from ComicUtility.ConvertComics import ConvertComics
from ComicUtility.ReNameComics import ReNameComics
from ComicUtility.ComicUtilities import PrintCommandHelperInfo as Help

import click


@click.command()
@click.option("mode", "-m", "--mode", type=click.Choice(["convert", "re-name"]), multiple=False, required=True,
              is_eager=True)
@click.option("path_to_input", "-i", "--input", type=click.Path(exists=True), multiple=False, required=True)
@click.option("path_to_output", "-o", "--output", type=click.Path(exists=True), multiple=False, required=False)
@click.option("help_msg", '-h', '--help', callback=Help.print_mode_help_info_handler, is_flag=True, is_eager=True)
def comic_utility_main(mode, path_to_input, path_to_output, help_msg):
    """
    \b
         How to Use the Tool:
    -i, --input  [input file]:  path to the comic files folder.
    -o, --output [output file]: path to output folder where to save the altered comic files.
    -m, --mode   required which can take the following values.
        convert:  convert Comic from cbr/cbz to pdf..
        re-name:  re-name comics to a given format Issue_Number Comic_Name.
    """

    if mode == "convert":
        ConvertComics.convert_comics(path_to_input)

    elif mode == "re-name":
        ReNameComics.rename_comic_files(path_to_input, path_to_output)


def main():
    comic_utility_main()
