class Room:
    def __init__(self, room_type, room_number, room_price):
        self.room_type = room_type
        self.room_number = room_number
        self.room_price = room_price

    def get_room_type(self):
        return self.room_type

