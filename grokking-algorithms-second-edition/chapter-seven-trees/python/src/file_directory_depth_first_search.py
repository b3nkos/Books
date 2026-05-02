from os import listdir
from os.path import isfile, join

final_files: list[str] = []

def get_list_names(start_dir) -> list[str]:
    for file in sorted(listdir(start_dir)):
        full_path = join(start_dir, file)
        if isfile(full_path):
            final_files.append(file)
        else:
            get_list_names(full_path)

    return final_files
