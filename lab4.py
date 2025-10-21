import numpy as np

def throw_rock(m, v0, theta):
    g = 9.81  # in m/s^2
    theta_rad = np.radians(theta)  # Convert degrees to radians

    # Calculations
    tf = (2 * v0 * np.sin(theta_rad)) / g  # Time of flight (s)
    hm = (v0**2 * np.sin(theta_rad)**2) / (2 * g)  # Max height (m)
    R = (v0**2 * np.sin(2 * theta_rad)) / g  # Range (m)
    vh = v0 * np.cos(theta_rad)  # Velocity at max height (m/s)
    Kh = 0.5 * m * vh**2  # Kinetic energy at max height (J)

    # Print results
    print(f"For a rock with {m:.3f} kg mass thrown with {v0:.3f} m/s at an angle of {theta:.2f} degrees:")
    print(f"Time of flight is    {tf:.1e} s")
    print(f"The range in x-direction is    {R:.1e} m")
    print(f"Maximum height is    {hm:.1e} m")
    print(f"The speed at maximum height is    {vh:.2e} m/s")
    print(f"Kinetic energy at the maximum height is {Kh:.2e} J")

    # Return all calculated values
    return tf, R, hm, vh, Kh