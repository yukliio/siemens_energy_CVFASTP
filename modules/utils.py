# utility helper functions for general use !

import os
import re

def rename_files_from_dir(folder_path): 
    """
    Purpose: renaming files for folder_path directory. 
    Returns: none. Just changes the file path to image number + item type.
    """
    item_type = os.path.basename(os.path.normpath(folder_path))
    print(item_type)
    for i, file_name in enumerate(os.listdir(folder_path)): 
        old_path = os.path.join(folder_path, file_name)
        print(old_path)
        new_path = os.path.join(folder_path, f"{i}_{item_type}.png")
        os.rename(old_path, new_path)
        print(f"Renamed: {old_path} --> {new_path}")