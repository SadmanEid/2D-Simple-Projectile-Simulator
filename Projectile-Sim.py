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
t = np.linspace(0, t_flight, 1000)

# Initialize arrays to store position
x = []
y = []

# Calculate position until projectile lands
for i, ti in enumerate(t):
    xi = v0 * np.cos(theta) * ti if not np.isclose(theta, np.pi/2) else 0
    yi = v0 * np.sin(theta) * ti - 0.5 * g * ti**2
    if yi < 0:
# Interpolate to find more accurate landing point at y=0 instead of stopping at negative height
        if i > 0:
            x0, y0 = x[-1], y[-1]
            x1, y1 = xi, yi
            frac = -y0 / (y1 - y0)
            x_ground = x0 + frac * (x1 - x0)
            x.append(x_ground)
            y.append(0)
        break
    x.append(xi)
    y.append(yi)

x = np.array(x)
y = np.array(y)
    
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

ani = FuncAnimation(fig, update, frames=len(x), init_func=init, interval=0.5, blit=True, repeat=False)

# Show the animation
plt.show()
