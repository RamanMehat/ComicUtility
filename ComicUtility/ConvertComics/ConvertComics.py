import os
import zipfile
import subprocess
from PIL import Image
import fitz  # PyMuPDF
import tempfile
import re

def extract_archive(file_path, extract_to):
    """
    Extracts the contents of a CBZ or CBR file to the specified folder.
    """
    ext = os.path.splitext(file_path)[-1].lower()
    
    if ext == '.cbz':
        # CBZ is a ZIP archive
        with zipfile.ZipFile(file_path, 'r') as archive:
            archive.extractall(extract_to)
            # Print extracted files for debugging
            extracted_files = os.listdir(extract_to)
            print(f"Extracted files from {file_path}: {extracted_files}")
    elif ext == '.cbr':
        # CBR is a RAR archive, use 'unar' command
        try:
            subprocess.run(['unar', '-o', extract_to, file_path], check=True)
            extracted_files = os.listdir(extract_to)
            print(f"Extracted files from {file_path}: {extracted_files}")
        except subprocess.CalledProcessError as e:
            print(f"Error extracting {file_path}: {e}")
    else:
        raise ValueError(f"Unsupported file type: {ext}. Only CBZ and CBR files are supported.")

def natural_key(filename):
    return [int(text) if text.isdigit() else text.lower()
            for text in re.split(r'(\d+)', filename)]

def get_images_from_folder(folder):
    images = []
    for root, _, files in os.walk(folder):
        for file_name in sorted(files, key=natural_key):
            if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp')):
                img_path = os.path.join(root, file_name)
                print(f"Processing image: {img_path}")
                with Image.open(img_path) as img:
                    if img.mode != 'RGB':
                        img = img.convert('RGB')
                    images.append(img.copy())
    return images    
    
def images_to_pdf(image_folder, output_pdf):
    """
    Converts a folder of images into a single PDF.
    """
    images = get_images_from_folder(image_folder)
    
    if images:
        print(f"Saving PDF to {output_pdf}")
        images[0].save(output_pdf, save_all=True, append_images=images[1:])
    else:
        print("No images found for conversion.")

def convert_comic_to_pdf(comic_file, output_pdf):
    """
    Main function to convert CBZ or CBR comic file to PDF.
    """
    # Create a temporary directory to extract images
    with tempfile.TemporaryDirectory() as temp_dir:
        print(f"Extracting {comic_file} to {temp_dir}...")
        extract_archive(comic_file, temp_dir)
        
        print(f"Converting {comic_file} to PDF...")
        images_to_pdf(temp_dir, output_pdf)

def batch_convert_comics(input_directory, output_directory):
    """
    Convert all CBZ and CBR files in the input_directory and save PDFs in the output_directory.
    """
    # Ensure the output directory exists
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Process all .cbz and .cbr files in the input directory
    for file_name in os.listdir(input_directory):
        if file_name.lower().endswith(('.cbz', '.cbr')) and not file_name.lower().startswith('.'):
            comic_file = os.path.join(input_directory, file_name)
            output_pdf = os.path.join(output_directory, os.path.splitext(file_name)[0] + '.pdf')
            print(f"Processing {comic_file} and saving to {output_pdf}")
            convert_comic_to_pdf(comic_file, output_pdf)
    print(f"All CBZ and CBR files in {input_directory} have been converted and saved to {output_directory}.")
