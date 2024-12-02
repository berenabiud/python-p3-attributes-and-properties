#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]
class Dog:
    def __init__(self, name="Dog", breed="Mutt"):
        self._name = None  # Initialize a private attribute for name
        self.name = name   # Use the setter to validate the default name
        self.breed = breed

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value
        else:
            print("Name must be string between 1 and 25 characters.")
class Dog:
    # Define the approved breeds as a class attribute
    approved_breeds = [
        "Mastiff", "Chihuahua", "Corgi", "Shar Pei", 
        "Beagle", "French Bulldog", "Pug", "Pointer"
    ]

    def __init__(self, name="Dog", breed="Mutt"):
        self._name = None  # Initialize a private attribute for name
        self._breed = None  # Initialize a private attribute for breed
        self.name = name    # Use the setter to validate the default name
        self.breed = breed  # Use the setter to validate the default breed

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value
        else:
            print("Name must be string between 1 and 25 characters.")

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, value):
        if value in self.approved_breeds or value == "Mutt":
            self._breed = value
        else:
            print("Breed must be in list of approved breeds.")
