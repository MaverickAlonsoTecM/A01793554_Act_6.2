# -*- coding: utf-8 -*-

"""
This is a simple Python script that implements the Customer class.
"""

# Standard library imports
import json
import os

# Class definitions
class Customer:
    """
    This class represents a customer.
    """

    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    def save_customer(self):
        """
        This method creates a new customer and stores it in a file.
        """
        customer_data = {
            'name': self.name,
            'email': self.email
        }
        with open(f'{self.name}.json', 'w') as file:
            json.dump(customer_data, file)

    def delete_customer(self):
        """
        This method deletes a customer and its associated file.
        """
        if os.path.exists(f'{self.name}.json'):
            os.remove(f'{self.name}.json')

    def display_customer_information(self):
        """
        This method displays the customer's information.
        """
        with open(f'{self.name}.json', 'r') as file:
            customer_data = json.load(file)
            print(f'Customer: {customer_data["name"]}, Email: {customer_data["email"]}')

    def modify_customer_information(self, new_name: str, new_email: str):
        """
        This method modifies the customer's information.
        """
        with open(f'{self.name}.json', 'r') as file:
            customer_data = json.load(file)
            customer_data['name'] = new_name
            customer_data['email'] = new_email
        with open(f'{new_name}.json', 'w') as file:
            json.dump(customer_data, file)
        self.delete_customer()
