from dataclasses import dataclass


@dataclass
class Book:
    title: str
    description: str
    price: float
    quantity: int