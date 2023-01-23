from os import listdir, rename, mkdir, path, remove
import re


# Automatyczne doliczanie nr pliku


def rename(path, new_name, format):
    files = listdir(path)
    counter = 1
    for file in files:
        files_max_char = len(str(files[-1]))
        file_char = len(str(file))
        if file.endswith(format):
            # file_type = file.split('.')[-1]
            nname = new_name + ((len(str(len(files))) - len(str(counter))) * '0') + str(counter) + '.' + format
            rename(f'{path}/{file}', f'{path}/{nname}')
            counter += 1


files_dir = 'D:\_Python\Roboczy\\files_rename\\files_rename_first_idea'
# files_dir = 'D:\_Python\Roboczy\\files_rename\\files_rename_second_idea'

# files_dir = input("Enter the path: ")
# print(type(files_dir))
frm = 'docx'
# rename(files_dir, 'AA', frm)


# Ręczne podawanie nazwy
"""
def rename(path):
    files = os.listdir(path)
    for file in files:
        file_type = file.split('.')[-1]
        new_name = str(input())
        os.rename(path + '/' + file, path + '/' + new_name + '.' + file_type)
        print(f'Zmiana nazwy {file} na {new_name}.{file_type}')

files_dir = 'D:\_Python\Roboczy\\files_rename\\files rename second idea\\1 To .docx'
rename(files_dir)
"""

# Regex

"""
def rename(path, new_name, format):
    files = os.listdir(path)
    counter = 1
    for file in files:
        if re.match(format, file):
            file_type = file.split('.')[-1]
            nname = new_name + ((len(str(len(files))) - len(str(counter))) * '0') + str(counter)+ '.' + file_type
            os.rename(f'{path}/{file}', f'{path}/{nname}')
            counter += 1


files_dir = 'D:\_Python\Roboczy\\files_rename\\files rename firsr idea'
file_dir = os.path.abspath('Test0027')
frm = '.*.txt'
rename(files_dir, 'notatnik', frm)
"""


def make_direction(path):
    qt_folders = int(input("How many folders you need: "))
    # raise
    if qt_folders == 1:
        folder_name = str(input("Enter the folder name: "))
        path_folder = path.join(path, folder_name)
        mkdir(path_folder)
    else:
        # counter = 1
        folder_name = str(input("Enter the folder name: "))
        for number in range(1, qt_folders+1):
            path_folder = path.join(path, f'{folder_name} ({str(number)})')
            mkdir(path_folder)
            # counter += 1

x = "D:\_Python\Roboczy\\files_rename"
y = "Test3"

# make_direction(x)


def delete_file(pathe):
    file_to_remove = str(input("Enter the name of file which would you delete: "))
    # if path.exists("demofile.txt"):
    #     remove("demofile.txt")
    # else:
    #     print("The file does not exist")
    frm = str(input("Enter the file type: "))
    remove_path = path.join(pathe, file_to_remove+frm)
    print(remove_path)
    remove(remove_path)
"""A0105"""
x = "D:\_Python\Roboczy\\files_rename"
# delete_file(x)


def searching_file(path, file_name):
    files = listdir(path)
    phrase = f'{file_name}'
    files_list = []
    for file in files:
        if re.search(phrase, file):
            files_list.append(file)
    print(*files_list, sep= "\n")

files_dir = 'D:\_Python\Roboczy\\files_rename\\files_rename_first_idea'
x = "na"

searching_file(files_dir, x)

