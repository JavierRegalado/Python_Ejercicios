from model.comida import Comida
from errores.calorias_invalidas_error import CaloriasInvalidasError

try:
    pizza = Comida("Pizza", -200)

except CaloriasInvalidasError as e:
    print(f"Error: {e.calorias}")

print(pizza)
