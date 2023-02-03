from os import listdir, rename, mkdir, path, remove, getcwd
from shutil import move
from re import search
import re


# Parent class
class ContentManager:
    def __init__(self, file_path: str, file_type: str, file_name: str, new_file_name: str, folder_name: str):
        self.file_path = file_path
        self.file_type = f'.{file_type}'
        self.file_name = file_name
        self.new_file_name = new_file_name
        self.folder_name = folder_name


# Class to rename all files in direction if type is correct according to pattern: new_name + number.
class RenameAuto(ContentManager):
    def __init__(self, file_path: str, file_type: str, new_file_name: str, counter: int):
        ContentManager.__init__(self, file_path, file_type, '', new_file_name, '')
        self.counter = counter

    def rename_auto(self):
        files = listdir(self.file_path)
        if re.search(r"[\\,/,*,:,?,\",<,>,|]", self.new_file_name):
            raise NameError
        for file in files:
            if file.endswith(self.file_type):
                new_name = self.new_file_name + str(self.counter) + self.file_type

                path_file = path.join(self.file_path, file)
                path_new_name = path.join(self.file_path, new_name)

                if path.exists(path_new_name):
                    raise FileExistsError
                else:
                    rename(path_file, path_new_name)
                self.counter += 1


# Class to rename a specific file. User can choose a specific name for file.
class RenameManual(ContentManager):
    def __init__(self, file_path: str, file_type: str, file_name: str, new_file_name: str):
        ContentManager.__init__(self, file_path, file_type, file_name, new_file_name, '')

    def rename_manual(self):
        if re.search(r"[\\,/,*,:,?,\",<,>,|]", self.new_file_name):
            raise NameError
        new_name = self.new_file_name + self.file_type

        path_file = path.join(self.file_path, (self.file_name+self.file_type))
        path_new_name = path.join(self.file_path, new_name)
        if not path.exists(path_file):
            raise FileNotFoundError
        if path.exists(path_new_name):
            raise FileExistsError
        else:
            rename(path_file, path_new_name)


# Class to create folders. User can choose numbers of folders to create and the name of them.
class NewDirection(ContentManager):
    def __init__(self, file_path: str, folder_name: str, quantity_folders: int):
        ContentManager.__init__(self, file_path, '', '', '', folder_name)
        self.quantity_folders = quantity_folders

    def make_direction(self):
        if re.search(r"[\\,/,*,:,?,\",<,>,|]", self.folder_name):
            raise NameError
        if self.quantity_folders < 1:
            raise ValueError
        elif self.quantity_folders == 1:
            path_folder = path.join(self.file_path, self.folder_name)
            if path.exists(path_folder):
                raise FileExistsError
            mkdir(path_folder)
        else:
            for number in range(1, self.quantity_folders + 1):
                path_folder = path.join(self.file_path, f'{self.folder_name} ({str(number)})')
                mkdir(path_folder)


# Class to move files to new location. User can choose numbers of files to move to new localisation.
class Move(ContentManager):
    def __init__(self, file_path: str, file_type: str, file_name: str, new_path: str):
        ContentManager.__init__(self, file_path, file_type, file_name, '', '')
        self.new_path = new_path

    def files_move(self):
        file_move_path = path.join(self.file_path, self.file_name+self.file_type)
        file_move_new_path = path.join(self.new_path, self.file_name+self.file_type)
        if path.exists(file_move_new_path):
            raise FileExistsError
        else:
            move(file_move_path, file_move_new_path)


# Class to remove files.
class Remove(ContentManager):
    def __init__(self, file_path: str, file_type: str, file_name: str):
        ContentManager.__init__(self, file_path, file_type, file_name, '', '')

    def delete_file(self):
        remove_path = path.join(self.file_path, self.file_name+self.file_type)
        if path.exists(remove_path):
            remove(remove_path)
        else:
            raise FileNotFoundError


# Function to searching file in specific location chosen by user.
class Search(ContentManager):
    def __init__(self, file_path: str, file_name: str):
        ContentManager.__init__(self, file_path, '', file_name, '', '')
        self.file_list = []

    def searching_file(self):
        files = listdir(self.file_path)
        for file in files:
            if re.search(self.file_name, file):
                self.file_list.append(file)
        if len(self.file_list) == 0:
            raise FileNotFoundError
        else:
            print(*self.file_list, sep='\n')


# Class to create file with file type: ".docx" and ".txt".
class Create(ContentManager):
    def __init__(self, file_path: str, file_type: str, new_file_name: str):
        ContentManager.__init__(self, file_path, file_type, '', new_file_name, '')
        self.mode = 'x'

    def create_text_file(self):
        new_file_path = path.join(self.file_path, self.new_file_name+self.file_type)
        if not self.file_type != 'txt' and self.file_type != 'docx':
            raise TypeError
        if path.exists(new_file_path):
            raise FileExistsError
        with open(new_file_path, self.mode) as f:
            f.write(self.new_file_name)

