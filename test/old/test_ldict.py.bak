def test_all(): 
  import dagger
  
  a = [1,2,3,4]
  d = dagger.ldict(a)
  if not d.head or d.head.data <> 1: return 0
  if not d.tail or d.tail.data <> 4: return 0

  for x in a:
    if not d.get(x) or d.get(x).data <> x: return 0
  
  for x,y,z in [ [1,2,4], [3,2,4], [4,2,2], [999,2,2] ]:
    d.remove(x)
    if not d.head or d.head.data <> y: return 0
    if not d.tail or d.tail.data <> z: return 0

  d.remove(2)
  if d.head: return 0
  if d.tail: return 0
  
  return True
  
#############################################
tests = [
test_all,
]

from tester import test
import sys
sys.exit( not test(tests=tests) )
