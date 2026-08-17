import numpy as np
import matplotlib.pyplot as plt
from math import ceil

current = np.array([0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4.0, 4.5, 5])
dI = 0

voltage = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
dU = 0

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
                rf'$m = ({round(slope * 10**2)/10**2:.2f} \pm {ceil(dSlope * 10**2)/10**2})$ A/V' +
                '\n' +
                rf'$b = ({round(b * 10)/10} \pm {ceil(dB * 10)/10})$ A'
)
ax.set_ylabel(r"$I/(\mathrm{A})$")
ax.set_xlabel(r"$U/(\mathrm{V})$ ")
ax.legend()
ax.set_title(r"$I(U)$-Diagramm zur Überprüfung des Ohm'schen Gesetzes")
plt.show()
# plt.savefig("./05_ESK/Images/TV2_U-I-Diagramm.jpg", dpi = 400)