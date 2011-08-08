#!/usr/bin/env python
import pygame
from pygame.locals import *

import body
from vector import Vector

white = [0, 0, 0]
black = [255, 255, 255]

def setup():
  pygame.init()
  screen = pygame.display.set_mode((640, 480))
  clock = pygame.time.Clock()
  pygame.display.set_caption("Verlet Integration")
  return (screen, clock)

def transform(world, width, height):
  """
    Maps world cordinates to screen.
  """
  return Vector(world.x + (width/2.0),
                world.y + (height/2.0))

def render_system(screen, s):
  for particle in s.particles:
    pos = particle.pos
    pygame.draw.circle(screen, black, (pos.x, pos.y), 2)

def main():
  scr, timer = setup()
  timestep = 0.01
  s = body.System(width=640, height=480, n=20, max_mass=1e5)
  print s.particles
  while True:
    scr.fill(white)
    for event in pygame.event.get():
      if event.type == QUIT:
        return
      if event.type == MOUSEBUTTONDOWN:
        print event.pos
    
    s.update(timestep)
    #b.force *= dampening
    #b.update(timestep)
    #paint = transform(b.pos, 640, 480)
    #print paint
    render_system(scr, s)
    #pygame.draw.circle(scr, black, (paint.x, paint.y), 5)
    pygame.display.flip()
    timer.tick(20)

if __name__ == "__main__":
  main()
