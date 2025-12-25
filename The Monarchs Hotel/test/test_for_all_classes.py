import unittest
from src.Booking import Booking
from src.Guest import Guest
from src.Hotel import Hotel
from src.Room import Room

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


class TestingForGuestClass(unittest.TestCase):
    def test_for_creating_a_new_guests_object(self):
        guest = Guest("Benny", "adamson@gmail.com", "08122222222", 1234,False)
        self.assertEqual("Benny", guest.get_name())

    # def test_for_invalid_email_for_a_new_guests_object(self):
    #     with self.assertRaises(TypeError):
    #         Guest("Benny", "macadamising.com", "08122222222", 1234,False)

    def test_for_invalid_email_for_a_new_guests_object(self):
        with self.assertRaises(TypeError):
            Guest("Benny", "macadam@ising.com", "081222", 1234,False)

class TestingForRoomClass(unittest.TestCase):
    def test_for_creating_a_new_room(self):
        room = Room("single", "001", 10000)
        self.assertEqual("single", room.get_room_type())

class TestingForHotel(unittest.TestCase):
    def test_for_creating_a_hotel_object(self):
        hotel = Hotel("The Monarchs Hotel")
        self.assertEqual("The Monarchs Hotel", hotel.get_name())

    def test_add_a_guest_to_an_hotel(self):
        hotel = Hotel("The Monarchs Hotel")
        guest = Guest("Benny", "adamson@gmail.com", "08122222222", 1234,False)
        hotel.add_guest(guest)
