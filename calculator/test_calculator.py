import calculator
import unittest
from unittest.mock import patch
import io

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.addition = calculator.Addition()
        self.subtraction = calculator.Subtraction()
        self.multiplication = calculator.Multiplication()
        self.division = calculator.Division()
        self.result = calculator.Result()
        self.operators = calculator.Operators()
        self.input_prompt = calculator.InputPrompt()
        self.calc = calculator.SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.addition.addition(2, 3), 5)
        self.assertEqual(self.addition.result, 5)
        self.assertEqual(str(self.addition), "5")
        self.assertEqual(self.result.set_result(5), 5)

    def test_subtraction(self):
        self.assertEqual(self.subtraction.subtraction(5, 3), 2)
        self.assertEqual(self.subtraction.result, 2)
        self.assertEqual(str(self.subtraction), "2")
        self.assertEqual(self.result.set_result(2), 2)

    def test_multiplication(self):
        self.assertEqual(self.multiplication.multiplication(2, 3), 6)
        self.assertEqual(self.multiplication.result, 6)
        self.assertEqual(str(self.multiplication), "6")
        self.assertEqual(self.result.set_result(6), 6)

    def test_division(self):
        self.assertEqual(self.division.division(6, 3), 2)
        self.assertEqual(self.division.result, 2)
        self.assertEqual(str(self.division), "2.0")
        self.assertEqual(self.result.set_result(2), 2)

    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            self.division.division(6, 0)
        self.assertEqual(self.division.result, 0)
        self.assertEqual(str(self.division), "0")

    def test_result(self):
        self.result.set_result(10)
        self.assertEqual(self.result.set_result(10), 10)
        self.assertEqual(str(self.result), "10")

    def test_result_singleton(self):
        """Test that Result is a singleton class"""
        result1 = calculator.Result()
        result2 = calculator.Result()
        self.assertIs(result1, result2)  # Should be the same instance
        
        # Changes to one should affect the other
        result1.set_result(42)
        self.assertEqual(str(result2), "42")

    def test_operators(self):
        """Test the operators class functionality"""
        ops = calculator.Operators()
        ops.add_operator("test", "t")
        self.assertIn("test", ops.operators)
        self.assertIn("t", ops.operators["test"])
        
        # Test adding second symbol to existing operation
        ops.add_operator("test", "x")
        self.assertIn("x", ops.operators["test"])
        
        # Test duplicate symbol not added twice
        ops.add_operator("test", "t")
        self.assertEqual(len(ops.operators["test"]), 2)
        
        # Test string representation
        self.assertIn("test", str(ops))

    def test_calculator_initialization(self):
        """Test that SimpleCalculator initializes correctly"""
        calc = calculator.SimpleCalculator()
        self.assertIsInstance(calc.operators, calculator.Operators)
        self.assertIsInstance(calc.input, calculator.InputPrompt)
        self.assertIsInstance(calc.result, calculator.Result)
        self.assertTrue(calc.running)

    def test_calculator_find_operation(self):
        """Test finding operations by symbol"""
        calc = calculator.SimpleCalculator()
        self.assertEqual(calc.find_operation("+"), "addition")
        self.assertEqual(calc.find_operation("add"), "addition")
        self.assertEqual(calc.find_operation("-"), "subtraction")
        self.assertEqual(calc.find_operation("*"), "multiplication")
        self.assertEqual(calc.find_operation("/"), "division")
        self.assertEqual(calc.find_operation("unknown"), None)

    def test_calculator_perform_operation(self):
        """Test operation execution"""
        calc = calculator.SimpleCalculator()
        self.assertEqual(calc.perform_operation("addition", 2, 3), 5)
        self.assertEqual(calc.perform_operation("subtraction", 5, 2), 3)
        self.assertEqual(calc.perform_operation("multiplication", 2, 3), 6)
        self.assertEqual(calc.perform_operation("division", 6, 2), 3)
        
        # Test invalid operation
        with self.assertRaises(ValueError):
            calc.perform_operation("invalid", 1, 2)

    @patch('builtins.input', side_effect=["5 + 3", "n"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_calculator_calculate_addition(self, mock_stdout, mock_input):
        """Test calculator's main calculation loop with addition"""
        calc = calculator.SimpleCalculator()
        calc.calculate()
        output = mock_stdout.getvalue()
        self.assertIn("8", output)  # Result should be 8

    @patch('builtins.input', side_effect=["5 - 3", "n"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_calculator_calculate_subtraction(self, mock_stdout, mock_input):
        calc = calculator.SimpleCalculator()
        calc.calculate()
        output = mock_stdout.getvalue()
        self.assertIn("2", output)

    @patch('builtins.input', side_effect=["5 * 3", "n"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_calculator_calculate_multiplication(self, mock_stdout, mock_input):
        calc = calculator.SimpleCalculator()
        calc.calculate()
        output = mock_stdout.getvalue()
        self.assertIn("15", output)

    @patch('builtins.input', side_effect=["6 / 3", "n"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_calculator_calculate_division(self, mock_stdout, mock_input):
        calc = calculator.SimpleCalculator()
        calc.calculate()
        output = mock_stdout.getvalue()
        self.assertIn("2", output)

    @patch('builtins.input', side_effect=["6 / 0", "n"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_calculator_calculate_division_by_zero(self, mock_stdout, mock_input):
        calc = calculator.SimpleCalculator()
        calc.calculate()
        output = mock_stdout.getvalue()
        self.assertIn("Error", output)

    @patch('builtins.input', side_effect=["exit"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_calculator_exit(self, mock_stdout, mock_input):
        calc = calculator.SimpleCalculator()
        calc.calculate()
        output = mock_stdout.getvalue()
        self.assertIn("Goodbye", output)

    @patch('builtins.input', side_effect=["invalid input", "exit"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_calculator_invalid_input(self, mock_stdout, mock_input):
        calc = calculator.SimpleCalculator()
        calc.calculate()
        output = mock_stdout.getvalue()
        self.assertIn("Invalid", output)

    @patch('builtins.input', side_effect=["5 $ 3", "exit"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_calculator_unknown_operator(self, mock_stdout, mock_input):
        calc = calculator.SimpleCalculator()
        calc.calculate()
        output = mock_stdout.getvalue()
        self.assertIn("Invalid", output)

    @patch('builtins.input', side_effect=["5 + 3", "y", "10 * 2", "n"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_calculator_multiple_calculations(self, mock_stdout, mock_input):
        calc = calculator.SimpleCalculator()
        calc.calculate()
        output = mock_stdout.getvalue()
        self.assertIn("8", output)
        self.assertIn("20", output)

if __name__ == '__main__':
    unittest.main(verbosity=2)