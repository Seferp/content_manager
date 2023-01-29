from os import listdir, rename, mkdir, path, remove
from shutil import move
from re import search

# Parent class
class ContentManager():
    def __init__(self, path:str, file_type:str, file_name: str, new_file_name: str, folder_name: str):
        self.path = path
        self.file_type = f'.{file_type}'
        self.file_name = file_name
        self.new_file_name = new_file_name
        self.folder_name = folder_name


# Class to rename all files in direction if type is correct according to pattern: new_name + number.
class RenameAuto(ContentManager):
    def __init__(self, path: str, file_type:str, new_file_name: str):
        ContentManager.__init__(self, path, file_type,'', new_file_name,'')

    def rename_auto(self):
        files = listdir(self.path)
        counter = 0

        for file in files:
            if file.endswith(self.file_type):
                new_name = self.new_file_name + str(counter) + self.file_type

                path_file = path.join(self.path, file)
                path_new_name = path.join(self.path, new_name)

                if path.exists(path_new_name):
                    raise FileExistsError
                else:
                    rename(path_file,path_new_name)
                counter += 1

#Class to rename file. User can choose a specific name for file.
class RenameManual(ContentManager):
    def __init__(self, path: str, file_type: str, file_name: str, new_file_name: str):
        ContentManager.__init__(self, path, file_type, file_name, new_file_name, '')

    def rename_manual(self):
        new_name = self.new_file_name + self.file_type

        path_file = path.join(self.path, (self.file_name+self.file_type))
        path_new_name = path.join(self.path, new_name)

        if path.exists(path_new_name):
            raise FileExistsError
        else:
            rename(path_file, path_new_name)

# Class to create folders. User can choose numbers of folders to create and the name of them.
class NewDirection(ContentManager):
    def __init__(self, path:str, folder_name: str, quantity_folders: int):
        ContentManager.__init__(self, path, '', '', '', folder_name)
        self.quantity_folders = quantity_folders

    def make_direction(self):
        if self.quantity_folders < 1:
            raise ValueError
        elif self.quantity_folders == 1:
            path_folder = path.join(self.path, self.folder_name)
            mkdir(path_folder)
        else:
            for number in range(1, self.quantity_folders + 1):
                path_folder = path.join(self.path, f'{self.folder_name} ({str(number)})')
                mkdir(path_folder)


# Class to move files to new location. User can choose numbers of files to move to new localisation.
class Move(ContentManager):
    def __init__(self, path: str, file_type: str, file_name: str, new_path: str):
        ContentManager.__init__(self, path, file_type, file_name, '', '')

        self.new_path = new_path

    def files_move(self):
        file_move_path = path.join(self.path, self.file_name+self.file_type)
        file_move_new_path = path.join(self.new_path, self.file_name+self.file_type )
        if path.exists(file_move_new_path):
            raise FileExistsError
        else:
            move(file_move_path, file_move_new_path)


# Class to remove files.
class Remove(ContentManager):
    def __init__(self, path: str, file_type: str, file_name: str):
        ContentManager.__init__(self, path, file_type, file_name, '', '')

    def delete_file(self):
        remove_path = path.join(self.path,self.file_name+self.file_type)
        if path.exists(remove_path):
            remove(remove_path)
        else:
            raise FileNotFoundError

# Function to searching file in specific location chosen by user.
class Search(ContentManager):
    def __init__(self, path:str, file_name: str):
        ContentManager.__init__(self, path, '', file_name, '')

    def searching_file(self):
        files = listdir(self.path)
        files_list = []
        for file in files:
            if search(self.file_name, file):
                files_list.append(file)
        if len(files_list) == 0:
            print("No file found")
        else:
            print(*files_list, sep='\n')

# Class to create file with file type: ".docx" and ".txt".
class Create(ContentManager):
    def __init__(self, path: str, file_type: str, new_file_name: str):
        ContentManager.__init__(self, path, file_type, '', new_file_name, '')
        self.mode = 'x'
    def create_text_file(self):
        new_file_path = path.join(self.path, self.new_file_name+self.file_type)
        if path.exists(new_file_path):
            raise FileExistsError

        with open(new_file_path, self.mode) as f:
            f.write(self.new_file_name)
