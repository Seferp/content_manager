from os import listdir, rename, mkdir, path, remove
from shutil import move
from re import search


class Content_Manager():
    def __init__(self, path:str, file_type:str, mode:str, file_name = input("Enter the file name: "),
                 new_file_name = input("Enter the new name: "), folder_name = input("Enter the folder name: ")):
        self.path = path
        self.file_type = f'.{file_type}'
        self.mode = mode
        self.file_name = file_name
        self.new_file_name = new_file_name
        self.folder_name = folder_name



    # Function to rename a large amounts of files according to pattern: new_name + number.
    def rename_auto(self):
        files = listdir(self.path)
        counter = int(input("Enter the starting numbering value: "))

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

    # Function to rename file. User can choose a specific name fo each file.
    def rename_manual(self):
        files = listdir(self.path)

        for file in files:
            if file.endswith(self.file_type):
                new_name = self.new_file_name + self.file_type

                path_file = path.join(self.path, file)
                path_new_name = path.join(self.path, new_name)

                if path.exists(path_file):
                    raise FileExistsError
                else:
                    rename(path_file,path_new_name)

    # Function to create folders. User can choose numbers of folders to create and the name of them.
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


    # Function to move files to new location. User can choose numbers of files to move to new localisation.
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

    # Function to remove files.
    def delete_file(self):
        file_to_remove = self.file_name
        remove_path = path.join(self.path,file_to_remove+self.file_type)
        if path.exists(remove_path):
            remove(remove_path)
        else:
            raise FileNotFoundError

    # Function to searching file in specific location chosen by user.
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

    # Function to create file with file type: ".docx" and ".txt".
    def create_text_file(self):
        new_file_path = path.join(self.path, self.new_file_name+self.file_type)
        if path.exists(new_file_path):
            raise FileExistsError
        self.mode = 'x'
        with open(new_file_path, self.mode) as f:
            f.write(input("Enter the text: "))
            f.close()


    # Function to modify file with file type: ".docx" and ".txt".
    def modify_text_file(self):
        file_path = path.join(self.path, self.file_name+self.file_type)
        if not path.exists(file_path):
            raise FileNotFoundError
        decision = str(input('Do you wanna \'overwrite\' or \'add\' new content for file?'))
        if decision == 'overwrite':
            self.mode = 'w'
        elif decision == 'add':
            self.mode == "a"
        else:
            raise NameError
            print('Please choose \'overwrite\' or \'add\'')

        if self.file_type is ".docx" or self.file_type is '.txt':
            with open(file_path, self.mode) as f:
                f.write(input("Enter the text: "))
                f.close()


