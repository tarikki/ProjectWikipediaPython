__author__ = 'extradikke'

import os

def load_files():
    files_inner = []
    path = "/media/extradikke/UbuntuData/wikipedia_data/viewCounts/"

    for (dirpath, dirnames, filenames) in os.walk(path):
        fillvalue = [dirpath + "/"] * len(filenames)
        if filenames is not None and dirpath is not "/":
            files_inner.extend(
                zip(fillvalue, [filename for filename in filenames if filename.startswith("pagecounts-")]))
    print(files_inner)
    print(len(set(files_inner)))
    return files_inner


def check_ready_files(save_path2):
    return [name.strip(".txt") for name in os.listdir(save_path2)]



if __name__ == '__main__':
    save_path = "/media/extradikke/BigStorage/wiki_project/view_counts/"
    files_path_and_name = load_files()
    already_done = check_ready_files(save_path)
    already_set = set(already_done)
    present_files = set()
    for index, (filepath, filename) in enumerate(files_path_and_name):
        no_ext, ext = filename.split(".")
        if no_ext in already_done:
            print(filename)
            present_files.add(filename)
    print(len(present_files), len(already_done), already_set-present_files)