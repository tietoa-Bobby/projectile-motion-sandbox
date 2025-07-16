"""
simulation.py - Physics calculations for projectile motion
"""
import math

class ProjectileSimulation:
    """
    Simulates 2D projectile motion with optional linear air resistance.
    """
    def __init__(self, velocity, angle_deg, gravity=9.81, air_resistance=False):
        self.v0 = velocity
        self.angle = math.radians(angle_deg)
        self.g = gravity
        self.air = air_resistance
        self.reset()

    def reset(self):
        self.t = 0.0
        self.x = 0.0
        self.y = 0.0
        self.vx = self.v0 * math.cos(self.angle)
        self.vy = self.v0 * math.sin(self.angle)
        self.trajectory = [(self.t, self.x, self.y, self.vx, self.vy)]

    def step(self, dt=0.02):
        """
        Advance the simulation by dt seconds.
        Returns: (t, x, y, vx, vy)
        """
        if self.air:
            # Simple linear drag: F_drag = -k*v (k is arbitrary small constant)
            k = 0.1
            ax = -k * self.vx
            ay = -self.g - k * self.vy
        else:
            ax = 0
            ay = -self.g
        self.vx += ax * dt
        self.vy += ay * dt
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.t += dt
        self.trajectory.append((self.t, self.x, self.y, self.vx, self.vy))
        return self.t, self.x, self.y, self.vx, self.vy

    def is_active(self):
        """
        Returns True if the projectile is above the ground (y >= 0 metres).
        """
        return self.y >= 0

    def get_trajectory(self):
        """
        Returns the list of (t, x, y, vx, vy) tuples for the trajectory (all in SI units, metres and seconds).
        """
        return self.trajectory 