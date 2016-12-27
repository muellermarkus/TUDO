import unittest

import main


class TestTudoMethods(unittest.TestCase):
    def setUp(self):
        main.init()
        main.task_db.reset()

    def test_add(self):
        main.add("Do Homework")
        # self.assertEqual(main.list_tasks()[-1], "Do Homework")
        print(len(main.list_tasks()))
        self.assertTrue(len(main.list_tasks()) == 1)

    def test_list(self):
        self.assertTrue(len(main.list_tasks()) == 0)


if __name__ == "__main__":
    unittest.main()