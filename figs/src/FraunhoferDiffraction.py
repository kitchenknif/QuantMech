import numpy as np
import matplotlib.pyplot as plt

I0 = 1
d = 2
h = 50
lam = 1
theta = np.linspace(-1,1,1000)

x = []
for th in theta:
    if th < 0:
        x.append(-np.sqrt(h*np.abs(np.tan(th))))
    else:
        x.append(np.sqrt(h*np.abs(np.tan(th))))

I = I0 * np.sinc((d * np.pi)/lam * np.abs(np.sin(theta)))

plt.plot(x, I)
plt.savefig("fraunhofer.eps")
plt.show()