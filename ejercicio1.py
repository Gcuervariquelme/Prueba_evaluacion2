import math

class Estrella:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"Estrella({self.x}, {self.y}, {self.z})"

    def galaxia(self):
        if self.x**2 + self.y**2 + self.z**2 < 10000:
            return "Vía Láctea"
        else:
            return "Andrómeda"

    def distancia(self, otra):
        return math.sqrt((self.x - otra.x)**2 + (self.y - otra.y)**2 + (self.z - otra.z)**2)

# Creación de estrellas
estrella_a = Estrella(2, 3, 1)
estrella_b = Estrella(4, 4, 4)
estrella_c = Estrella(-3, -1, 0)

# Impresión de estrellas y sus galaxias
estrellas = [estrella_a, estrella_b, estrella_c]
for estrella in estrellas:
    print(f"{estrella} en la galaxia {estrella.galaxia()}")

# Cálculo de distancias
distancia_ab = estrella_a.distancia(estrella_b)
distancia_bc = estrella_b.distancia(estrella_c)
print(f"Distancia entre A y B: {distancia_ab}")
print(f"Distancia entre B y C: {distancia_bc}")
