import numpy as np
import matplotlib.pyplot as plt
from math import ceil

current = np.array([0.59, 1.21, 1.82, 2.43, 3.04, 3.65, 4.27, 4.87, 5.49])
dI = 0.01 * current + 0.05

voltage = np.array([1.99, 4.01, 6.01, 8.00, 10.00, 12.01, 14.05, 16.01, 18.03])
dU = 0.009 * voltage + 0.04

line, cov = np.polyfit(voltage, current, 1, cov = True)
slope, b = line
dSlope, dB = np.sqrt(np.diag(cov))

fig, ax = plt.subplots(figsize = (7, 4.5))
ax.errorbar(voltage, current, dI, dU,
            fmt='o', color='steelblue', ecolor='salmon',
            ms=3, capsize=3, label='Messdaten'
)
ax.plot(voltage, slope*voltage + b,
        color = "red", linestyle = "--",
        label = rf'Linearer Fit' + '\n' + 
                rf'$m = ({round(slope * 10**5)/10**5:.5f} \pm {ceil(dSlope * 10**5)/10**5})$ mA/V' +
                '\n' +
                rf'$b = ({round(b * 10**4)/10**4} \pm {ceil(dB * 10**4)/10**4})$ mA'
)
ax.set_ylabel(r"$I/(\mathrm{A})$")
ax.set_xlabel(r"$U/(\mathrm{V})$ ")
ax.legend()
ax.set_title(r"$I(U)$-Diagramm zur Überprüfung des Ohm'schen Gesetzes")
# plt.show()
plt.savefig("./06_ESK/Images/TV2_U-I-Diagramm.jpg", dpi = 400)