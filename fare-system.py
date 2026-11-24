# CS3 Pair Assessment: Fare System
# Authors: Shiloh Quisote, Vittoria Bestes
# Section: (write your section here)

from abc import ABC, abstractmethod

class Vehicle(ABC):
    """Abstract base class for every public vehicle."""

    def __init__(self, plate_number, capacity):
        self.__plate_number = plate_number
        self.__capacity = capacity

    def get_plate_number(self):
        return self.__plate_number
    
    def set_plate_number(self, plate_number):
        self.__plate_number = plate_number

    def get_capacity(self):
        return self.__capacity


    def set_capacity(self, capacity):
        try:
            if int(capacity) == capacity and capacity > 0:
                self.__capacity = capacity
            else:
                print("Invalid capacity.")
        except (ValueError, TypeError):
            print("Invalid capacity.")

    @abstractmethod
    
    def compute_fare(self, distance_km):
        pass

    @abstractmethod

    def describe(self):
        pass
    
# ===== Jeepney class (Developer A) =====

class Jeepney(Vehicle):
    def __init__(self, plate_number, capacity, route):
        super().__init__(plate_number, capacity)
        self.__route = route


    def get_route(self):
        return self.__route


    def set_route(self, route):
        self.__route = route


    def compute_fare(self, distance_km):
        if distance_km <= 4:
            return 13.00
        return round(13.00 + (distance_km - 4) * 1.80, 2)


    def describe(self):
        return f"Jeepney {self.__plate_number} | Route: {self.__route} | Seats: {self.__capacity}"
    
# ===== Tricycle class (Developer B) =====

class Tricycle(Vehicle):
    def __init__(self, plate_number, capacity, barangay):
        super().__init__(plate_number, capacity)
        self.__barangay = barangay


    def get_barangay(self):
        return self.__barangay


    def set_barangay(self, barangay):
        self.__barangay = barangay


    def compute_fare(self, distance_km):
        if distance_km <= 2:
            return 20.00
        return round(20.00 + (distance_km -2) * 5.00, 2)


    def describe(self):
        return f"Tricycle {self.__plate_number} | Barangay: {self.__barangay} | Seats: {self.__capacity}"
    
# ===== Test code (Part 6 only) =====