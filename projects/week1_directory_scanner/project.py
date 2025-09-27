# user is asked to enter a directory, default is the current working directory.
# A function to ask the user to enter details about directory
# A function to then ls the all the files and subdirectories
# Count files by type (e.g., `.txt`, `.py`, `.jpg`).
# A function to sort the files by size
# A function to sort by last modified
import os
import re
import subprocess


def user_input():
    print("Enter directory name or full path (defaults to current directory): ")
    keyed_input = input()
    # take the keyed input and call list_content_function else use default.
    if keyed_input != "":
        return keyed_input
    else:
        current_directory = subprocess.getoutput("pwd")
        print("current directory: " + current_directory)
        return current_directory


def list_directory_content(directory: str):
    print(directory)
    content = subprocess.getoutput(f"ls {directory}")
    list_content = content.split()

    return list_content


# inspect the content of the list and count the file types.
# store this in a dict object like {dir:7, .json:3, .txt:2....}
# Sample list ['journals', 'katas', 'project.txt', 'homework.txt', 'README.md']
def content_of_directory(content: list):
    # content = ["journals", "katas", "project.txt", "homework.txt", "README.md"]
    dict_of_directory = {}
    count_of_filetype = []
    for x in content:
        if "." not in x:
            dict_of_directory["dir"] = dict_of_directory.get("dir", 0) + 1
        elif "." in x:
            count_of_filetype = x.split(".")[-1]
            # print(count_of_filetype)
            file_type = "." + count_of_filetype
            dict_of_directory[file_type] = dict_of_directory.get(file_type, 0) + 1
    return dict_of_directory
    # print(dict_of_directory)
    # dict_of_directory[x] = content.count(x)
    #    if "." not in x:
    # 	    dict_of_directory["dir"] = content.count(x)
    #    elif "." in x:
    # 	count_of_file = x.split(".",1)
    #        print(count_of_filetype)
    # return dict_of_directory


def sort_by_size(directory: str):
    # return a dict in order of size of object i.e. {'Readme.md':15MB, 'file.pdf':100kb, 'myfiles.pdf':75kb}
    # add each awk line as a tuple in a list [(Readme.md':15MB),(Readme.md':15MB)....]
    # Then add to a dictionary? but how do you do that
    current_dir_dict = {}
    current_dir_list = (
        subprocess.getoutput(f"ls -lhS {directory} | awk '{{print $9,$5}}'")
        .strip()
        .splitlines()
    )
    for x in current_dir_list:
        file = str(x).split()
        file_name = file[0]
        file_size = file[1]
        current_dir_dict[file_name] = file_size

    # print(current_dir_dict)
    return current_dir_dict


def sort_by_modified(directory: str):
    # return a dict in order of size of object i.e. {'Readme.md':15MB, 'file.pdf':100kb, 'myfiles.pdf':75kb}
    # add each awk line as a tuple in a list [(Readme.md':15MB),(Readme.md':15MB)....]
    # Then add to a dictionary? but how do you do that
    current_dir_dict = {}
    current_dir_list = (
        subprocess.getoutput(
            f"ls -alhSTt {directory} | awk '{{print $10,$6" - "$7" - "$9" - "$8}}'"
        )
        .strip()
        .splitlines()
    )
    for x in current_dir_list:
        file = str(x).split()
        file_name = file[0]
        file_size = file[1]
        current_dir_dict[file_name] = file_size

    # print(current_dir_dict)
    return current_dir_dict


if __name__ == "__main__":
    # user_input()
    a = user_input()
    # b = list_directory_content(a)
    # print(b)
    # c = content_of_directory(b)
    # print(c)
    sort_by_size(a)
    sort_by_modified(a)
