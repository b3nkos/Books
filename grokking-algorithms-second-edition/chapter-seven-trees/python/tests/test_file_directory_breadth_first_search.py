from file_directory_breadth_first_search import get_list_names


def test_get_list_names():
    final_list = [
        'a.txt',
        'b.rs',
        'folder_one_file_five.c',
        'folder_one_file_four.txt',
        'folder_one_file_one.tx',
        'folder_one_file_three.txt',
        'folder_one_file_two.cpp',
        'folder_two_file_one.txt',
        'folder_one_folder_one_file_one.js'
    ]

    assert get_list_names("pics") == final_list
