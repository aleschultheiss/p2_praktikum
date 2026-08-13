import numpy as np
import matplotlib.pyplot as plt

temp = [12.68, 10.45, 9.27, 8.05, 7.11, 5.90, 4.88, 3.99, 3.46, 2.82, 2.62, 2.47, 0.61, 0.27, -0.10, -0.18, 0.83, 0.85, 0.03, -0.66, -1.03, -1.60, -1.70, -1.80, -0.11, -0.05]
times = [0, 5, 10, 15, 20, 30, 40, 50, 60, 90, 120, 150, 180, 200, 240, 250, 300, 360, 420, 480, 510, 540, 600, 630, 645, 660]

fig, ax = plt.subplots(figsize=(7, 4.5))
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.set_ylabel('Temperatur in °C')
ax.set_xlabel('Zeit in s')

plt.plot(times, temp, 'o:r', label = "Gemessene Temperatur")
plt.vlines(150, -3, 13, 'grey', linestyles=':')
plt.text(150, -4, 'Rühren 1', ha = 'center', size = 7)
plt.vlines(250, -3, 13, 'grey', linestyles=':')
plt.text(250, -4, 'Rühren 2', ha = 'center', size = 7)
plt.vlines(360, -3, 13, 'grey', linestyles=':')
plt.text(360, -4, 'Rühren 3', ha = 'center', size = 7)
plt.vlines(630, -3, 13, 'orange')
plt.text(630, -4, 'Kratzen am Glas', ha = 'center', size = 7)
plt.savefig("./04_APW/Images/TV3_TempVerlaufDiag.jpg", dpi = 800)