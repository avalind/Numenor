#!/usr/bin/env python
import pygame
from pygame.locals import *

import body
from vector import Vector

black = [0, 0, 0]
white = [255, 255, 255]

def setup():
  pygame.init()
  screen = pygame.display.set_mode((640, 480))
  clock = pygame.time.Clock()
  pygame.display.set_caption("Verlet Integration")
  return (screen, clock)

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
    render_system(scr, s)
    pygame.display.flip()
    timer.tick(20)

if __name__ == "__main__":
  main()
