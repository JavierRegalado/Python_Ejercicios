from dataclasses import dataclass

@dataclass

class comida:
    nombre: str
    calorias: int
    proteinas: float
    carbohidratos: float
    grasas: float


print(repr(comida("Pizza", 300, 12.5, 35.0, 10.0)))