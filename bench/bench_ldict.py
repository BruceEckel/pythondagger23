import time
import sys
sys.path.append('../dagger')
import dagger

if len(sys.argv) > 1:
  n = int(sys.argv[1])
else:
  n = 100000

a = list(range(n))
d = dagger.ldict(a)

tic = time.time()
while d.head:
  d.remove(d.head.data)

toc = time.time()
print(toc-tic)