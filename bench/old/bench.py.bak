# Hall of Fame
#
# 960799 nodes
# 6.22s Run allpaths=None levels=7 cross=0 hash=None width=7

import optparse, time

import sys
from os.path import normpath, dirname, join
daggerpath = '../src'
local_module = normpath( join(dirname(__file__), daggerpath) )
sys.path.insert(0, local_module)
import dagger
 
def GetOpt():
  desc = """Benchmark graph evaluation."""
  parser = optparse.OptionParser(description=desc)

  parser.add_option('-a', '--allpaths', help="Find all paths in graph.", action="store_true")
  parser.add_option('--dot', help='Output dot graph file to visualize.')
  parser.add_option('--cross', help='Cross dependencies so inner nodes parent all node in next level.', action="store_true")
  parser.add_option('--hash', help='Use text based hash db.', action="store_true")
  parser.add_option('--hashsql', help='Use sqlite hash db.', action="store_true")
  parser.add_option("-l", "--levels", help="How many levels to make mock graph tree.", default='2')
  parser.add_option('-w', '--width', help='How many children a node should have.', default='2')
  opts, args = parser.parse_args()
  opts = vars(opts)
  
  return opts

######################################################################
def children(p, width):
  """Return list of child ids for parent id p."""
  i0 = (p+1)*width
  i1 = i0 + width
  return range(i0,i1)
  
######################################################################
def otherchildren(p, levels, width):
  existing = children(p, width)
  
  pseries = [sum([width**i for i in xrange(1,lev+1)]) for lev in xrange(1,levels+1)]
  
  lev = 1
  # Find level node p is in.
  for z in pseries:
    if p < z: break
    lev += 1

  if lev >= len(pseries): return []
  
  # Choose other children.
  out = []
  for i in xrange(pseries[lev-1], pseries[lev]):
    if i not in existing: out.append(i)
    
  return out
  
######################################################################
opt = GetOpt()
allpaths = opt.get('allpaths')
hash = opt.get('hash')
hashsql = opt.get('hashsql')
cross = opt.get('cross')
levels = int( opt.get('levels') )
dot = opt.get('dot')
width = int( opt.get('width') )

tBuild, tRun = 0,0

#---------------------------------------------------------------------
# Build basic graph.
tic = time.clock()
dag = dagger.dagger()

nInner = sum([width**i for i in xrange(1,levels)])
nOuter = width**levels # Leaves.
print 'nodes: inner=%s outer=%s total=%s' % (str(nInner), str(nOuter), str(nInner+nOuter))

# Add nodes with children.
for p in xrange(0,nInner):
  dag.add( str(p), map(str, children(p, width)) )

# Force last node stale to get side effects.
dag.stale(str(nInner+nOuter-1))

# Add optional cross links so graph isn't simple k-trees.
if cross:
  for p in xrange(0,nInner):
    other = otherchildren(p, levels, width)
    dag.add( str(p), map(str, other) )

toc = time.clock()
tBuild = toc - tic

#---------------------------------------------------------------------
tic = toc
dag.run(allpaths=allpaths)

toc = time.clock()
tRun = toc - tic

#---------------------------------------------------------------------
print '%ss Build allpaths=%s levels=%s cross=%s hash=%s width=%s' % ( str(tBuild), str(allpaths), str(levels), str(cross), str(hash), str(width) ) 

print '%ss Run allpaths=%s levels=%s cross=%s hash=%s width=%s' % ( str(tBuild), str(allpaths), str(levels), str(cross), str(hash), str(width) ) 

if dot: dag.dot(dot)
