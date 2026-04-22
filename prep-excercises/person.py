import datetime
 
# Advantages of methods over free functions:
# 1. Ease of documentation - all Person-related behaviour is grouped together in one place
# 2. Encapsulation - if Person's internals change, only the class needs updating
# 3. Readability - imran.is_adult() reads more naturally than is_adult(imran)
 
class Person:
    def __init__(self, name: str, date_of_birth: datetime.date, preferred_operating_system: str):
        self.name = name
        self.date_of_birth = date_of_birth  # changed from age to date_of_birth
        self.preferred_operating_system = preferred_operating_system
 
    def is_adult(self) -> bool:
        today = datetime.date.today()
        age = today.year - self.date_of_birth.year
        # Adjust if birthday hasn't happened yet this year
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
        return age >= 18
 
imran = Person("Imran", datetime.date(2002, 5, 15), "Ubuntu")
eliza = Person("Eliza", datetime.date(1990, 3, 22), "Arch Linux")
 
print(imran.name)
print(imran.is_adult())  # True - Imran is 22
 
print(eliza.name)
print(eliza.is_adult())  # True - Eliza is 34
 