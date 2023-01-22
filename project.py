from os import listdir, rename

class Content_Menager():
    def __init__(self, path, file_name, new_file_name, file_type):
        self.path = path
        self.file_name = file_name
        self.new_file_name = new_file_name
        self.file_type = file_type


    def rename_many_files(self):
        files = listdir(self.path)
        counter = int(input())   # User can choose from which number wants start numbering
        for file in files:
            if file.endswith(self.file_type):
                new_name = self.new_file_name + counter + self. file_type
                rename(f'{self.path}/{file}', f'{self.path}/{new_name}')
                counter += 1