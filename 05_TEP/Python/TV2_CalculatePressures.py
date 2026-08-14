import numpy as np
from texttable import Texttable
from latextable import draw_latex
from math import ceil

pAtm = 723.6
pMess = np.array([296, 274, 249, 225, 202, 169, 142])
p0 = 438

theta = np.array([89.3, 74.8, 59.0, 44.9, 29.7, 14.8, 0.5])
dTheta = 0.0003*theta + 0.1

p = pMess - p0 + pAtm

table = Texttable()
table.set_cols_dtype(['t', 't'])
table.set_cols_align(['c', 'c'])
table.add_row([r'Temperatur in °C', 'Druck in $\mathrm{mmHg}$'])
for i in range(len(pMess)):
    table.add_row([rf"${theta[i]:.2f} \pm {ceil(100*dTheta[i])/100}$", rf"${p[i]} \pm {0.5}$"])

latex_table = draw_latex(table, caption="Gemessene Drücke bei verschiedenen Temperaturen in mmHg", label="tab:IsoChorPmmHg",)
print(latex_table)