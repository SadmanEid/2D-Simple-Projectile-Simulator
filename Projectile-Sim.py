import matplotlib.pyplot as plt
import numpy as np

# Get user inputs 
angle_deg = float(input("Enter the launch angle in degrees: "))
v0 = float(input("Enter the initial velocity (m/s): "))

# Parameters or constants 
g = 9.81                                             # gravity (m/s^2)
theta = np.radians(angle_deg)                        # convert angle to radians

#Physics calculations
t_flight = (2 * v0 * np.sin(theta)) / g              # total time of flight
height_max = (v0**2 * np.sin(theta)**2) / (2 * g)    # maximum height
if np.isclose(theta, np.pi/2):                       # check if angle is 90 degrees  
    distance = 0                                     # horizontal distance
else:
    distance = v0 * np.cos(theta) * t_flight

# Time steps
t = np.linspace(0, t_flight, num=1000)

# Initialize arrays to store position
x = np.zeros(len(t))
y = np.zeros(len(t))

# Calculate position at each time step
for i in range(len(t)):
    if np.isclose(theta, np.pi/2):                   # check if angle is 90 degrees
        x[i] = 0
    else:
        x[i] = v0 * np.cos(theta) * t[i]
    y[i] = v0 * np.sin(theta) * t[i] - 0.5 * g * t[i]**2

# Print results of things
print("Time in air: {:.2f} seconds".format(t_flight))
print("Distance traveled: {:.2f} meters".format(distance))
print("Maximum height: {:.2f} meters".format(height_max))

# Plot
plt.plot(x, y)
plt.title("Simple Flight Trajectory")
plt.xlabel("Distance (m)")
plt.ylabel("Height (m)")
plt.grid()
plt.show()

