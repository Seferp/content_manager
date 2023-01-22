import os
import re


# Automatyczne doliczanie nr pliku


def rename(path, new_name, format):
    files = os.listdir(path)
    counter = 1
    for file in files:
        if file.endswith(format):
            file_type = file.split('.')[-1]
            nname = new_name + ((len(str(len(files))) - len(str(counter))) * '0') + str(counter)+ '.' + file_type
            os.rename(f'{path}/{file}', f'{path}/{nname}')
            counter += 1


# files_dir = 'D:\_Python\Roboczy\\files_rename\\files_rename_first_idea'
# files_dir = 'D:\_Python\Roboczy\\files_rename\\files_rename_second_idea'

# files_dir = input("Enter the path: ")
# print(type(files_dir))
# frm = 'docx'
# rename(files_dir, 'TESTXYZ', frm)


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

