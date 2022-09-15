import unittest
import main

m = main


class GiftsTests(unittest.TestCase):

    def setUp(self):
        self.phone_data = m.phone_data
        self.file_location = "test_data.json"
        self.sort_name = "alcatel"
        self.sort_screen = 5.0
        self.test_data = {"name":"acer go","brand":"acer","screen_inches":4.0,"camera_mp":5.0}

    def test_get_file(self):
        print("Test get remote file")
        filename = m.get_file()
        file_length = len(self.file_location)
        file_end = filename[-file_length:]
        self.assertEqual(self.file_location, file_end)

    def test_sort_file(self):
        print("Get file data and sort")
        filename = m.get_file()
        m.sort_file(filename)
        test_name = self.phone_data[1][0]
        test_size = self.phone_data[2][1]
        self.assertEqual(self.sort_name, test_name)
        self.assertEqual(self.sort_screen, test_size)

    def test_each_row(self):
        print("Test get relevant data")
        row = m.sort_each_row(self.test_data)
        self.assertEqual(row[1], 4.0)
        self.assertEqual(row[0],"acer")

    def test_sort_data(self):
        print("Test separate out data")
        total = 0
        filename = m.get_file()
        m.sort_file(filename)
        m.sort_data()
        result = m.phone_results
        num_count = 0
        for name in result:

            if name == self.sort_name:
                num_count += 1
        if num_count > 1:
            self.assertTrue(True)

        print(m.add_phone())


if __name__ == '__main__':
    unittest.main()