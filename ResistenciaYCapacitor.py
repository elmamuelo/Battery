from pylab import *

nominal_voltage = 12.0
resistance0 = 2.0
resistance1 = 1.0
current0 = 2.0
current1 = 1.0
capacitance = 1.0
voltage_history = []
time = []

for i in range(100):
    time.append(i)
    dVoltage = nominal_voltage * (i / 100)
    ocv = nominal_voltage-dVoltage
    voltage_history.append(ocv - (current1 * resistance1) - (current0*resistance0))

print(voltage_history)
print(time)

plt.plot(time, voltage_history)
plt.xlabel('Tiempo (s)')
plt.ylabel('Tensión (V)')
plt.title('Simulación de batería con resistencia y capacitor')
plt.grid(True)
plt.show()
