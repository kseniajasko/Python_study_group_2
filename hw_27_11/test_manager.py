import unittest
from console_manager import *

class FileManagerTest(unittest.TestCase):

    def test_create_delete_folder(self):
        folder_name = 'test_new_folder'
        new_folder(folder_name)
        self.assertTrue(os.path.isdir(folder_name))
        delete_folder(folder_name)

    def test_rename_folder(self):
        folder_name = 'new_folder_name'
        new_folder(folder_name)
        new_folder_name = 'rename_folder_name'
        rename_folder(folder_name, new_folder_name)
        self.assertTrue(os.path.isdir(new_folder_name))
        delete_folder(new_folder_name)

    def test_create_delete_file(self):
        file_name = 'test_new_file'
        new_file(file_name)
        self.assertTrue(os.path.isfile(file_name))
        delete_file(file_name)

    def test_rename_file(self):
        file_name = 'new_file_name'
        new_file(file_name)
        new_file_name = 'rename_folder_name'
        rename_file(file_name, new_file_name)
        self.assertTrue(os.path.isfile(new_file_name))
        delete_file(new_file_name)

    def test_replace_file_path(self):
        new_file('test_file.txt')
        new_folder('test_replace_path')
        replace_file_path('test_file.txt', 'test_replace_path/test_file2.txt')
        self.assertTrue(os.path.exists('test_replace_path/test_file2.txt'))
        delete_folder('test_replace_path')


    def test_file_size(self):
        file_name = 'test_manager.py'
        self.assertEqual(file_size(file_name), os.stat(file_name).st_size)

    def test_dir_structure(self):
        dir_structure_to_json('test_structure.json')
        test_path = 'data/test_structure.json'
        with open(test_path, 'r+') as f:
            tmp_json = json.load(f)

        self.assertEqual(tmp_json, dir_structure('.'))

        delete_file(test_path)

if __name__ == '__main__':
    unittest.main()