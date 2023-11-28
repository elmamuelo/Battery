import matplotlib.pyplot as plt

class Bateria:
    def __init__(self, porcentaje, voltaje):
        self.porcentaje = porcentaje
        self.voltaje = voltaje

class Circuito:
    def __init__(self, resistencia, bateria):
        self.resistencia = resistencia
        self.bateria = bateria

    def calcular_corriente(self):
        return self.bateria.voltaje / self.resistencia

# Datos proporcionados
datos = [
    {"%": 100, "V": 9.05},
    {"%": 95, "V": 9.0465},
    # ... Agrega el resto de los datos aquí ...
    {"%": 0, "V": 8.8}
]

# Crear las baterías
baterias = [Bateria(dato["%"], dato["V"]) for dato in datos]

# Crear el circuito con una resistencia de 10 ohmios
circuito = Circuito(10, baterias[0])

# Calcular la corriente para cada batería
corrientes = [circuito.calcular_corriente() for circuito.bateria in baterias]

# Crear la gráfica
plt.figure(figsize=(10, 6))
plt.plot([bateria.porcentaje for bateria in baterias], corrientes, marker='o')
plt.title('Gráfica de Corriente vs Porcentaje de Carga')
plt.xlabel('Porcentaje de Carga (%)')
plt.ylabel('Corriente (A)')
plt.grid(True)
plt.show()
