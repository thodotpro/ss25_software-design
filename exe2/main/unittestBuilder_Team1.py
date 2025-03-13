import unittest
import excersiseBuilder_Team1 as exercise_builder

class TestBuilder(unittest.TestCase):
    def setUp(self):
        self.windows = exercise_builder.WindowsFactory()
        self.macos = exercise_builder.MacOSFactory()

    def test_windows_button(self):
        self.assertEqual(self.windows.create_button(), "This is a Windows button")
        self.assertFalse(self.windows.create_button() == "This is a MacOS button")
        self.assertIsInstance(self.windows.create_button(), str)

    def test_windows_checkbox(self):
        self.assertEqual(self.windows.create_checkbox(), "This is a Windows checkbox")
        self.assertFalse(self.windows.create_checkbox() == "This is a MacOS checkbox")
        self.assertIsInstance(self.windows.create_checkbox(), str)

    def test_macos_button(self):
        self.assertEqual(self.macos.create_button(), "This is a MacOS button")
        self.assertFalse(self.macos.create_button() == "This is a Windows button")
        self.assertIsInstance(self.macos.create_button(), str)

    def test_macos_checkbox(self):
        self.assertEqual(self.macos.create_checkbox(), "This is a MacOS checkbox")
        self.assertFalse(self.macos.create_checkbox() == "This is a Windows checkbox")
        self.assertIsInstance(self.macos.create_checkbox(), str)

    def test_ui_factory_instantiation(self):
        self.assertRaises(TypeError, exercise_builder.UIFactory)

    def tearDown(self):
        self.windows = None
        self.macos = None

if __name__ == "__main__":
    unittest.main(verbosity=2)