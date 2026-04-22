import sys
from dataclasses import dataclass
from enum import Enum
from typing import List
 
 
class OperatingSystem(Enum):
    MACOS = "macOS"
    ARCH = "Arch Linux"
    UBUNTU = "Ubuntu"
 
 
@dataclass(frozen=True)
class Person:
    name: str
    age: int
    preferred_operating_systems: List[OperatingSystem]
 
 
@dataclass(frozen=True)
class Laptop:
    id: int
    manufacturer: str
    model: str
    screen_size_in_inches: float
    operating_system: OperatingSystem
 
 
def find_possible_laptops(laptops: List[Laptop], person: Person) -> List[Laptop]:
    possible_laptops = []
    for laptop in laptops:
        if laptop.operating_system in person.preferred_operating_systems:
            possible_laptops.append(laptop)
    return possible_laptops
 
 
def parse_operating_system(value: str) -> OperatingSystem:
    valid_options = {os.value.lower(): os for os in OperatingSystem}
    result = valid_options.get(value.strip().lower())
    if result is None:
        valid_names = ", ".join(os.value for os in OperatingSystem)
        print(f"Error: '{value}' is not a valid operating system. Choose from: {valid_names}", file=sys.stderr)
        sys.exit(1)
    return result
 
 
def parse_age(value: str) -> int:
    try:
        age = int(value.strip())
        if age <= 0:
            raise ValueError
        return age
    except ValueError:
        print(f"Error: '{value}' is not a valid age.", file=sys.stderr)
        sys.exit(1)
 
 
# Library's available laptops
laptops: List[Laptop] = [
    Laptop(id=1, manufacturer="Dell", model="XPS", screen_size_in_inches=13, operating_system=OperatingSystem.ARCH),
    Laptop(id=2, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=3, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=4, manufacturer="Apple", model="MacBook", screen_size_in_inches=13, operating_system=OperatingSystem.MACOS),
    Laptop(id=5, manufacturer="Apple", model="MacBook", screen_size_in_inches=15, operating_system=OperatingSystem.MACOS),
    Laptop(id=6, manufacturer="Apple", model="MacBook", screen_size_in_inches=15, operating_system=OperatingSystem.MACOS),
]
 
# Accept user input - convert to constrained types as early as possible
print("Welcome to the Laptop Library!")
print(f"Available operating systems: {', '.join(os.value for os in OperatingSystem)}")
print()
 
name = input("Enter your name: ").strip()
age = parse_age(input("Enter your age: "))
preferred_os = parse_operating_system(input("Enter your preferred operating system: "))
 
person = Person(name=name, age=age, preferred_operating_systems=[preferred_os])
 
# Count laptops per OS
laptops_by_os: dict[OperatingSystem, List[Laptop]] = {}
for os in OperatingSystem:
    laptops_by_os[os] = [l for l in laptops if l.operating_system == os]
 
# Find matching laptops
matching_laptops = find_possible_laptops(laptops, person)
print(f"\nHi {person.name}! We have {len(matching_laptops)} laptop(s) with {preferred_os.value}.")
 
# Find if another OS has more laptops available
best_os = max(laptops_by_os, key=lambda os: len(laptops_by_os[os]))
if best_os != preferred_os and len(laptops_by_os[best_os]) > len(matching_laptops):
    print(f"Tip: If you're willing to use {best_os.value}, we have {len(laptops_by_os[best_os])} laptop(s) available — more likely to get one!")
 