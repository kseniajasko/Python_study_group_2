import os
import os.path
import shutil
import json
import logging

logging.basicConfig(filename='app.log', filemode='w', format='%(asctime)s - %(message)s', level=logging.INFO, datefmt='%d-%b-%y %H:%M:%S')


def list_dir():
    print("All directories and files:", os.listdir())
    logging.info(f'Method list_dir')

def all_dir():

    for dir_path, dir_names, file_names in os.walk("."):

        for dir_name in dir_names:
            print("Directory:", os.path.join(dir_path, dir_name))

        for file_name in file_names:
            print("File:", os.path.join(dir_path, file_name))
    logging.info(f'Method all_dir')

def dir_structure(path):
    d = {'name': os.path.basename(path)}
    if os.path.isdir(path):
        d['type'] = "directory"
        child = [dir_structure(os.path.join(path, x)) for x in os.listdir(path)]
        if len(child) != 0:
            d['children'] = child
    else:
        d['type'] = "file"
    return d

def dir_structure_to_json(file_name):
    path_json = os.path.join(os.getcwd(), 'data', file_name)
    with open(path_json, 'w', encoding='utf-8') as f:
        json.dump(dir_structure('.'), f, ensure_ascii=False, indent=4)
    logging.info(f'Catalogues Dump to json {file_name}')

def new_folder(folder_name: str):
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
        logging.info(f'Create new folder {folder_name}')
    else:
        raise FileNotFoundError('Folder exist')


def rename_folder(folder_name, new_folder_name):
    if not os.path.isdir(folder_name):
        raise FileNotFoundError('No such folder')
    os.rename(folder_name, new_folder_name)
    logging.info(f'Folder {folder_name} renamed on {new_folder_name}')

def delete_folder(folder_name):
    if not os.path.isdir(folder_name):
        raise FileNotFoundError('No such folder')
    shutil.rmtree(folder_name)
    logging.info(f'Deleted folder {folder_name}')

def new_file(file_name):
    if not os.path.isfile(file_name):
        open(file_name, "w")
        logging.info(f'Created new file {file_name}')
    else:
        raise FileNotFoundError('File exist')

def rename_file(file_name, new_file_name):
    if not os.path.exists(file_name):
        raise FileNotFoundError('No such file')
    else:
        os.rename(file_name, new_file_name)
        logging.info(f'File {file_name} renamed on {new_file_name}')

def replace_file_path(file_name, new_path):
    if not os.path.exists(file_name):
        raise FileNotFoundError('No such file')

    os.replace(file_name, new_path)
    logging.info(f'File {file_name} replaced to {new_path}')

def remove_file(file_name):
    if not os.path.exists(file_name):
        raise FileNotFoundError('No such file')

    if not os.path.isfile(file_name):
        raise FileNotFoundError("It's not file")

    os.remove(file_name)
    logging.info(f'File {file_name} removed')

def file_size(file_name):
    print(os.stat(file_name).st_size)
    logging.info(f'File size {file_name} is given')




if __name__ == '__main__':

    new_folder('proba3')
    # new_folder('proba4')
    rename_folder('proba3', 'proba1')
    delete_folder('proba1')
    new_file("text.txt")
    rename_file("text.txt", "text1.txt" )
    # replace_file_path("text1.txt", "dir1/dir2/text1.txt")
    # print(remove_file("file_dir2.py"))
    file_size("console_manager.py")
    list_dir()
    print(dir_structure('.'))
    all_dir()
    dir_structure_to_json('folder_structure.json')
