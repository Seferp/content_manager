from project import RenameAuto, RenameManual, NewDirection, Move, Remove, Search, Create
import unittest
import os
import shutil


class TestRenameAuto(unittest.TestCase):
    def setUp(self):
        self.path_dir = os.getcwd() + '\\' + 'Test'
        os.mkdir(self.path_dir)
        open(os.path.join(self.path_dir, 'test0.txt'), 'x').close()
        open(os.path.join(self.path_dir, 'test1.txt'), 'x').close()
        open(os.path.join(self.path_dir, 'test2.txt'), 'x').close()
        open(os.path.join(self.path_dir, 'test3.txt'), 'x').close()
        open(os.path.join(self.path_dir, 'test4.txt'), 'x').close()
        open(os.path.join(self.path_dir, 'test0.docx'), 'x').close()
        open(os.path.join(self.path_dir, 'test1.docx'), 'x').close()
        open(os.path.join(self.path_dir, 'test2.docx'), 'x').close()
        open(os.path.join(self.path_dir, 'test3.docx'), 'x').close()
        open(os.path.join(self.path_dir, 'test4.docx'), 'x').close()

    def test_rename_auto(self):
        test1 = RenameAuto(self.path_dir, 'txt', 'test_name', 0)
        test2 = RenameAuto(self.path_dir, 'docx', 'test_name', 3)
        test1.rename_auto()
        test2.rename_auto()
        assert os.path.exists(os.path.join(self.path_dir, 'test_name0.txt'))
        assert os.path.exists(os.path.join(self.path_dir, 'test_name1.txt'))
        assert os.path.exists(os.path.join(self.path_dir, 'test_name2.txt'))
        assert os.path.exists(os.path.join(self.path_dir, 'test_name3.txt'))
        assert os.path.exists(os.path.join(self.path_dir, 'test_name4.txt'))
        assert os.path.exists(os.path.join(self.path_dir, 'test_name3.docx'))
        assert os.path.exists(os.path.join(self.path_dir, 'test_name4.docx'))
        assert os.path.exists(os.path.join(self.path_dir, 'test_name5.docx'))
        assert os.path.exists(os.path.join(self.path_dir, 'test_name6.docx'))
        assert os.path.exists(os.path.join(self.path_dir, 'test_name7.docx'))

    def test_rename_auto_to_check_file_exist_error(self):
        test1 = RenameAuto(self.path_dir, 'txt', 'test_name', 0)
        test2 = RenameAuto(self.path_dir, 'docx', 'test_name', 3)
        test1.rename_auto()
        test2.rename_auto()
        assert FileExistsError
        assert FileExistsError
        assert FileExistsError
        assert FileExistsError
        assert FileExistsError
        assert FileExistsError
        assert FileExistsError
        assert FileExistsError
        assert FileExistsError
        assert FileExistsError

    def tearDown(self):
        shutil.rmtree(self.path_dir)


class TestRenameManual(unittest.TestCase):
    def setUp(self):
        self.path_dir = os.getcwd() + '\\' + 'Test'
        os.mkdir(self.path_dir)
        open(os.path.join(self.path_dir, 'test.txt'), 'x').close()
        open(os.path.join(self.path_dir, 'test.jpg'), 'x').close()
        open(os.path.join(self.path_dir, 'test.docx'), 'x').close()
        open(os.path.join(self.path_dir, 'test.css'), 'x').close()

    def test_rename_manual(self):
        test1 = RenameManual(self.path_dir, 'txt', 'test', 'test_name')
        test2 = RenameManual(self.path_dir, 'jpg', 'test', 'test_name')
        test3 = RenameManual(self.path_dir, 'docx', 'test', 'test_name')
        test4 = RenameManual(self.path_dir, 'css', 'test', 'test_name')
        test1.rename_manual()
        test2.rename_manual()
        test3.rename_manual()
        test4.rename_manual()
        assert os.path.exists(os.path.join(self.path_dir, 'test_name.txt'))
        assert os.path.exists(os.path.join(self.path_dir, 'test_name.jpg'))
        assert os.path.exists(os.path.join(self.path_dir, 'test_name.docx'))
        assert os.path.exists(os.path.join(self.path_dir, 'test_name.css'))

    def test_rename_manual_to_check_file_exist_error(self):
        test1 = RenameManual(self.path_dir, 'txt', 'test', 'test_name')
        test2 = RenameManual(self.path_dir, 'jpg', 'test', 'test_name')
        test3 = RenameManual(self.path_dir, 'docx', 'test', 'test_name')
        test4 = RenameManual(self.path_dir, 'css', 'test', 'test_name')
        test1.rename_manual()
        test2.rename_manual()
        test3.rename_manual()
        test4.rename_manual()
        assert FileExistsError
        assert FileExistsError
        assert FileExistsError
        assert FileExistsError

    def tearDown(self):
        shutil.rmtree(self.path_dir)


    """
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