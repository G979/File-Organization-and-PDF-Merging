import os
from typing import List
from fpdf import FPDF


def create_requested_subfolders(subfolder_names: List, files_path: str):
    """
    A function that creates subfolders with the requested names 00,01 and 02
    :param subfolder_names: A List with the requested subfolders name 00,01 and 02
    :param files_path: String Variable with a path to the pictures folder
    :return:
    """
    for prefix in subfolder_names:
        path = os.path.join(files_path, prefix)  # Find Destination Path
        try:
            os.mkdir(path)  # Create Sub Folders
        except OSError as error:
            print(error)


def move_files(subfolder_names: List, path_file: str):
    """
    A function that moves images to their respected folder based on their prefix name
    :param subfolder_names: A List with the requested subfolders name 00,01 and 02
    :param path_file: String Variable with a path to the pictures folder
    :return:
    """
    for img in os.listdir(path_file):
        old_file = path_file + os.sep + img
        try:
            if img.startswith('00') and len(img) > 2:
                destination = path_file + os.sep + subfolder_names[0] + os.sep + img  # Find Destination Path
                os.rename(old_file, destination)  # Move File
                print('Moved:', img)
            elif img.startswith('01') and len(img) > 2:
                destination = path_file + os.sep + subfolder_names[1] + os.sep + img
                os.rename(old_file, destination)
                print('Moved:', img)
            elif img.startswith('02') and len(img) > 2:
                destination = path_file + os.sep + subfolder_names[2] + os.sep + img
                os.rename(old_file, destination)
                print('Moved:', img)
            else:
                print('Wrong Image Prefix. Img did not move')
        except OSError as error:
            print(error)


def pdf_creator(subfolder_names: List, path_file: str):
    """
    A function that creates a pdf with sorted alphabetical order for each subfolders' images
    :param subfolder_names: A List with the requested subfolders name 00,01 and 02
    :param path_file: String Variable with a path to the pictures folder
    :return:
    """
    for i in range(3):
        try:
            pdf = FPDF()  # Create image object with fpdf
            pdf.add_page()  # Add Page with fpdf
            destination = path_file + os.sep + subfolder_names[i]  # Find Destination Path
            image_files = [i for i in os.listdir(destination) if
                           (i.endswith(".jpg") or i.endswith(".jpeg") or i.endswith(".png"))]  # Image File List Creation
            image_files.sort()  # Sort Images
            for img in image_files:
                img_path = destination + os.sep + img
                pdf.image(img_path)  # Create image object with fpdf
            if i == 0:
                pdf.output(f"{path_file}/pdf/00.pdf")  # Output File in pdf folder
                print("00.pdf Created")
            elif i == 1:
                pdf.output(f"{path_file}/pdf/01.pdf")
                print("01.pdf Created")
            elif i == 2:
                pdf.output(f"{path_file}/pdf/02.pdf")
                print("02.pdf Created")
            else:
                print("Not requested Image Prefix")
        except OSError as error:
            print(error)
