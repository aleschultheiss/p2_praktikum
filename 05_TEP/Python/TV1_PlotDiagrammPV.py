import numpy as np
import matplotlib.pyplot as plt
from math import ceil

pAtm = 723.6
pMess = np.array([438, 417, 400, 380, 366, 350, 334, 322, 309, 296])
p0 = 438

kolbenPos = np.array([72, 74, 76, 78, 80, 82, 84, 86, 88, 90])

p = pMess - p0 + pAtm
dp = 0.5
yVals = pAtm/p
yErr = yVals * dp/p

line, cov = np.polyfit(kolbenPos, yVals, 1, cov = True)
slope, b = line
dSlope, dB = np.sqrt(np.diag(cov))

fig, ax = plt.subplots(figsize = (7, 4.5))
ax.errorbar(kolbenPos, yVals, yErr,
            fmt='o', color='steelblue', ecolor='salmon',
            ms=3, capsize=3, label='Messdaten'
)
ax.plot(kolbenPos, slope*kolbenPos + b,
        color = "red", linestyle = "--",
        label = rf'Linearer Fit, $m = ({round(slope * 10**5)/10**5:.5f} \pm {ceil(dSlope * 10**5)/10**5})$ mm'
)
ax.set_ylabel(r"$p_0/p$")
ax.set_xlabel(r"Kolbenposition x/mm ($=V/(A_{\mathrm{grund}} \cdot \mathrm{mm}$))")
ax.legend()
ax.set_title(r"$\frac{p_{atm}}{p}(x)$-Diagramm")
plt.savefig("./05_TEP/Images/TV1_DiagrammP0-P-x-Diagramm.jpg", dpi = 400)