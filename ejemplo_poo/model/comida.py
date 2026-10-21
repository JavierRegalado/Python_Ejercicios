from errores.calorias_invalidas_error import CaloriasInvalidasError


class Comida:
    def __init__(self, nombre, calorias):
        if calorias < 0:
            raise CaloriasInvalidasError(calorias)
        self.nombre = nombre
        self.calorias = calorias

    def __str__(self):
        return f"{self.nombre} tiene {self.calorias} calorías."
    def __repr__(self):
        return f"comida(nombre='{self.nombre}', calorias={self.calorias})"