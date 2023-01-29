from project import ContentManager, RenameAuto, RenameManual, NewDirection, Move, Remove, Search, Create
import unittest
import os
import shutil


class TestRenameAuto(unittest.TestCase):
    def setUp(self):
        self.path_dir = os.getcwd()+'\Test'
        os.mkdir(self.path_dir)
        open(os.path.join(self.path_dir,'test0.txt'), 'x').close()
        open(os.path.join(self.path_dir,'test1.txt'), 'x').close()
        open(os.path.join(self.path_dir,'test2.txt'), 'x').close()
        open(os.path.join(self.path_dir,'test3.txt'), 'x').close()
        open(os.path.join(self.path_dir,'test4.txt'), 'x').close()

    def test_rename_auto(self):
        test = RenameAuto((os.getcwd()+'\Test'), 'txt', 'test_name')
        test.rename_auto()
        assert os.path.exists(os.path.join(self.path_dir,'test0.txt'))
        assert os.path.exists(os.path.join(self.path_dir,'test1.txt'))
        assert os.path.exists(os.path.join(self.path_dir,'test2.txt'))
        assert os.path.exists(os.path.join(self.path_dir,'test3.txt'))
        assert os.path.exists(os.path.join(self.path_dir,'test4.txt'))


    # def tearDown(self):
    #     shutil.rmtree(self.path_dir)


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