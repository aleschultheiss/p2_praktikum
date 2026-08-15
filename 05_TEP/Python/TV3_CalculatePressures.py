import numpy as np
from texttable import Texttable
from latextable import draw_latex

pAtm = 723.6
pMess = np.array([244, 230, 216, 204, 192, 181, 170, 160, 149, 142])
p0 = 438

kolbenPos = np.array([72, 74, 76, 78, 80, 82, 84, 86, 88, 90])

p = pMess - p0 + pAtm

table = Texttable()
table.set_cols_dtype(['t', 't'])
table.set_cols_align(['c', 'c'])
table.add_row([rf'Kolbenposition in $mm$', 'Druck in $\mathrm{mmHg}$'])
for i in range(len(pMess)):
    table.add_row([rf"${kolbenPos[i]}$", rf"${p[i]} \pm {0.5}$"])

latex_table = draw_latex(table, caption="Gemessene Drücke in mmHg während der Kompression", label="tab:ThermKompPmmHg",)
print(latex_table)