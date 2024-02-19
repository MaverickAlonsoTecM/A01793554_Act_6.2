import json
import os

class Room:
    """
    This class represents a room.
    """

    def __init__(self, room_number: int, capacity: int):
        self.room_number = room_number
        self.capacity = capacity

    def reserve_room(self, hotel_name: str, customer_name: str, check_in_date: str, check_out_date: str):
        """
        This method reserves a room for a customer.
        """
        reservation_data = {
            'room_number': self.room_number,
            'capacity': self.capacity,
            'hotel_name': hotel_name,
            'customer_name': customer_name,
            'check_in_date': check_in_date,
            'check_out_date': check_out_date
        }
        file_path = os.path.join(f'{hotel_name}_reservations.json')
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                reservations = json.load(file)
        else:
            reservations = []
        reservations.append(reservation_data)
        with open(file_path, 'w') as file:
            json.dump(reservations, file)

    def cancel_reservation(self, hotel_name: str, customer_name: str, check_in_date: str, check_out_date: str):
        """
        This method cancels a reservation for a customer.
        """
        file_path = os.path.join(f'{hotel_name}_reservations.json')
        with open(file_path, 'r') as file:
            reservations = json.load(file)
        new_reservations = []
        for reservation in reservations:
            if reservation['room_number'] != self.room_number or reservation['customer_name'] != customer_name or reservation['check_in_date'] != check_in_date or reservation['check_out_date'] != check_out_date:
                new_reservations.append(reservation)
        with open(file_path, 'w') as file:
            json.dump(new_reservations, file)
