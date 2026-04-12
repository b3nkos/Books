from os import listdir
from os.path import isfile, join
from collections import deque


def get_list_names(start_dir) -> list[str]:
    search_queue = deque()
    search_queue.append(start_dir)
    final_files: list[str] = []

    while search_queue:
        dir = search_queue.popleft()
        for file in sorted(listdir(dir)):
            fullpath = join(dir, file)
            if isfile(fullpath):
                final_files.append(file)
            else:
                search_queue.append(fullpath)

    return final_files
