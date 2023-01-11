import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def fun(t, y, proj):
    velocity = y[1::2]
    weight = proj.get_weight_force()
    drag = proj.get_drag_force(velocity)
    magnus = proj.get_magnus_force(velocity)
    a_res = (weight + drag + magnus) / proj.mass
    return [y[1], a_res[0], y[3], a_res[1], y[5], a_res[2]]

class Projectile:
    def __init__(self, t, theta, v0, grav):
        self.t = t
        self.theta = np.radians(theta)
        self.v0 = v0
        self.grav = grav

        self.y0 = [0., 0., 0., self.v0 * np.cos(self.theta), 0., self.v0 * np.sin(self.theta)]

        self.mass = 0.454
        self.drag_coef = 0.5
        self.magnus_coef = 1.0
        self.air_density = 1.2
        self.radius = 0.111
        self.area = np.pi * self.radius**2
        self.beta_drag = 0.5 * self.drag_coef * self.air_density * self.area
        self.beta_magnus = 0.5 * self.magnus_coef * self.air_density * self.area * self.radius

        self.wind = np.array([0., 0., 0.])
        self.angular_velocity = np.array([0., 0., 0.])

    def get_weight_force(self):
        return np.array([0., 0., -self.mass * self.grav])

    def get_drag_force(self, velocity):
        v_rel = velocity - self.wind
        return -self.beta_drag * np.linalg.norm(v_rel) * v_rel

    def get_magnus_force(self, velocity):
        v_rel = velocity - self.wind
        return self.beta_magnus * np.cross(self.angular_velocity, v_rel) 

    def set_wind(self, wind):
        self.wind = wind

    def set_angular_velocity(self, angular_velocity):
        self.angular_velocity = angular_velocity

    def get_projectile(self):
        ts = (self.t.min(), self.t.max())
        s = solve_ivp(fun, t_span=ts, y0=self.y0, method='DOP853', t_eval=self.t, args=(self,), atol=1.e-50, rtol=1.e-12)
        return s.y[0], s.y[2], s.y[4]

if __name__ == "__main__":

    t = np.linspace(0., 5., 100)
    theta = 30.0
    v0 = 30.0
    grav = 9.8

    p = Projectile(t, theta, v0, grav)
    p.set_wind(np.array([0., 5., 0.]))
    x1, y1, z1 = p.get_projectile()

    p.set_angular_velocity(np.array([0, 0, 2 * np.pi * 5]))
    x2, y2, z2 = p.get_projectile()
    
    ax = plt.figure().add_subplot(projection='3d')
    ax.plot(x1[z1>0], y1[z1>0], z1[z1>0], '-b')
    ax.plot(x2[z2>0], y2[z2>0], z2[z2>0], '-r')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()








