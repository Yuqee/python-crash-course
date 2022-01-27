import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Tests for the class Employee."""

    def setUp(self):
        """
        Create a employee for use in all test methods.
        """
        self.my_employee = Employee('james', 'bond', 10000)
    
    def test_give_default_raise(self):
        old = self.my_employee.annual_salary
        self.my_employee.give_raise()
        self.assertEqual(self.my_employee.annual_salary-old, 5000)

    def test_give_custom_raise(self):
        old = self.my_employee.annual_salary
        custom_raise = 3000
        self.my_employee.give_raise(custom_raise)
        self.assertEqual(self.my_employee.annual_salary-old, custom_raise)

if __name__ == '__main__':
    unittest.main()