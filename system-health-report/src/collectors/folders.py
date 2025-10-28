import os
from humanfriendly import format_size

main_root = os.path.abspath(os.sep)

def get_folders(root_path: str):
    # retrieves all folders list from root_path
    all_folders = []
    folder_paths = []

    # loop through root_path, if entity is dir, append a new list with its name
    for obj in os.scandir(root_path):
        if obj.is_dir():
            all_folders.append(obj)
    # loop through list containing all folders in root_path, create a list of dicts containing folder name and folder path
    for fold in all_folders:
        folder_paths.append({"name": fold.name, "path": fold.path})
    # return list of dict containing all folders and paths in root_path
    return folder_paths

def get_folder_size(folder_path: str) -> int:
    """Return total size of all files inside the folder and its subfolders."""
    total_size = 0

    # calculate the total size of target folder (sum of all files)
    for root, dirs, files in os.walk(folder_path):
        for f in files:
            # if there is permission issues - skip the file
            try:
                fp = os.path.join(root, f)
                total_size += os.path.getsize(fp)
            except (PermissionError, FileNotFoundError):
                continue
    # return total size of the target folder
    return total_size

def get_top_folders(root_path=main_root, limit=10):
    # loop through folders list, calculate each folder's size
    single_folder_size = 0
    final_folders_list = []
    extracted_folders = get_folders(root_path)
    for path in extracted_folders:
        # create a new list of dicts, containing folder name, path and size in bytes
        single_folder_size = get_folder_size(path["path"])
        final_folders_list.append({"name": path["name"], "path": path["path"], "size": single_folder_size, "size_human": format_size(single_folder_size)})
    # sort the list by size desc
    final_folders_list.sort(key=lambda x: x["size"], reverse=True)
    # filter only first X folders
    top_10_folders = final_folders_list[:limit]
    return top_10_folders