class Person:
    """
    Represents a person with a nickname, name, family, and age.

    Attributes:
    ------------------------------------------------------------
        nickname(str): The person's nickname
        name(str): The person's first name
        family(str): The person's last name
        age(int): The person's age
    """
    def __init__(self, nickname, name, family, age):
        # Constructs a Person object.
        self.nickname = nickname
        self.name = name
        self.family = family
        self.age = int(age)

    def __str__(self):
        # Returns a string representation of the person object.
        return f'{self.nickname} ({self.name} {self.family}, {self.age})'