# -*- coding: utf-8 -*-

"""
This is a simple Python script that implements the Reservation class.
"""

# Standard library imports
import json
import os

# Class definitions
class Reservation:
    """
    This class represents a reservation.
    """

    def __init__(self, customer, check_in_date, check_out_date):
        self.customer = customer
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date

    def create_reservation(self, hotel_name: str):
        """
        This method creates a new reservation and stores it in a file.
        """
        reservation_data = {
            'customer': self.customer.name,
            'check_in_date': self.check_in_date,
            'check_out_date': self.check_out_date
        }
        filename = f'{hotel_name}_reservations.json'
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                reservations = json.load(file)
        else:
            reservations = []
        reservations.append(reservation_data)
        with open(filename, 'w') as file:
            json.dump(reservations, file)

    def cancel_reservation(self, hotel_name: str):
        """
        This method cancels a reservation.
        """
        filename = f'{hotel_name}_reservations.json'
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                reservations = json.load(file)
        else:
            return  # No reservations to cancel
        new_reservations = []
        for reservation in reservations:
            if reservation['customer'] == self.customer.name and reservation['check_in_date'] == self.check_in_date and reservation['check_out_date'] == self.check_out_date:
                continue
            new_reservations.append(reservation)
        with open(filename, 'w') as file:
            json.dump(new_reservations, file)
