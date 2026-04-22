from dataclasses import dataclass
from typing import List
 
@dataclass(frozen=True)
class Person:
    name: str
    age: int                    # Fix: added age field so child.age works
    children: List["Person"]
 
fatma = Person(name="Fatma", age=8, children=[])
aisha = Person(name="Aisha", age=5, children=[])
 
imran = Person(name="Imran", age=35, children=[fatma, aisha])
 
def print_family_tree(person: Person) -> None:
    print(person.name)
    for child in person.children:
        print(f"- {child.name} ({child.age})")  # Now works - mypy knows child is a Person
 
print_family_tree(imran)
 