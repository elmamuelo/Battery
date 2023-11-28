import matplotlib.pyplot as plt

class Bateria:
    def __init__(self, porcentaje, voltaje):
        self.porcentaje = porcentaje
        self.voltaje = voltaje

class Graficador:
    def __init__(self, baterias):
        self.baterias = baterias

    def graficar(self):
        porcentajes = [bateria.porcentaje for bateria in self.baterias]
        voltajes = [bateria.voltaje for bateria in self.baterias]

        plt.figure(figsize=(10, 6))
        plt.plot(porcentajes, voltajes, marker='o')
        plt.title('Gráfica de Voltaje vs Porcentaje de Carga')
        plt.xlabel('Porcentaje de Carga (%)')
        plt.ylabel('Voltaje (V)')
        plt.grid(True)
        plt.show()

# Datos proporcionados
datos = [
    {"%": 100, "V": 9.05},
    {"%": 95, "V": 9.0465},
    {"%": 90, "V": 9.0430},
    {"%": 85, "V": 9.0394},
    {"%": 80, "V": 9.0359},
    {"%": 75, "V": 9.0324},
    {"%": 70, "V": 9.0285},
    {"%": 65, "V": 9.0243},
    {"%": 60, "V": 9.0196},
    {"%": 55, "V": 9.0144},
    {"%": 50, "V": 9.0088},
    {"%": 45, "V": 9.0026},
    {"%": 40, "V": 8.9957},
    {"%": 35, "V": 8.9881},
    {"%": 30, "V": 8.9794},
    {"%": 25, "V": 8.9697},
    {"%": 20, "V": 8.9581},
    {"%": 15, "V": 8.9284},
    {"%": 10, "V": 8.8856},
    {"%": 5, "V": 8.8428},
    {"%": 0, "V": 8.8}
]

# Crear las baterías
baterias = [Bateria(dato["%"], dato["V"]) for dato in datos]

# Crear el graficador
graficador = Graficador(baterias)

# Graficar
graficador.graficar()
