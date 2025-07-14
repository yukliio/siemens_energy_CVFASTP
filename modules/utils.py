# utility helper functions for general use !

import os
import re
import glob
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

def deleteDupes(folder_path): 
    png_files = glob.glob(os.path.join((folder_path), '*png'))
    for i in range(1, 6): 
        for file in png_files: 
            if file.endswith(f"({i}).png"): 
                os.remove(file)
                print("deleted")


def name_parts(parts_txt, desc_parts_txt): 
    parts = []
    descs = []
    file_name_new = []

    import re

    for part in parts_txt.decode("utf-8").splitlines(): 
        part_cleaned= re.sub(r"[\s,]+", "", part)
        parts.append(part_cleaned)
    for desc in desc_parts_txt.decode("utf-8").splitlines(): 
        desc_cleaned= re.sub(r"[\s,]+", "", desc)
        descs.append(desc_cleaned)

    for desc, part in zip(descs, parts):
        new_file = f"{part}_{desc}"
        file_name_new.append(new_file)
    
    return file_name_new
    
    

    




    
    

