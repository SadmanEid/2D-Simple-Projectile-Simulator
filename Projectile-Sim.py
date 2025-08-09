import matplotlib.pyplot as plt
import numpy as np

# Get user inputs
angle_deg = float(input("Enter the launch angle in degrees: "))
v0 = float(input("Enter the initial velocity (m/s): "))

# Convert angle to radians
theta = np.radians(angle_deg)

# Parameters
g = 9.81  # gravity (m/s^2)
t_end = 30  # total simulation time in seconds

# Time steps
t = np.linspace(0, t_end, num=500)

# Initialize arrays to store position
x = np.zeros(len(t))
y = np.zeros(len(t))

# Calculate position at each time step
for i in range(len(t)):
    x[i] = v0 * np.cos(theta) * t[i]
    y[i] = v0 * np.sin(theta) * t[i] - 0.5 * g * t[i]**2

# Cut off where projectile hits the ground
mask = y >= 0
x = x[mask]
y = y[mask]

# Plot
plt.plot(x, y)
plt.title("Simple Flight Trajectory")
plt.xlabel("Distance (m)")
plt.ylabel("Height (m)")
plt.grid()
plt.show()


