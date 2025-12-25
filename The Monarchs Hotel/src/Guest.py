
class Guest:
    def __init__(self, name, email, phone_number, pin, occupied_room):
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.pin = pin
        self.occupied_room = occupied_room

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def email(self):
        return self._email

    # @email.setter
    # def email(self, value):
    #     if "@" not in self.email:
    #         raise "Invalid email address"
    #     self._email = value

    @property
    def phone_number(self):
        return self.phone_number

    # @phone_number.setter
    # def phone_number(self, value):
    #     if len(self.phone_number) < 7:
    #         raise "Invalid phone number, less than 11 digits"
    #     self.phone_number = value



