# PrintCommandHelperInfo.py

""" Will Print Detailed Help Message for Each Mode """

# Import statement
import __init__
import sys


def print_header():
    """
    Function will print tool name and version from __init__.py
    :return: None
    """
    sys.stdout.write('\n' + "-------------------------------------------------" + '\n')
    sys.stdout.write("Tool: {!s}, Version: {!s}".format(__init__.name, __init__.version) + '\n')
    sys.stdout.write("-------------------------------------------------" + '\n' + '\n')


def print_mode_help_info_handler(ctx, param, help_msg):
    """
    Print help information for each mode and the entire tool handler

    :param ctx: Current Context
    :param param: click option parameter
    :param help_msg: Help Message Boolean
    :return: None
    """

    if not help_msg or ctx.resilient_parsing:
        return

    mode = ctx.params.get("mode")
    print_mode_help_info(mode)
    ctx.exit()


def print_mode_help_info(mode):
    """
    Print a detailed Help Message for The Specified Mode

    :param mode: The mode the Command Line Tool will generate file for, which is given by the user.
    :return: None
    """

    if mode == 'convert':
        sys.stdout.write("""
    How to use the 'convert' command:
    Convert comics from cbr/cbz to PDF format.
    -i, --input  [input file]:  path to the comic folder.                                                     [required]
    \n""")

    elif mode == 're-name':
        sys.stdout.write("""
    How to use the 're-name' command:
    Re-name comics to a given format Issue_Number Comic_Name Vol_Number.
    -i, --input  [input file]:  path to the comic folder.                                                    [required]
    -o, --output [output file]: path to output folder where to save the altered comic files.                  [required]
    \n""")

    elif mode == 'chk_lst_pg':
        sys.stdout.write("""
    How to use the 'chk_lst_pg' command:
    Check last page of comics and remove if its not part of the original comic.
    -i, --input  [input file]:  path to the comic folder.                                                     [required]
    -o, --output [output file]: path to output folder where to save the altered comic files.                  [required]
    \n""")

    else:
        sys.stdout.write("""
     How to Use the Tool:
    -i, --input  [input file]:  path to the comic files folder.
    -o, --output [output file]: path to output folder where to save the altered comic files.
    -m, --mode   required which can take the following values.
        convert:    Convert Comic from cbr/cbz to pdf..
        re-name:    Re-name comics to a given format Issue_Number Comic_Name Vol_Number.
        chk_lst_pg: Check comic book last page and remove if it is not a comic accurate page
    -h, --help:  Show this message and exit.
    \n""")
