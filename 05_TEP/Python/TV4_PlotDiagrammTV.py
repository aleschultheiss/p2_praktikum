import numpy as np
import matplotlib.pyplot as plt
from math import ceil

theta = np.array([0.5, 15.3, 30.4, 45.9, 60.4, 74.8, 90.0])
dTheta = 0.0003*theta + 0.1

kolbenpos = np.array([52.0, 54.5, 57.2, 61.9, 65.0, 68.0, 71.5])

line, cov = np.polyfit(theta, kolbenpos, 1, cov = True)
slope, b = line
dSlope, dB = np.sqrt(np.diag(cov))

fig, ax = plt.subplots(figsize = (7, 4.5))
ax.errorbar(theta, kolbenpos, 0.5, dTheta,
            fmt='o', color='steelblue', ecolor='salmon',
            ms=3, capsize=3, label='Messdaten'
)
ax.plot(theta, slope*theta + b,
        color = "red", linestyle = "--",
        label = rf'Linearer Fit' + '\n' + 
                rf'$m = ({round(slope * 10**2)/10**2:.2f} \pm {ceil(dSlope * 10**2)/10**2})$ mm/°C' +
                '\n' +
                rf'$b = ({round(b * 10)/10} \pm {ceil(dB * 10)/10})$ mm'
)
print(-b/slope)
ax.set_ylabel(r"$x_{\mathrm{Kolben}}/(mm)$")
ax.set_xlabel(r"$\theta$ in °C")
ax.legend()
ax.set_title(r"$x(\theta)$-Diagramm")
# plt.show()
plt.savefig("./05_TEP/Images/TV4_x-T-Diagramm.jpg", dpi = 400)