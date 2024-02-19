# -*- coding: utf-8 -*-

"""
This is a simple Python script that implements
the test cases for the Reservation class.
"""

# Standard library imports
import json
import unittest
from bookinn.customer.customer import Customer
from bookinn.reservation.reservation import Reservation

# Module-level constants
HOTEL_CAPACITY = 100


# Unit test cases
class TestReservation(unittest.TestCase):
    """
    Test cases for the Reservation class.
    """

    def setUp(self):
        """
        Set up the test case.
        """
        self.customer = Customer(name='JesusA', email='JEsteinerA@gmail.com')
        self.reservation = Reservation(
            customer=self.customer,
            check_in_date='2024-02-18',
            check_out_date='2024-02-20'
        )

    def test_create_reservation(self):
        """
        Test the create_reservation method.
        """
        self.reservation.create_reservation(hotel_name='Example Hotel')
        with open(
            'Example Hotel_reservations.json',
            'r',
            encoding='utf-8'
        ) as file:
            reservations = json.load(file)
            self.assertEqual(len(reservations), 1)

    def test_cancel_reservation(self):
        """
        Test the cancel_reservation method.
        """
        self.reservation.create_reservation(hotel_name='Example Hotel')
        self.reservation.cancel_reservation(hotel_name='Example Hotel')
        with open(
            'Example Hotel_reservations.json',
            'r',
            encoding='utf-8'
        ) as file:
            reservations = json.load(file)
            self.assertEqual(len(reservations), 0)


if __name__ == '__main__':
    unittest.main()
