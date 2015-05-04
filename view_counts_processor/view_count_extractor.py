__author__ = 'extradikke'
from multiprocessing import Process, Queue
import os
import bz2
import urllib.parse
import time
from itertools import zip_longest


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


def uncompress_and_save(file_path, file_name):
    decompressor = bz2.BZ2Decompressor()
    counter = 0
    with open(file_path + file_name, "rb") as file_path:
        for data in iter(lambda: file_path.read(100 * 1024), b''):
            decompressor.decompress(data)

            counter += 1
            if counter > 10:
                break


def reject_non_articles(possible_link):
    temp = possible_link.lower()
    if temp.startswith((
            "file:", "category:", "wikipedia:", "wikt:", "image:", "media:", "s:", "n:", "commons:", "user:",
            "special:", "biblewiki:", "book:", "wiktionary:", "wikiquote:")):
        return False
    else:
        return True


def uncompress2(file_path, file_name, save_path2):
    reader = bz2.BZ2File(file_path + file_name, "rb")
    counter = 0
    file_name_no_ext, ext = file_name.split(".")
    # print(file_name_no_ext, ext)
    final_path = save_path2 + file_name_no_ext + ".txt"
    last_edit = None
    with open(final_path, encoding="utf-8", mode="w") as destination:
        for index, line in enumerate(reader):
            clear_line = line.decode("utf-8", "ignore")
            if index % 1000000 == 0 and last_edit != None:
                if counter > 1000000 and time.time() - last_edit > 5:
                    print(time.time() - last_edit)
                    break
                    # print(time.time() - last_edit)
            if clear_line.lower().startswith("en.z"):
                # print(urllib.parse.unquote(clear_line)[5::])
                last_edit = time.time()
                candidate_line = urllib.parse.unquote(clear_line)[5::]
                if reject_non_articles(candidate_line):
                    destination.write(candidate_line)
                counter += 1
                # if counter % 50000 == 0:
                # print("%d articles done" % counter)

    reader.close()


if __name__ == '__main__':
    save_path = "/media/extradikke/BigStorage/wiki_project/view_counts/"
    files_path_and_name = load_files()
    already_done = check_ready_files(save_path)
    average_time = 0
    total_time = 0
    finished_articles = 0
    finished_this_time = 0
    for filepath, filename in files_path_and_name:
        end_time = 0
        shorter_name, ext = filename.split(".")
        if shorter_name in already_done:
            finished_articles += 1
            print("already done %s, skipping..." % filename)
        else:
            start = time.time()
            print("Working on %s" % filename)
            uncompress2(filepath, filename, save_path)
            finished_this_time += 1
            finished_articles += 1
            end_time = time.time() - start
            total_time += end_time

            print("Day %s done in %.2f seconds. Average processing time %.2f" % (
                filename, end_time, total_time / finished_this_time))
            print("%d files to go" % (len(files_path_and_name) - finished_articles))




