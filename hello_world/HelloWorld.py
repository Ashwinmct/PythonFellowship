import unittest


class HelloWorld:

    def get_hello_world(self):
            return "Hello World"


class HelloWorldTest(unittest.TestCase):
    def test_for_get_hello_world_method(self):
        hello_note = HelloWorld()
        self.assertEqual(hello_note.get_hello_world(), "Hello World")


if __name__ == '__main__':
    unittest.main()