__author__ = 'extradikke'
import os
import bz2



def uncompress_and_save(file, destination_directory):
    elements= file.split("/")
    file_name = elements[-1]
    print(file_name)
    file_name_no_ext, ext = file_name.split(".")
    print(file_name_no_ext)
    save_path = destination_directory+file_name_no_ext+".uncompressed"
    with open(save_path, "wb") as save_file, open(file, "rb") as file:
        decompressor = bz2.BZ2Decompressor()
        counter = 0
        for data in iter(lambda : file.read(100*1024), b''):
            print(decompressor.decompress(data))
            counter+=1
            if  counter > 10:
                break


if __name__ == '__main__':
    path ="/media/extradikke/UbuntuData/wikipedia_data/january"
    destination_d = "/media/extradikke/FastFiles/wikidata/1/"
    files = [file for file in os.listdir(path)]
    print(files)
    file = path+ "/" + files[0]
    print(file)
    uncompress_and_save(file, destination_d)
