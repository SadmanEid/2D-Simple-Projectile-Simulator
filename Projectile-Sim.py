import matplotlib.pyplot as plt
import numpy as np

# Parameters
g = 9.81  # gravity (m/s^2)
v0 = 50   # initial speed (m/s)
angle = 45  # launch angle in degrees
t_end = 10  # total simulation time in seconds

# Convert angle to radians
theta = np.radians(angle)

# Time steps
t = np.linspace(0, t_end, num=500)

# Equations of motion (without air resistance)
x = v0 * np.cos(theta) * t
y = v0 * np.sin(theta) * t - 0.5 * g * t**2

# Cut off where projectile hits the ground
x = x[y >= 0]
y = y[y >= 0]

# Plot
plt.plot(x, y)
plt.title("Simple Flight Trajectory")
plt.xlabel("Distance (m)")
plt.ylabel("Height (m)")
plt.grid()
plt.show()
