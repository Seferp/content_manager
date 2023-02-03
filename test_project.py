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
        test1 = RenameAuto(self.path_dir, 'txt', 'test', 0)
        test2 = RenameAuto(self.path_dir, 'docx', 'test', 3)
        with self.assertRaises(FileExistsError):
            test1.rename_auto()
            test2.rename_auto()

    def test_rename_auto_special_characters(self):
        test1 = RenameAuto(self.path_dir, 'txt', 'New>', 0)
        test2 = RenameAuto(self.path_dir, 'txt', 'New:', 0)
        test3 = RenameAuto(self.path_dir, 'txt', 'New/', 0)
        test4 = RenameAuto(self.path_dir, 'txt', 'New*', 0)
        test5 = RenameAuto(self.path_dir, 'txt', 'New|', 0)
        with self.assertRaises(NameError):
            test1.rename_auto()
            test2.rename_auto()
            test3.rename_auto()
            test4.rename_auto()
            test5.rename_auto()

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
        test1 = RenameManual(self.path_dir, 'txt', 'test', 'test')
        test2 = RenameManual(self.path_dir, 'jpg', 'test', 'test')
        test3 = RenameManual(self.path_dir, 'docx', 'test', 'test')
        test4 = RenameManual(self.path_dir, 'css', 'test', 'test')
        with self.assertRaises(FileExistsError):
            test1.rename_manual()
            test2.rename_manual()
            test3.rename_manual()
            test4.rename_manual()

    def test_rename_manual_to_check_file_not_found_error(self):
        test1 = RenameManual(self.path_dir, 'txt', 'File', 'test')
        test2 = RenameManual(self.path_dir, 'jpg', 'File', 'test')
        test3 = RenameManual(self.path_dir, 'docx', 'File', 'test')
        test4 = RenameManual(self.path_dir, 'css', 'File', 'test')
        with self.assertRaises(FileNotFoundError):
            test1.rename_manual()
            test2.rename_manual()
            test3.rename_manual()
            test4.rename_manual()

    def test_rename_manual_special_characters(self):
        test1 = RenameManual(self.path_dir, 'txt', 'test', 'New>')
        test2 = RenameManual(self.path_dir, 'txt', 'test', 'New:')
        test3 = RenameManual(self.path_dir, 'txt', 'test', 'New/')
        test4 = RenameManual(self.path_dir, 'txt', 'test', 'New*')
        test5 = RenameManual(self.path_dir, 'txt', 'test', 'New|')
        with self.assertRaises(NameError):
            test1.rename_manual()
            test2.rename_manual()
            test3.rename_manual()
            test4.rename_manual()
            test5.rename_manual()

    def tearDown(self):
        shutil.rmtree(self.path_dir)


class TestNewDirection(unittest.TestCase):

    def setUp(self):
        self.path_dir = os.getcwd() + '\\' + 'Test'
        os.mkdir(self.path_dir)

    def test_make_only_one_new_direction(self):
        test1 = NewDirection(self.path_dir, 'Test_name', 1)
        test1.make_direction()
        assert os.path.exists(os.path.join(self.path_dir, 'Test_name'))

    def test_make_many_new_directions(self):
        test1 = NewDirection(self.path_dir, 'Test_name', 12)
        test1.make_direction()
        assert os.path.exists(os.path.join(self.path_dir, 'Test_name (1)'))
        assert os.path.exists(os.path.join(self.path_dir, 'Test_name (2)'))
        assert os.path.exists(os.path.join(self.path_dir, 'Test_name (3)'))
        assert os.path.exists(os.path.join(self.path_dir, 'Test_name (4)'))
        assert os.path.exists(os.path.join(self.path_dir, 'Test_name (5)'))
        assert os.path.exists(os.path.join(self.path_dir, 'Test_name (6)'))
        assert os.path.exists(os.path.join(self.path_dir, 'Test_name (7)'))
        assert os.path.exists(os.path.join(self.path_dir, 'Test_name (8)'))
        assert os.path.exists(os.path.join(self.path_dir, 'Test_name (9)'))
        assert os.path.exists(os.path.join(self.path_dir, 'Test_name (10)'))
        assert os.path.exists(os.path.join(self.path_dir, 'Test_name (11)'))
        assert os.path.exists(os.path.join(self.path_dir, 'Test_name (12)'))

    def test_make_direction_negative_counter_value(self):
        test1 = NewDirection(self.path_dir, 'Test_name', -1)
        with self.assertRaises(ValueError):
            test1.make_direction()

    def test_make_direction_special_characters(self):
        test1 = NewDirection(self.path_dir, 'Test_name>', 1)
        test2 = NewDirection(self.path_dir, 'Test_name:', 1)
        test3 = NewDirection(self.path_dir, 'Test_name/', 1)
        test4 = NewDirection(self.path_dir, 'Test_name*', 1)
        test5 = NewDirection(self.path_dir, 'Test_name|', 1)
        with self.assertRaises(NameError):
            test1.make_direction()
            test2.make_direction()
            test3.make_direction()
            test4.make_direction()
            test5.make_direction()

    def tearDown(self):
        shutil.rmtree(self.path_dir)


class TestMove(unittest.TestCase):

    def setUp(self):
        self.path_dir = os.getcwd() + '\\' + 'Test'
        self.new_path_dir = os.getcwd() + '\\' + 'Test2'
        os.mkdir(self.path_dir)
        os.mkdir(self.new_path_dir)
        open(os.path.join(self.path_dir, 'test.txt'), 'x').close()

    def test_files_move_to_new_location(self):
        test1 = Move(self.path_dir, 'txt', 'test', self.new_path_dir)
        test1.files_move()
        assert os.path.exists(os.path.join(self.new_path_dir, 'test.txt'))

    def test_files_move_to_new_location_where_exist_same_file(self):
        open(os.path.join(self.new_path_dir, 'test.txt'), 'x').close()
        test1 = Move(self.path_dir, 'txt', 'test', self.new_path_dir)
        with self.assertRaises(FileExistsError):
            test1.files_move()

    def tearDown(self):
        shutil.rmtree(self.path_dir)
        shutil.rmtree(self.new_path_dir)


class TestRemove(unittest.TestCase):

    def setUp(self):
        self.path_dir = os.getcwd() + '\\' + 'Test'
        os.mkdir(self.path_dir)
        open(os.path.join(self.path_dir, 'test.txt'), 'x').close()

    def test_delete_files_from_direction(self):
        test1 = Remove(self.path_dir, 'txt', 'test')
        test1.delete_file()
        assert not os.path.exists(os.path.join(self.path_dir, 'test.txt'))

    def test_delete_files_when_files_dont_exist(self):
        test1 = Remove(self.path_dir, 'txt', 'test2')
        with self.assertRaises(FileNotFoundError):
            test1.delete_file()

    def tearDown(self):
        shutil.rmtree(self.path_dir)


class TestSearch(unittest.TestCase):

    def setUp(self):
        self.path_dir = os.getcwd() + '\\' + 'Test'
        os.mkdir(self.path_dir)
        open(os.path.join(self.path_dir, 'test0.txt'), 'x').close()
        open(os.path.join(self.path_dir, 'test1.txt'), 'x').close()
        open(os.path.join(self.path_dir, 'test2.txt'), 'x').close()

    def test_searching_file_when_file_exist(self):
        test = Search(self.path_dir, 'test')
        test.searching_file()
        self.assertCountEqual(['test0.txt', 'test1.txt', 'test2.txt'], test.file_list)

    def test_searching_file_when_file_not_exist(self):
        test = Search(self.path_dir, 'File')
        with self.assertRaises(FileNotFoundError):
            test.searching_file()

    def tearDown(self):
        shutil.rmtree(self.path_dir)


class TestCreate(unittest.TestCase):

    def setUp(self):
        self.path_dir = os.getcwd() + '\\' + 'Test'
        os.mkdir(self.path_dir)
        open(os.path.join(self.path_dir, 'File1.txt'), 'x').close()
        open(os.path.join(self.path_dir, 'File2.docx'), 'x').close()

    def test_create_text_file(self):
        test1 = Create(self.path_dir, 'txt', 'test1')
        test2 = Create(self.path_dir, 'docx', 'test2')
        test1.create_text_file()
        test2.create_text_file()
        assert os.path.exists(os.path.join(self.path_dir, 'test1.txt'))
        assert os.path.exists(os.path.join(self.path_dir, 'test2.docx'))

    def test_create_text_file_when_file_exist(self):
        test1 = Create(self.path_dir, 'txt', 'File1')
        test2 = Create(self.path_dir, 'docx', 'File2')

        with self.assertRaises(FileExistsError):
            test1.create_text_file()
            test2.create_text_file()

    def test_create_text_file_when_file_type_is_wrong(self):
        test1 = Create(self.path_dir, 'jpg', 'test1')
        test2 = Create(self.path_dir, 'css', 'test2')
        test3 = Create(self.path_dir, 'csv', 'test3')
        test4 = Create(self.path_dir, 'py', 'test4')

        with self.assertRaises(TypeError):
            test1.create_text_file()
            test2.create_text_file()
            test3.create_text_file()
            test4.create_text_file()
    def tearDown(self):
        shutil.rmtree(self.path_dir)