class Booking:
    def __init__(self, guest_name, room_number, number_of_night):
        self.guest_name = guest_name
        self.room_number = room_number
        self.number_of_night = number_of_night


    @property
    def get_guest_name(self):
        return self.guest_name

    def get_room_number(self):
        return self.room_number

    def get_number_of_night(self):
        return self.number_of_night