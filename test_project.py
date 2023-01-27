from project import ContentManager
import unittest
import os
import shutil


class TestRenameAuto(unittest.TestCase):
    def setUp(self):
        self.path_dir = os.path.join(os.getcwd(), 'Test')
        os.makedirs(self.path_dir, exist_ok=True)
        for n in range(5):
            open(f'{self.path_dir}/test_name{n}.txt', 'x')
    def test_rename_auto(self):
        test = ContentManager(os.path.join(os.getcwd(), 'Test'), "", "", "", 'test_name', "", 0)
        test.rename_auto()
        files = os.listdir(self.path_dir)
        for file in files:
            self.assertTrue(os.path.exists(os.path.join(f'{self.path_dir,file}.txt')))
    def tearDown(self):
        shutil.rmtree(self.path_dir)


# if __name__ == '__main__':
    # unittest

"""
    def test_rename_manual(self):
        pass

    def test_make_direction(self):
        pass

    def test_files_move(self):
        pass

    def test_delete_file(self):
        pass

    def test_searching_file(self):
        pass

    def test_create_text_file(self):
        pass

    def test_modify_text_file(self):
        pass
"""