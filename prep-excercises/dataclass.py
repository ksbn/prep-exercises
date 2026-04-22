import datetime
from dataclasses import dataclass
 
@dataclass(frozen=True)
class Person:
    name: str
    date_of_birth: datetime.date
    preferred_operating_system: str
 
    def is_adult(self) -> bool:
        today = datetime.date.today()
        age = today.year - self.date_of_birth.year
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
        return age >= 18
 
imran = Person("Imran", datetime.date(2002, 5, 15), "Ubuntu")
imran2 = Person("Imran", datetime.date(2002, 5, 15), "Ubuntu")
eliza = Person("Eliza", datetime.date(1990, 3, 22), "Arch Linux")
 
# @dataclass generates __str__ for us
print(imran)   # Person(name='Imran', date_of_birth=datetime.date(2002, 5, 15), preferred_operating_system='Ubuntu')
 
# @dataclass generates __eq__ for us
print(imran == imran2)  # True - same fields
print(imran == eliza)   # False - different fields
 
# is_adult still works
print(imran.is_adult())  # True
print(eliza.is_adult())  # True