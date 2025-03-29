import calculator
import unittest

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.ops = calculator.Operators()
        self.calc = calculator.SimpleCalculator()


    def test_add_operator(self):
        self.ops.add_operator("addition", "+")
        self.assertIn("+", self.ops.operators["addition"])
        self.ops.add_operator("addition", "add")
        self.assertIn("add", self.ops.operators["addition"])
        self.ops.add_operator("addition", "plus")
        self.assertIn("plus", self.ops.operators["addition"])
        self.ops.add_operator("subtraction", "-")
        self.assertIn("-", self.ops.operators["subtraction"])
        self.ops.add_operator("subtraction", "sub")
        self.assertIn("sub", self.ops.operators["subtraction"])
        self.ops.add_operator("subtraction", "minus")
        self.assertIn("minus", self.ops.operators["subtraction"])
        self.ops.add_operator("multiplication", "*")
        self.assertIn("*", self.ops.operators["multiplication"])
        self.ops.add_operator("multiplication", "mal")
        self.assertIn("mal", self.ops.operators["multiplication"])
        self.ops.add_operator("multiplication", "times")
        self.assertIn("times", self.ops.operators["multiplication"])
        self.ops.add_operator("division", "/")
        self.assertIn("/", self.ops.operators["division"])
        self.ops.add_operator("division", "div")
        self.assertIn("div", self.ops.operators["division"])
        self.ops.add_operator("division", "divide")
        self.assertIn("divide", self.ops.operators["division"])
        self.ops.add_operator("division", "durch")
        self.assertIn("durch", self.ops.operators["division"])
        self.ops.add_operator("result", "enter")
        self.assertIn("enter", self.ops.operators["result"])
        self.ops.add_operator("result", "return")
        self.assertIn("return", self.ops.operators["result"])
        self.ops.add_operator("result", "go")
        self.assertIn("go", self.ops.operators["result"])
        self.ops.add_operator("result", "=")
        self.assertIn("=", self.ops.operators["result"])
    
    def test_str(self):
        self.assertEqual(str(self.ops), str({}))

    def test_rem_operator(self):
        self.ops.add_operator("addition", "+")
        self.ops.rem_operator("addition", "+")
        self.assertNotIn("+", self.ops.operators["addition"])
        self.ops.rem_operator("addition", "add")
        self.assertNotIn("add", self.ops.operators["addition"])
        self.ops.rem_operator("addition", "plus")
        self.assertNotIn("plus", self.ops.operators["addition"])
        self.ops.rem_operator("subtraction", "-")
        self.assertNotIn("-", self.ops.operators["subtraction"])
        self.ops.rem_operator("subtraction", "sub")
        self.assertNotIn("sub", self.ops.operators["subtraction"])
        self.ops.rem_operator("subtraction", "minus")
        self.assertNotIn("minus", self.ops.operators["subtraction"])
        self.ops.rem_operator("multiplication", "*")
        self.assertNotIn("*", self.ops.operators["multiplication"])
        self.ops.rem_operator("multiplication", "mal")
        self.assertNotIn("mal", self.ops.operators["multiplication"])
        self.ops.rem_operator("multiplication", "times")
        self.assertNotIn("times", self.ops.operators["multiplication"])
        self.ops.rem_operator("division", "/")
        self.assertNotIn("/", self.ops.operators["division"])
        self.ops.rem_operator("division", "div")
        self.assertNotIn("div", self.ops.operators["division"])
        self.ops.rem_operator("division", "divide")
        self.assertNotIn("divide", self.ops.operators["division"])
        self.ops.rem_operator("division", "durch")
        self.assertNotIn("durch", self.ops.operators["division"])
        self.ops.rem_operator("result", "enter")
        self.assertNotIn("enter", self.ops.operators["result"])
        self.ops.rem_operator("result", "return")
        self.assertNotIn("return", self.ops.operators["result"])
        self.ops.rem_operator("result", "go")
        self.assertNotIn("go", self.ops.operators["result"])
        self.ops.rem_operator("result", "=")
        self.assertNotIn("=", self.ops.operators["result"])




if __name__ == '__main__':
    unittest.main(verbosity=2)