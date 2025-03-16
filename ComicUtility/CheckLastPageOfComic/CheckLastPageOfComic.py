# CheckLastPageOfComic.py

"""
This Python Script Will Check Comic Book last page and determine if it is not an original page of the comic.
If not an original page it will be removed.
Else no action required
 """

# Import Statement
from PIL import Image, ImageChops
from ComicUtility.ComicUtilities import FileHandlingUtilities

import os
import shutil
import fitz


# Constants
COMIC_UTILITY_ROOT_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
REF_PAGE_TO_REMOVE_DIR = os.path.join(os.path.dirname(COMIC_UTILITY_ROOT_DIR), 'References')


def chck_comic_lst_page(input_folder, output_folder):
    """
    Will RCheck comic last page and remove if not part of the original comic.

    :param input_folder: Folder where original comics are.
    :param output_folder: Folder where the re-named comics will be saved.
    :return: None
    """

    abs_input_folder = os.path.abspath(input_folder)
    abs_output_folder = os.path.abspath(output_folder)

    tmp_dir = os.path.abspath(os.path.join(abs_input_folder, 'temp'))
    if os.path.exists(tmp_dir):
        shutil.rmtree(tmp_dir)

    os.mkdir(tmp_dir)
    for comic_file in os.listdir(abs_input_folder):
        if (os.path.splitext(comic_file)[1] == '.pdf') and ("._" not in comic_file) and ('.DS_Store' != comic_file):
            print('Processing ' + comic_file)
            abs_comic_file_path = os.path.join(abs_input_folder, comic_file)
            comic_book_doc = fitz.open(abs_comic_file_path)
            page = comic_book_doc.load_page(-1)
            lst_pg_comic = os.path.join(tmp_dir, os.path.splitext(comic_file)[0] + '.png')
            page.get_pixmap().save(lst_pg_comic)
            comic_book_doc.close()
            images_are_same = False
            for png_file in os.listdir(REF_PAGE_TO_REMOVE_DIR):
                if os.path.splitext(png_file)[1] == '.png':
                    abs_png_file_path = os.path.join(REF_PAGE_TO_REMOVE_DIR, png_file)
                    percentage_diff, images_are_same, tolerance = compare_images(Image.open(lst_pg_comic),
                                                                                 Image.open(abs_png_file_path),
                                                                                 0.002)
                    # Remove non-comic page and save new file in Output directory
                    if images_are_same:
                        print('Updating and Copying ' + comic_file)
                        comic_book_doc = fitz.open(abs_comic_file_path)
                        comic_book_doc.delete_page(-1)
                        comic_book_doc.save(os.path.join(abs_output_folder, comic_file))
                        break

            # Copy over Comic files, which have no extra pages
            if not images_are_same:
                print('Copying ' + comic_file)
                shutil.copy(abs_comic_file_path, os.path.join(abs_output_folder, comic_file))

    # Remove Temp Directory
    if os.path.exists(tmp_dir):
        shutil.rmtree(tmp_dir)

    if len(os.listdir(input_folder)) == len(os.listdir(output_folder)):
        FileHandlingUtilities.remove_files_from_input_folder(input_folder)
    else:
        print("Output files does not match input files, input directory was not cleaned")


def compare_images(lst_pg_comic_pmg, img_cmp, tolerance):
    """
    Compare two images.

    If tolerance is defined the outcome will compare with the accepted tolerance.
    The tolerance is a percentage difference calculated using

    https://rosettacode.org/wiki/Percentage_difference_between_images#Python
    ref: https://rowannicholls.github.io/python/image_analysis/comparing_two_images.html

    :param lst_pg_comic_pmg: Last page of the comic as a png.
    :param img_cmp: Image to be compared to
    :param tolerance: Tolerance allowed for the two image can differ
    :return: percentage_diff, images_are_same, tolerance
    """

    # Remove alpha layer if it exists
    if lst_pg_comic_pmg.getbands() == ('R', 'G', 'B', 'A'):
        lst_pg_comic_pmg = lst_pg_comic_pmg.convert('RGB')

    if img_cmp.getbands() == ('R', 'G', 'B', 'A'):
        img_cmp = img_cmp.convert('RGB')

    if lst_pg_comic_pmg.getbands() == ('L', 'A'):
        lst_pg_comic_pmg = lst_pg_comic_pmg.convert('L')

    if img_cmp.getbands() == ('L', 'A'):
        img_cmp = img_cmp.convert('L')

    # Check that the images can be compared
    if lst_pg_comic_pmg.mode != img_cmp.mode:
        raise Exception(f'Different kinds of images: {lst_pg_comic_pmg.mode} != {img_cmp.mode}')

    if lst_pg_comic_pmg.size != img_cmp.size:
        # print("Images are of different sizes, skip comparison")
        return 100, False, tolerance

    # Pixel-by-pixel comparison
    pairs = zip(lst_pg_comic_pmg.getdata(), img_cmp.getdata())
    # If the image is greyscale
    if len(lst_pg_comic_pmg.getbands()) == 1:
        # Total difference
        diff = sum(abs(pixel1 - pixel2) for pixel1, pixel2 in pairs)

    # If the image is RGB
    else:
        # Total difference
        diff = sum(abs(c1 - c2) for p1, p2 in pairs for c1, c2 in zip(p1, p2))

    # Total number of colour components
    total_nbr_clr = lst_pg_comic_pmg.size[0] * lst_pg_comic_pmg.size[1] * len(lst_pg_comic_pmg.getbands())
    # Calculate the percentage difference
    percentage_diff = diff / 255 / total_nbr_clr * 100
    # Assess if the difference falls within the tolerance
    if percentage_diff <= tolerance:
        images_are_same = True

    else:
        images_are_same = False

    return percentage_diff, images_are_same, tolerance
