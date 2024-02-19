# -*- coding: utf-8 -*-

"""
This is a simple Python script that implements the Hotel class.
"""

# Standard library imports
import json
import os

# Module-level constants
HOTEL_CAPACITY = 100

# Class definitions
class Hotel:
    """
    This class represents a hotel.
    """

    def __init__(self, name: str, location: str, capacity: int = HOTEL_CAPACITY):
        self.name = name
        self.location = location
        self.capacity = capacity
        self.reservations = []

    def add_reservation(self, reservation):
        """
        This method adds a reservation to the hotel's list of reservations.
        """
        if len(self.reservations) < self.capacity:
            self.reservations.append(reservation)
            return True
        return False

    def remove_reservation(self, reservation):
        """
        This method removes a reservation from the hotel's list of reservations.
        """
        if reservation in self.reservations:
            self.reservations.remove(reservation)
            return True
        return False

    def get_available_capacity(self) -> int:
        """
        This method returns the available capacity of the hotel.
        """
        return self.capacity - len(self.reservations)

    def create_hotel(self):
        """
        This method creates a new hotel and stores it in a file.
        """
        hotel_data = {
            'name': self.name,
            'location': self.location,
            'capacity': self.capacity,
            'reservations': []
        }
        with open(f'{self.name}.json', 'w') as file:
            json.dump(hotel_data, file)

    def delete_hotel(self):
        """
        This method deletes a hotel and its associated file.
        """
        if os.path.exists(f'{self.name}.json'):
            os.remove(f'{self.name}.json')

    def display_hotel_information(self):
        """
        This method displays the hotel's information.
        """
        with open(f'{self.name}.json', 'r') as file:
            hotel_data = json.load(file)
            print(f'Hotel: {hotel_data["name"]}, Location: {hotel_data["location"]}, Capacity: {hotel_data["capacity"]}, Available Capacity: {self.get_available_capacity()}')

    def modify_hotel_information(self, new_name: str, new_location: str, new_capacity: int):
        """
        This method modifies the hotel's information.
        """
        with open(f'{self.name}.json', 'r') as file:
            hotel_data = json.load(file)
            hotel_data['name'] = new_name
            hotel_data['location'] = new_location
            hotel_data['capacity'] = new_capacity
        with open(f'{new_name}.json', 'w') as file:
            json.dump(hotel_data, file)
        self.delete_hotel()
