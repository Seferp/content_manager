from os import listdir, rename, mkdir, path

class Content_Menager():
    def __init__(self, path, file_name, new_file_name, file_type):
        self.path = path
        self.file_name = file_name
        self.new_file_name = new_file_name
        self.file_type = file_type


    def rename_auto(self):
        files = listdir(self.path)
        counter = int(input("Enter the starting numbering value: "))   # User can choose from which number wants start numbering

        for file in files:
            if file.endswith(self.file_type):
                new_name = self.new_file_name + counter + self.file_type

                path_file = path.join(self.path, file)
                path_new_name = path.join(self.path, new_name)

                rename(path_file,path_new_name)
                counter += 1

        print("Successful change of names.")

    def rename_manual(self):
        files = listdir(self.path)

        for file in files:
            if file.endswith(self.file_type):
                new_name = str(input("Enter the new name: ")) + self.file_type   # User chooses a filename

                path_file = path.join(self.path, file)
                path_new_name = path.join(self.path, new_name)

                rename(path_file,path_new_name)

        print("Successful change of name.")


    def make_direction(self):
        qt_folders = int(input("How many folders you need: "))
            # raise
        if qt_folders == 1:
            folder_name = str(input("Enter the folder name: "))
            path_folder = path.join(self.path, folder_name)
            mkdir(path_folder)
            print("The folder has been created")
        else:
            folder_name = str(input("Enter the folder name: "))
            for number in range(1, qt_folders+1):
                path_folder = path.join(self.path, f'{folder_name} ({str(number)})')
                mkdir(path_folder)
            print("The folder's has been created")
    def files_move(self):
        pass

    def remove_files(self):
        pass

    def searching_file(self):
        pass

