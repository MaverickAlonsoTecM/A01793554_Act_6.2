# -*- coding: utf-8 -*-

"""
This is a simple Python script that implements
the test cases for the Reservation class.
"""
import unittest
import json
import os
from bookinn.customer.customer import Customer
from bookinn.reservation.reservation import Reservation
from bookinn.hotel.hotel import Hotel

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
        self.reservation = Reservation(
            customer=Customer(
                name='John Doe',
                email='john.doe@example.com'
            ),
            check_in_date='2024-02-18',
            check_out_date='2024-02-20'
        )

    def tearDown(self):
        """
        Clean up the test case.
        """
        # Delete the reservation file after each test
        if os.path.exists('Example Hotel_reservations.json'):
            os.remove('Example Hotel_reservations.json')

    def test_create_reservation(self):
        """
        Test the create_reservation method.
        """
        self.reservation.create_reservation(hotel_name='Example Hotel')
        with open('Example Hotel_reservations.json', 'r') as file:
            reservations = json.load(file)
        self.assertIn(
            {
                "customer": "John Doe",
                "check_in_date": "2024-02-18",
                "check_out_date": "2024-02-20"
            },
            reservations
        )

    def test_cancel_reservation(self):
        """
        Test the cancel_reservation method.
        """
        self.reservation.create_reservation(hotel_name='Example Hotel')
        self.reservation.cancel_reservation(hotel_name='Example Hotel')
        with open('Example Hotel_reservations.json', 'r') as file:
            reservations = json.load(file)
        self.assertNotIn(
            {
                "customer": "John Doe",
                "check_in_date": "2024-02-18",
                "check_out_date": "2024-02-20"
            },
            reservations
        )

    def test_cancel_nonexistent_reservation(self):
        """
        Test canceling a reservation that does not exist.
        """
        # Create a reservation but don't cancel it
        self.reservation.create_reservation(hotel_name='Example Hotel')
        # Attempt to cancel a different reservation
        another_reservation = Reservation(
            customer=Customer(
                name='Jane Doe',
                email='jane.doe@example.com'
            ),
            check_in_date='2024-02-18',
            check_out_date='2024-02-20'
        )
        self.assertRaises(
            ValueError,
            another_reservation.cancel_reservation,
            hotel_name='Example Hotel'
        )

    def test_cancel_reservation_no_file(self):
        """
        Test canceling a reservation when the file does not exist.
        """
        # Create a reservation but don't cancel it
        self.reservation.create_reservation(hotel_name='Example Hotel')
        # Delete the reservation file
        os.remove('Example Hotel_reservations.json')
        # Attempt to cancel the reservation
        self.assertRaises(
            FileNotFoundError,
            self.reservation.cancel_reservation,
            hotel_name='Example Hotel'
        )

    def test_cancel_reservation_empty_file(self):
        """
        Test canceling a reservation when the file is empty.
        """
        # Create a reservation but don't cancel it
        self.reservation.create_reservation(hotel_name='Example Hotel')
        # Empty the reservation file
        open('Example Hotel_reservations.json', 'w').close()
        # Attempt to cancel the reservation
        self.assertRaises(
            json.JSONDecodeError,
            self.reservation.cancel_reservation,
            hotel_name='Example Hotel'
        )

    def test_cancel_reservation_invalid_json(self):
        """
        Test canceling a reservation when the file contains invalid JSON.
        """
        # Create a reservation but don't cancel it
        self.reservation.create_reservation(hotel_name='Example Hotel')
        # Write invalid JSON to the reservation file
        with open('Example Hotel_reservations.json', 'w') as file:
            file.write('invalid json')
        # Attempt to cancel the reservation
        self.assertRaises(
            json.JSONDecodeError,
            self.reservation.cancel_reservation,
            hotel_name='Example Hotel'
        )


if __name__ == '__main__':
    unittest.main()
