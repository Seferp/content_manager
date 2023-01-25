from project import Content_Manager
from unittest import mock, TestCase


class Test(TestCase):
      def test_rename_auto(self):
        for n in range(5):
            f = open(f'Tests/file{n}.txt','x')
            input_name = ''
            input_new_name = 'New_name'
            input_folder = ''


        user_test = Content_Manager('Tests/', 'txt', "")

    # result = user_test.rename_auto()







 """   def test_rename_manual():
        pass

    def test_make_direction():
        pass

    def test_files_move():
        pass

    def test_delete_file():
        pass

    def test_searching_file():
        pass

    def test_create_text_file():
        pass

    def test_modify_text_file():
        pass
"""