import numpy as np
import matplotlib.pyplot as plt

# Example: simple CSTR reaction simulation
F_in = 1.0  # mol/s
V = 10.0    # L
k = 0.1     # 1/s

# Steady-state conversion
X = np.linspace(0, 1, 100)
C_A = F_in * (1 - X) / V

plt.figure()
plt.plot(X, C_A)
plt.xlabel('Conversion')
plt.ylabel('Concentration of A (mol/L)')
plt.title('CSTR Conversion vs Concentration')
plt.grid(True)
plt.show()
