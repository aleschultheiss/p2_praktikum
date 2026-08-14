import numpy as np
import matplotlib.pyplot as plt
from math import ceil

pAtm = 723.6
pMess = np.array([296, 274, 249, 225, 202, 169, 142])
p0 = 438

theta = np.array([89.3, 74.8, 59.0, 44.9, 29.7, 14.8, 0.5])
dTheta = 0.0003*theta + 0.1

p = pMess - p0 + pAtm

line, cov = np.polyfit(theta, p, 1, cov = True)
slope, b = line
dSlope, dB = np.sqrt(np.diag(cov))

fig, ax = plt.subplots(figsize = (7, 4.5))
ax.errorbar(theta, p, 0.5, dTheta,
            fmt='o', color='steelblue', ecolor='salmon',
            ms=3, capsize=3, label='Messdaten'
)
ax.plot(theta, slope*theta + b,
        color = "red", linestyle = "--",
        label = rf'Linearer Fit' + '\n' + 
                rf'$m = ({round(slope * 10**2)/10**2:.2f} \pm {ceil(dSlope * 10**2)/10**2})$ mmHg/°C' +
                '\n' +
                rf'$b = ({round(b * 10)/10} \pm {ceil(dB * 10)/10})$ mmHg'
)
print(-b/slope)
ax.set_ylabel(r"$p/(mmHg)$")
ax.set_xlabel(r"$\theta$ in °C")
ax.legend()
ax.set_title(r"$p(\theta)$-Diagramm")
# plt.show()
plt.savefig("./05_TEP/Images/TV2_P-T-Diagramm.jpg", dpi = 400)