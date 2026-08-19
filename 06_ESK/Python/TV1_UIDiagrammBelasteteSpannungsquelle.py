import numpy as np
import matplotlib.pyplot as plt
from math import ceil

current = np.array([10.67, 12.6, 14.6, 16.6, 18.6, 20.6, 22.6, 24.6, 26.6, 28.6, 30.6, 33.2])
dI = np.array([0.15, 0.6, 0.6, 0.6, 0.6, 0.7, 0.7, 0.7, 0.7, 0.7, 0.8, 0.8])

voltage = np.array([1.362, 1.335, 1.290, 1.259, 1.223, 1.186, 1.145, 1.104, 1.064, 1.017, 1.002, 0.938])
dU = np.array([0.018, 0.018, 0.017, 0.017, 0.017, 0.016, 0.016, 0.015, 0.015, 0.015, 0.015, 0.014])

line, cov = np.polyfit(current, voltage, 1, cov = True)
slope, b = line
dSlope, dB = np.sqrt(np.diag(cov))

fig, ax = plt.subplots(figsize = (7, 4.5))
ax.errorbar(current, voltage, dU, dI,
            fmt='o', color='steelblue', ecolor='salmon',
            ms=3, capsize=3, label='Messdaten'
)
ax.plot(current, slope*current + b,
        color = "red", linestyle = "--",
        label = rf'Linearer Fit' + '\n' + 
                rf'$m = ({round(slope * 10**4)/10**4} \pm {ceil(dSlope * 10**4)/10**4})$ V/mA' +
                '\n' +
                rf'$b = ({round(b * 10**3)/10**3} \pm {ceil(dB * 10**3)/10**3})$ V'
)
ax.set_xlabel(r"$I/(\mathrm{mA})$")
ax.set_ylabel(r"$U/(\mathrm{V})$ ")
ax.legend()
ax.set_title(r"$U(I)$-Diagramm einer belateten galvanischen Zelle")
# plt.show()
plt.savefig("./06_ESK/Images/TV1_U-I-Diagramm.jpg", dpi = 400)