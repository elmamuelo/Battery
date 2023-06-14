from pylab import *

nominal_voltage = 12.0
resistance = 1.0
current = 2.0
voltage_history = []
time = []

for i in range(100):
    time.append(i)
    dVoltage = nominal_voltage * (i / 100)
    voltage_history.append((nominal_voltage - dVoltage) - (current * resistance))

print(voltage_history)
print(time)

plt.plot(time, voltage_history)
plt.xlabel('Tiempo (s)')
plt.ylabel('Tensión (V)')
plt.title('Simulación de batería con resistencia')
plt.grid(True)
plt.show()
