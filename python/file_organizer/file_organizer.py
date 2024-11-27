from pathlib import Path
from shutil import move
import os

def organize_by_extension(to_sort, destination_path):
    global extension_path_dict
    extension_path_dict = {"":"no_ext_files"}
    os.makedirs("no_ext_files", exist_ok=True)

    to_sort = Path(to_sort)

    os.makedirs(destination_path, exist_ok=True)

    for item in to_sort.rglob("*"):
        try:
            extension = item.suffix
            if not extension in extension_path_dict:   
                extension_path_dict.update({extension: f"{extension[1:]}_files"})
                os.makedirs(f"{extension[1:]}_files", exist_ok=True)
                print(f"{extension[1:]}_files directory created")

            if os.path.exists(f"{extension[1:]}_files/{item.name}"):
                os.remove(f"{extension[1:]}_files/{item.name}")

            move(item, extension_path_dict[extension])
            #log in logger move made
            print(f"{item} moved to {extension_path_dict[extension]}")

            
        except PermissionError:
            print(f"Permission denied for file {item}")        