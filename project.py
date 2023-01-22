from os import listdir, rename

class Content_Menager():
    def __init__(self, path, file_name, new_file_name, file_type):
        self.path = path
        self.file_name = file_name
        self.new_file_name = new_file_name
        self.file_type = file_type


    def rename_auto(self):
        files = listdir(self.path)
        counter = int(input("Enter the starting numbering value."))   # User can choose from which number wants start numbering
        for file in files:
            if file.endswith(self.file_type):
                new_name = self.new_file_name + counter + self.file_type
                rename(f'{self.path}/{file}', f'{self.path}/{new_name}')
                counter += 1
        print("Successful change of name")

    def rename_manual(self):
        files = listdir(self.path)
        for file in files:
            if file.endswith(self.file_type):
                new_name = str(input("Enter the new name")) + self.file_type   # User chooses a filename
                rename(f'{self.path}/{file}',f'{self.path}/{new_name}')
        print("Successful change of name")

