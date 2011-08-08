#!/usr/bin/env python
from vector import Vector

def verlet(cur_pos, old_pos, acc, dt):
  retval = (cur_pos * 2) - old_pos +  (acc * (dt**2.0))
  print "cur_pos = %s, old_pos = %s, new_pos = %s, acc = %s" % (cur_pos, old_pos, retval, acc)
  return retval

def main():
  cur_pos = Vector(0.0, 0.0)
  old_pos = Vector(0.0, 0.0)
  acc = Vector(0.5, 0.5)
  timestep = 0.001
  steps = 1000

  for x in xrange(0, steps):
    new_pos = verlet(cur_pos, old_pos, acc, timestep)
    print "%f\t%s" % (x*timestep, new_pos)
    old_pos = cur_pos
    cur_pos = new_pos

if __name__ == "__main__":
  main()
