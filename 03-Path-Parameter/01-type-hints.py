from typing import Any

text: str = "Kankon"
percentage: int = 37
temperature: float = 45.5

number1: int | float = 12.5
optional: str | None

optional = "value"

def sqRoot(num: int | float,exp: float | None = .5) -> float:
    return pow(num, exp)

root25 = sqRoot(25.5)

digits: list[int] = [1, 2, 3, 4, 5]

ages: tuple[int, ...] = (23, 34, 43, 23, 45)

tempArea: tuple[str, float] = ("City", 34.5)

shipment: dict[str, Any] = {
    "id": 23424,
    "weight": 23.4,
    "content": "wooden table",
    "location": "New York"
}

class City:
    def __init__(self, name, location):
        self.name = name
        self.location = location

hampshire = City("Hampshire", "New York")
tempArea1: tuple[City, float] = (hampshire, 34.5)