import numpy as np
from texttable import Texttable
from latextable import draw_latex
from math import ceil

alpha = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 90])
_beta = np.array([268.0, 286.0, 307.0, 322.5, 340.0, 356.0, 370.5, 384.0, 396.0, 407.5])
dalpha = 2
dbeta = 1
beta = _beta - 268.0
phi = alpha - beta
dphi = np.sqrt(dalpha**2 + dbeta**2)


table = Texttable()
table.set_cols_dtype(['t', 't', 't'])
table.set_cols_align(['c', 'c', 'c'])
table.add_row(['$\\alpha$ in $^{\\circ}$', '$\\beta$ in $^{\\circ}$', '$\\varphi$ in $^{\\circ}$'])
for i in range(len(alpha)):
    table.add_row([f"${alpha[i]:.1f} \pm {ceil(dalpha * 10) / 10:.1f}$", f"${beta[i]:.1f} \pm {ceil(dbeta * 10) / 10:.1f}$", f"${phi[i]:.1f} \pm {ceil(dphi * 10) / 10:.1f}$"])

latex_table = draw_latex(table, caption="Berechnete Winkel", label="tab:angles")
print(latex_table)

print("\nBerechnete Winkel:")
print(f"alpha = np.array({alpha})")
print(f"phi = np.array({phi})")