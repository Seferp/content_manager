from os import listdir, rename, mkdir, path, remove
from shutil import move
from re import search


class Content_Manager():
    def __init__(self, path:str, file_name:str, file_type:str, mode:str):
        self.path = path
        self.file_type = file_type
        self.mode = f'.{mode}'
        self.file_name = str(input("Enter the file name: "))
        self.new_file_name = str(input("Enter the new name: "))
        self.folder_name = str(input("Enter the folder name: "))

    def rename_auto(self):
        files = listdir(self.path)
        counter = int(input("Enter the starting numbering value: ")) # User can choose from which number wants start numbering

        for file in files:
            if file.endswith(self.file_type):
                new_name = self.new_file_name + counter + self.file_type
                path_file = path.join(self.path, file)
                path_new_name = path.join(self.path, new_name)
                if path.exists(path_file):
                    raise FileExistsError
                else:
                    rename(path_file,path_new_name)
                counter += 1


    def rename_manual(self):
        files = listdir(self.path)

        for file in files:
            if file.endswith(self.file_type):
                new_name = self.new_file_name + self.file_type   # User chooses a filename

                path_file = path.join(self.path, file)
                path_new_name = path.join(self.path, new_name)

                if path.exists(path_file):
                    raise FileExistsError
                else:
                    rename(path_file,path_new_name)

    def make_direction(self):
        quantity_folders = int(input("How many folders you need: "))
        if quantity_folders < 1:
            raise ValueError
        elif quantity_folders == 1:
            path_folder = path.join(self.path, self.folder_name)
            mkdir(path_folder)
        else:
            for number in range(1, quantity_folders+1):
                path_folder = path.join(self.path, f'{self.folder_name} ({str(number)})')
                mkdir(path_folder)


    def files_move(self):
        quantity_files = int(input("Enter the number of files which you would move to another localisation: "))
        new_location = str(input("Enter the new localisation which would you like to move your files: "))
        if quantity_files < 1:
            raise ValueError
        elif quantity_files == 1:
            file_move_path = path.join(self.path, self.file_name+self.file_type)
            file_move_new_path = path.join(new_location, self.file_name+self.file_type )
            move(file_move_path, file_move_new_path)
        else:
            files = listdir(self.path)
            for file in files:
                if file.endswith(self.file_type):
                    file_move_path = path.join(self.path, file + self.file_type)
                    file_move_new_path = path.join(new_location, file + self.file_type)
                    if path.exists(file_move_new_path):
                        raise FileExistsError
                    else:
                        move(file_move_path, file_move_new_path)

    def delete_file(self):
        file_to_remove = self.file_name
        remove_path = path.join(self.path,file_to_remove+self.file_type)
        if path.exists(remove_path):
            remove(remove_path)
        else:
            raise FileNotFoundError

    def searching_file(self):
        files = listdir(self.path)
        searching_phrase = f'{self.file_name}'
        files_list = []
        for file in files:
            if search(searching_phrase, file):
                files_list.append(file)
        if len(files_list) == 0:
            print("No file found")
        else:
            print(*files_list, sep='\n')

    def modify_text_file(self):
        pass