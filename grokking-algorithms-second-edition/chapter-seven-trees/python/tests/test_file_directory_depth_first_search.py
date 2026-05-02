from file_directory_depth_first_search import get_list_names


def test_get_list_names():
    final_list = [
        'folder_one_folder_one_file_one.js',
        'folder_one_file_five.c',
        'folder_one_file_four.txt',
        'folder_one_file_one.tx',
        'folder_one_file_three.txt',
        'folder_one_file_two.cpp',
        'folder_two_file_one.txt',
        'a.txt',
        'b.rs'
    ]

    assert get_list_names("pics") == final_list
