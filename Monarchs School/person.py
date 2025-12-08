class Person:
    def __init__(self, name, age, phone):
        self.name = name
        self.age = age
        self.phone = phone

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def __str__(self):
        return f"{self.name}\n{self.age}\n{self.phone}"

person = Person("ade",21,"08122713205")
print(person)