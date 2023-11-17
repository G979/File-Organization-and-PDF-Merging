import os
from typing import List
from utils import create_requested_subfolders, move_files, pdf_creator


def assignment(subfolder_names: List, picture_path: str):
    # Create requested subfolders
    create_requested_subfolders(subfolder_names=subfolder_names, files_path=picture_path)

    # Iterate through files
    move_files(subfolder_names=subfolder_names, path_file=picture_path)

    # Create PDFs
    pdf_creator(subfolder_names=subfolder_names, path_file=picture_path)