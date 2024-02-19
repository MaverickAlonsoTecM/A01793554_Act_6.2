import json
import os
import unittest
from bookinn.room.room import Room

class TestRoom(unittest.TestCase):
    """
    Test cases for the Room class.
    """

    def setUp(self):
        """
        Set up the test case.
        """
        self.room = Room(room_number=101, capacity=2)

    def test_reserve_room(self):
        """
        Test the reserve_room method.
        """
        self.room.reserve_room(hotel_name='Example Hotel', customer_name='John Doe', check_in_date='2024-02-18', check_out_date='2024-02-20')
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
        self.room.reserve_room(hotel_name='Example Hotel', customer_name='John Doe', check_in_date='2024-02-18', check_out_date='2024-02-20')
        self.room.cancel_reservation(hotel_name='Example Hotel', customer_name='John Doe', check_in_date='2024-02-18', check_out_date='2024-02-20')
        with open(
            'Example Hotel_reservations.json',
            'r',
            encoding='utf-8'
        ) as file:
            reservations = json.load(file)
            self.assertEqual(len(reservations), 0)


if __name__ == '__main__':
    unittest.main()
