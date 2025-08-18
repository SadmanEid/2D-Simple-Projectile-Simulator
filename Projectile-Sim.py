import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


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
t = np.linspace(0, t_flight)

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
fig, ax = plt.subplots()
ax.set_title("Simple Flight Trajectory")
ax.set_xlabel("Distance (m)")
ax.set_ylabel("Height (m)")
ax.grid()
line, = ax.plot([], [], lw=2)

# Initialization and update functions for animation
def init():
    ax.set_xlim(0, distance * 1.1 if distance > 0 else 10)
    ax.set_ylim(0, height_max * 1.2 if height_max > 0 else 10)
    line.set_data([], [])
    return line,

def update(frame):
    line.set_data(x[:frame], y[:frame])
    return line,

ani = FuncAnimation(fig, update, frames=len(t), init_func=init, blit=True, interval=20)

# Show the animation
plt.show()
