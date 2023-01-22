from os import listdir, rename, mkdir, path, remove



class Content_Manager():
    def __init__(self, path, file_name, new_file_name, file_type):
        self.path = path
        self.file_name = file_name
        self.new_file_name = new_file_name
        self.file_type = file_type
        self.folder_name = str(input("Enter the folder name: "))

    def rename_auto(self):
        files = listdir(self.path)
        counter = int(input("Enter the starting numbering value: "))          # User can choose from which number wants start numbering

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
        quantity_folders = int(input("How many folders you need: "))
        result = "The folder has been created"
            # raise
        if quantity_folders == 1:
            path_folder = path.join(self.path, self.folder_name)
            mkdir(path_folder)
            print(result)
        else:
            for number in range(1, quantity_folders+1):
                path_folder = path.join(self.path, f'{self.folder_name} ({str(number)})')
                mkdir(path_folder)
            print(result)
    def files_move(self):
        pass

    def delete_file(self):
        file_to_remove = str(input("Enter the name of file which would you delete: "))
        remove_path = path.join(self.path,file_to_remove)
        remove(remove_path)

    def searching_file(self):
        pass

