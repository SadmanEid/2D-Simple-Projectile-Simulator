import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

#---------------------
#The Physics Engine 
#---------------------


def simulate_flight(
    initial_velocity: float, 
    launch_angle_degrees: float, 
    object_mass: float, 
    object_radius: float, 
    time_step: float = 0.01
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:

    """
    Calculates the trajectory of a projectile experiencing aerodynamic drag.
    
    Arguements of the function:
        initial_velocity: The starting speed of the object in m/s.
        launch_angle_degrees: The angle of launch relative to the ground.
        object_mass: Mass of the object in kilograms.
        object_radius: Radius of the spherical object in meters.
        time_step: The time increment for the simulation loop in seconds.
        
    Returns:
        A tuple containing three numpy arrays: X positions, Y positions, and time stamps.
    """
    # Environment constants
    gravity_acceleration = 9.81
    air_density = 1.225
    drag_coefficient = 0.47
    cross_sectional_area = np.pi * (object_radius ** 2)
    launch_angle_radians = np.radians(launch_angle_degrees)

    # Calculate starting velocities for X and Y axes
    velocity_x = initial_velocity * np.cos(launch_angle_radians)
    velocity_y = initial_velocity * np.sin(launch_angle_radians)

    # Lists to record the flight path
    positions_x = [0.0]
    positions_y = [0.0]
    time_stamps = [0.0]

    # Run the simulation until the object hits the ground
    while positions_y[-1] >= 0:
        current_speed = np.sqrt(velocity_x**2 + velocity_y**2)
        
        if current_speed == 0: 
            break

        # Calculate forces and resulting acceleration (Newton's Second Law: a = F/m)
        drag_force_magnitude = 0.5 * air_density * (current_speed**2) * drag_coefficient * cross_sectional_area
        
        acceleration_x = -(drag_force_magnitude * (velocity_x / current_speed)) / object_mass
        acceleration_y = -gravity_acceleration - (drag_force_magnitude * (velocity_y / current_speed)) / object_mass

        # Step forward in time to find the new velocity
        velocity_x += acceleration_x * time_step
        velocity_y += acceleration_y * time_step
        
        # Calculate where the object will be next
        next_position_x = positions_x[-1] + velocity_x * time_step
        next_position_y = positions_y[-1] + velocity_y * time_step

        # Interpolation Logic to ensure the object doesn't go below ground level
        if next_position_y < 0:
            fraction_of_step_needed = positions_y[-1] / (positions_y[-1] - next_position_y)
            final_ground_position_x = positions_x[-1] + (velocity_x * time_step * fraction_of_step_needed)
            
            positions_x.append(final_ground_position_x)
            positions_y.append(0.0)
            time_stamps.append(time_stamps[-1] + (time_step * fraction_of_step_needed))
            break

        # Save standard frame data
        positions_x.append(next_position_x)
        positions_y.append(next_position_y)
        time_stamps.append(time_stamps[-1] + time_step)

    return np.array(positions_x), np.array(positions_y), np.array(time_stamps)


#---------------------
#The Graph Gui
#---------------------
def animate_trajectory(trajectory_x: np.ndarray, trajectory_y: np.ndarray) -> None:
    """Renders an animated plot of the provided X and Y coordinates."""
    
    fig, ax_plot = plt.subplots()
    ax_plot.set_title("Realistic Flight Trajectory")
    ax_plot.set_xlabel("Distance (m)")
    ax_plot.set_ylabel("Height (m)")
    ax_plot.grid(True)

    # Set window limits dynamically based on the flight path size
    ax_plot.set_xlim(0, max(trajectory_x) * 1.1)
    ax_plot.set_ylim(0, max(trajectory_y) * 1.1)

    animated_line, = ax_plot.plot([], [], 'r-', lw=2)

    def initialize_animation():
        animated_line.set_data([], [])
        return animated_line,

    def update_animation_frame(frame_index: int):
        # We use frame_index + 1 to ensure the final ground contact point is drawn
        animated_line.set_data(trajectory_x[:frame_index+1], trajectory_y[:frame_index+1])
        return animated_line,

    animation_object = FuncAnimation(
        fig, 
        update_animation_frame, 
        frames=len(trajectory_x), 
        init_func=initialize_animation, 
        interval=10, 
        blit=True, 
        repeat=False
    )
    plt.show()


#-----------------------------------------
#The User Inputs and Simulation Execution
#-----------------------------------------  
if __name__ == "__main__":
    print("--- Projectile Simulator ---")
    
    # Collect inputs
    launch_angle = float(input("Launch angle (degrees): "))
    launch_velocity = float(input("Initial velocity (m/s): "))
    projectile_mass = float(input("Mass (kg): "))
    projectile_radius = float(input("Radius (m): "))

    # Execute simulation
    x_data, y_data, time_data = simulate_flight(launch_velocity, launch_angle, projectile_mass, projectile_radius)

    # Display console results
    print(f"\nTime in air: {time_data[-1]:.2f} seconds")
    print(f"Distance traveled: {x_data[-1]:.2f} meters")
    print(f"Maximum height: {max(y_data):.2f} meters")

    # Launch graphical animation
    animate_trajectory(x_data, y_data)
