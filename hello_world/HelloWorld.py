import unittest


class HelloWorld:

    def get_hello_world(self,name=None):
        if name is None:
            return "Hello World !"
        return "Hello World ! I'm "+name


class HelloWorldTest(unittest.TestCase):
    def test_for_get_hello_world_method(self):
        hello_note = HelloWorld()
        self.assertEqual(hello_note.get_hello_world(), "Hello World !")

    def test_for_get_hello_world_method_name(self):
        hello_note = HelloWorld()
        self.assertEqual(hello_note.get_hello_world("Ashwin"), "Hello World ! I'm Ashwin")


if __name__ == '__main__':
    unittest.main()