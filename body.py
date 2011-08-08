#!/usr/bin/env python
import random
import verlet
from vector import Vector

class Body(object):
  def __init__(self, mass, pos, force):
    self.mass = float(mass)
    self.pos = pos
    self.old_pos = pos
    self.force = force

  def update(self, dt, debug=False):
    new_pos = verlet.verlet(self.pos, self.old_pos, self.force * (1 / float(self.mass)), dt)
    self.old_pos = self.pos
    self.pos = new_pos


class System(object):
  def __init__(self, width, height, n=50, max_mass=100):
    self.n = n
    self.particles = []
    self.width = width
    self.height = height
    for x in xrange(0, n):
      mass = random.random() * max_mass
      x = float(random.randint(0, width))
      y = float(random.randint(0, height))
      self.particles.append(Body(mass, Vector(x, y), Vector(0.0, 0.0)))
  
  def update(self, dt):
    grav_constant = 1.0

    for particle in self.particles:
      resultant = Vector(0.0, 0.0)
      for other in self.particles:
        if other == particle:
          continue
        else:
          dvec = particle.pos - other.pos
          dvec_ls = dvec.length_squared()
          dvec = dvec.normalized()
          resultant += dvec * (-grav_constant * (particle.mass * other.mass) / dvec_ls)
          print resultant
      particle.force = resultant

    for particle in self.particles:
      particle.update(dt, debug=True)
      if particle.pos.x < 0.0 or particle.pos.x > self.width or \
         particle.pos.y < 0.0 or particle.pos.y > self.height:
           del particle
