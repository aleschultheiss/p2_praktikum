import numpy as np

values = [1.095, 1.105, 1.055, 1.125, 1.085, 1.125, 1.080, 
          1.125, 1.120, 1.130, 1.095, 1.135, 1.115, 1.115, 
          1.080, 1.115]

mean = np.mean(values)
mean = np.round(mean, 3)
sigma = np.std(values, ddof = 1) #Standardabweichung einer Stichprobe mit Besselscher Korrektur
error = sigma / np.sqrt(len(values))
error = np.round(error, 3)
print(f"\hat{{U}}_{{\mathrm{{ind}}}} = {mean} \pm {error}")
