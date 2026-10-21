class CaloriasInvalidasError(Exception):
    def __init__(self, calorias):
        self.calorias = calorias
        super().__init__(f"Calorías inválidas: {calorias}. Deben ser un número entero positivo.")