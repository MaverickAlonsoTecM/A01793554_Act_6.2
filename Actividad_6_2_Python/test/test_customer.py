"""
This module contains unit tests for the Customer class.
"""

import unittest
from unittest.mock import patch
from io import StringIO
import json
import os

from bookinn.customer.customer import Customer


class TestCustomer(unittest.TestCase):
    """
    This class contains unit tests for the Customer class.
    """

    def setUp(self):
        """
        Set up the test environment.
        """
        self.customer = Customer('JesusA', 'JEsteinerA@gmail.com')
        self.customer.save_customer()

    def tearDown(self):
        """
        Tear down the test environment.
        """
        if os.path.exists('JesusA.json'):
            os.remove('JesusA.json')

    def test_save_customer(self):
        """
        Test the save_customer method.
        """
        self.assertTrue(os.path.exists('JesusA.json'))

    def test_delete_customer(self):
        """
        Test the delete_customer method.
        """
        self.customer.delete_customer()
        self.assertFalse(os.path.exists('JesusA.json'))

    def test_display_customer_information(self):
        """
        Test the display_customer_information method.
        """
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.customer.display_customer_information()
            self.assertEqual(
                fake_out.getvalue().strip(),
                'Customer: JesusA, Email: JEsteinerA@gmail.com'
            )

    def test_modify_customer_information(self):
        """
        Test the modify_customer_information method.
        """
        new_name = 'JesusA_2'
        new_email = 'JEsteinerA@gmail.com'
        self.customer.modify_customer_information(new_name, new_email)
        with open(f'{new_name}.json', 'r', encoding='utf-8') as file:
            customer_data = json.load(file)
            self.assertEqual(customer_data['name'], new_name)
            self.assertEqual(customer_data['email'], new_email)


if __name__ == '__main__':
    unittest.main()
