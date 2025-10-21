import numpy as np
def throw_rock(m, v0, theta):
        degree = theta
        g = 9.81  # in m/s^2
        theta = theta * np.pi / 180  # in rad.
        tf = 2 * v0 * np.sin(theta) / g  # in s
        hm = v0 ** 2 * np.sin(theta) ** 2 / (2 * g)  # in m
        R = v0 ** 2 * np.sin(2 * theta) / g  # in m
        vh = v0 * np.cos(theta)  # in m/s
        Kh = 1 / 2 * m * vh * hm ** 2  # in j

        return (
            f"For a rock with {m:.3f} kg mass thrown with {v0:.3f} m/s at angle of {degree:.2f} degrees:\n"
            f"Time of flight is {tf:.1e} seconds.\n"
            f"The range in x-direction is {R:.1e} m.\n"
            f"Maximum height is {hm:.1e} m.\n"
            f"The speed at maximum height is {vh:.1e} m/s.\n"
            f"Kinetic energy at the maximum height is {Kh:.2e} J"
        )


print(throw_rock(1.5,0.3,35.20))