import unittest
from src.Booking import Booking

class TestingBookingClass(unittest.TestCase):
    def test_for_creating_a_new_object_from_booking_class(self):
        booking = Booking("Adam", "001", 3)
        self.assertEqual("Adam", booking.get_guest_name)

    def test_for_guest_name_for_new_object_from_booking_class(self):
        booking = Booking("Adamson", "001", 3)
        self.assertEqual("Adamson", booking.get_guest_name)

    def test_for_room_number_for_new_object_from_booking_class(self):
        booking = Booking("Adamson", "001", 3)
        self.assertEqual("001", booking.get_room_number())

    def test_for_room_number_of_night_for_new_object_from_booking_class(self):
        booking = Booking("Adamson", "001", 3)
        self.assertEqual(3, booking.get_number_of_night())


