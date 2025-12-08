class Guest:
    def __init__(self, guest_name, guest_email, guest_phone_number, guest_pin, occupied_room):

        if "@" not in guest_email:
            raise "Invalid email address"
        if len(guest_phone_number) < 7:
            raise "Invalid phone number, less than 11 digits"

        self.guest_name = guest_name
        self.guest_email = guest_email
        self.guest_phone_number = guest_phone_number
        self.guest_pin = guest_pin
        self.occupied_room = occupied_room

    def get_name(self):
        return self.guest_name


