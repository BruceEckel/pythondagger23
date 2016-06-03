def delete(files):
  import os
  if type(files) not in [type([]),type(())]:
    files = [files]
    
  for f in files:
    try: os.remove(f)
    except: pass
  
def fill(files, text=''):
  """Write text to all files listed."""
  for f in files: fh = open(f,'w'); fh.write(text); fh.close()
  
def touch(names, t=None):
  """Set (future) atime/mtime per file name."""
  import os,time
  if type(names) not in [type([]),type(())]:
    names = [names]
  
  if t==None:
    t = time.time() + 1
    
  for n in names:
    if not os.path.exists(n): fill(n)
    os.utime(n, (t,t))
  
def paths_equal(dag, names, truth):
  """Check if each node has paths in truth dict."""
  for name in names:
    n = dag.get(name)
    if not n.paths:
      if n.paths <> truth[name]: return False
    elif dag.pathnames(name) <> truth[name]:
      return False
      
  return True
  
def stale_dict(dag, names):
  """Create dict of stale values for just named files."""
  out = {}
  for n in names: out[n] = dag.get(n).stale
  return out
  
def test_pathnames():
  import dagger
  d = dagger.dagger()
  d.add('1', ['2','3'])
  n1 = d.get('1')
  n2 = d.get('2')
  n3 = d.get('3')
  n1.paths = [ [n2,n3] ]
  p = d.pathnames('1'); #print p
  return p and p == [['2','3']]

def test_run_order():
  """Check graph walk order."""  
  import dagger
  all = '1 2 3 4 5 6 7'.split()
  fill(all)
  
  d = dagger.dagger()
  d.add('1', ['2','3'])
  d.add('3', ['4','5'])
  d.add('6', ['3','7'])
  d.run(allpaths=False)
  names = [n.name for n in d.order.list]; #print names
  return names == '2 4 5 3 1 7 6'.split()

def test_run_paths():
  """Check graph depth-first path for each node."""
  import dagger
  d = dagger.dagger()
  d.add('1', ['2','3'])
  d.add('3', ['4','5'])
  d.add('6', ['3','7'])

  all = '1 2 3 4 5 6 7'.split()
  fill(all)
  d.run(allpaths=False)
  
  truth = {
  '1': None,
  '2':[['1']],
  '3':[['1'], ['6']],
  '4':[['3','1']],
  '5':[['3','1']],
  '6': None,
  '7':[['6']],
  }
  if not paths_equal(d, all, truth):
    return False
  
  return True

def test_run_allpaths():
  """Check all graph paths possible."""
  import dagger
  d = dagger.dagger()
  d.add('1', ['2','3'])
  d.add('3', ['4','5'])
  d.add('6', ['3','7'])

  all = '1 2 3 4 5 6 7'.split()
  fill(all)
  
  d.run(allpaths=True)
  
  truth = {
  '1': None,
  '2':[['1']],
  '3':[['1'], ['6']],
  '4':[['3','1'], ['3','6']],
  '5':[['3','1'], ['3','6']],
  '6': None,
  '7':[['6']],
  }
  if not paths_equal(d, all, truth):
    return False
  
  return True

def test_force(allpaths=False):
  """Check forcing staleness."""
  import dagger
  d = dagger.dagger()
  d.add('1', ['2','3'])
  d.add('3', ['4','5'])
  d.add('6', ['3','7'])

  all = '1 2 3 4 5 6 7'.split()
  touch(all)
  
  d.resetnodes()
  d.stale('1',1)
  d.run(allpaths=allpaths)
  truth = {'1':1, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0}
  states1 = stale_dict(d, all)
  if states1 <> truth:
    print 'states1 =',states1,'<>\ntruth   =',truth,'\n'
    return False

  touch(all)
  d.resetnodes()
  d.forced.clear()
  d.stale('2',1)
  d.run(allpaths=allpaths)
  truth = {'1':1, '2':1, '3':0, '4':0, '5':0, '6':0, '7':0}
  states2 = stale_dict(d, all)
  if states2 <> truth:
    print 'states2 =',states2,'<>\ntruth   =',truth,'\n'
    return False
  
  touch(all)
  d.resetnodes()
  d.forced.clear()
  d.stale('3',1)
  d.run(allpaths=allpaths)
  truth = {'1':1, '2':0, '3':1, '4':0, '5':0, '6':1, '7':0}
  states3 = stale_dict(d, all)
  if states3 <> truth:
    print 'states3 =',states3,'<>\ntruth   =',truth,'\n'
    return False

  touch(all)
  d.resetnodes()
  d.forced.clear()
  d.stale('5',1)
  d.run(allpaths=allpaths)
  truth = {'1':1, '2':0, '3':1, '4':0, '5':1, '6':1, '7':0}
  states4 = stale_dict(d, all)
  if states4 <> truth:
    print 'states4 =',states4,'<>\ntruth   =',truth,'\n'
    return False
  
  return True

def test_force_allpaths():
  return test_force(allpaths=1)
  
def test_time(allpaths=False):
  """Check stale when file timestamps are old."""
  import dagger
  d = dagger.dagger()
  d.add('1', ['2','3'])
  d.add('3', ['4','5'])
  d.add('6', ['3','7'])
  
  all = '1 2 3 4 5 6 7'.split()
  fill(all)
  touch(all,0)
  touch('1')

  d.run(allpaths=allpaths)
  truth = {'1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0}
  states1 = stale_dict(d, all)
  if states1 <> truth: 
    print 'states1 =',states1,'<>\ntruth   =',truth,'\n'
    return False
  
  touch(all,0)
  touch('2')

  d.resetnodes()
  d.run(allpaths=allpaths)
  truth = {'1':1, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0}
  states2 = stale_dict(d, all)
  if states2 <> truth:
    print 'states2 =',states2,'<>\ntruth   =',truth,'\n'
    return False
  
  touch(all,0)
  touch('3')

  d.resetnodes()
  d.run(allpaths=allpaths)
  truth = {'1':1, '2':0, '3':0, '4':0, '5':0, '6':1, '7':0}
  states3 = stale_dict(d, all)
  if states3 <> truth:
    print 'states3 =',states3,'<>\ntruth   =',truth,'\n'
    return False

  touch(all,0)
  touch('4')

  d.resetnodes()
  d.run(allpaths=allpaths)
  truth = {'1':1, '2':0, '3':1, '4':0, '5':0, '6':1, '7':0}
  states4 = stale_dict(d, all)
  if states4 <> truth:
    print 'states4 =',states4,'<>\ntruth   =',truth,'\n'
    return False

  touch(all,0)
  touch('5')

  d.resetnodes()
  d.run(allpaths=allpaths)
  truth = {'1':1, '2':0, '3':1, '4':0, '5':0, '6':1, '7':0}
  states5 = stale_dict(d, all)
  if states5 <> truth:
    print 'states5 =',states5,'<>\ntruth   =',truth,'\n'
    return False

  touch(all,0)
  touch('6')
  
  d.resetnodes()
  d.run(allpaths=allpaths)
  truth = {'1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0}
  states6 = stale_dict(d, all)
  if states6 <> truth:
    print 'states6 =',states6,'<>\ntruth   =',truth,'\n'
    return False

  touch(all,0)
  touch('7')

  d.resetnodes()
  d.run(allpaths=allpaths)
  truth = {'1':0, '2':0, '3':0, '4':0, '5':0, '6':1, '7':0}
  states7 = stale_dict(d, all)
  if states7 <> truth:
    print 'states7 =',states7,'<>\ntruth   =',truth,'\n'
    return False

  return True
  
def test_time_allpaths():
  return test_time(allpaths=1)

def test_hash_missing(): 
  """Check stale when file hashes missing."""
  import dagger
  d = dagger.dagger('tmp.missing')
  d.hashall = True
  d.add('1', ['2','3'])
  d.add('3', ['4','5'])
  d.add('6', ['3','7'])

  all = '1 2 3 4 5 6 7'.split()
  fill(all)

  d.run()
  truth = {'1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0}
  states = stale_dict(d, all)
  if states <> truth:
    print states,'<>\n',truth,'\n'
    return False

  return 1

def test_hash(): 
  """Check stale when file hashes change."""
  import dagger
  all = '1 2 3 4 5 6 7'.split()
  fill(all,'')
  
  db = dagger.hashdb('tmp.db')
  for f in all: db.update(f)
  db.export()

  fill(['5'], 'test')
  
  d = dagger.dagger('tmp.db')
  d.hashall = True
  d.add('1', ['2','3'])
  d.add('3', ['4','5'])
  d.add('6', ['3','7'])
  
  d.run()
  truth = {'1':1, '2':0, '3':1, '4':0, '5':1, '6':1, '7':0}
  states1 = stale_dict(d, all)
  if states1 <> truth:
    print 'states1 =',states1,'<>\ntruth   =',truth,'\n'
    return False

  return 1
  
def test_dot():
  """Test exporting dot graph file."""
  import dagger
  d = dagger.dagger()
  d.add('1', ['2','3'])
  d.add('3', ['4','5'])
  d.add('6', ['3','7'])
  
  all = '1 2 3 4 5 6 7'.split()
  fill(all)
  touch(all,0)
  touch('5')

  f = 'tmp.dot'
  d.run()
  d.dot(out=f, color=1)
  
  import os
  if not os.path.exists(f): return False
  text = open(f).read()
  return ('1 [fillcolor = "#ff' in text) and ('3 [fillcolor = "#ff' in text) and ('6 [fillcolor = "#ff' in text) and ('5 [fillcolor = white]' in text)
  
def test_phony():
  """Make a missing file phony and make sure nothing is stale."""
  import dagger
  d = dagger.dagger()
  d.add('1', ['2','3'])
  d.add('3', ['4','5'])
  d.add('6', ['3','7'])
  d.phony('3')
  
  all = '1 2 3 4 5 6 7'.split()
  touch(all,0)
  delete('3')
  d.run()
  
  truth = {'1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0}
  states1 = stale_dict(d, all)
  if states1 <> truth:
    print 'states1 =',states1,'<>\ntruth   =',truth,'\n'
    return False
  
  return 1
  
def test_phony_force_stale():
  """Make a missing file phony and force it to stale."""
  import dagger
  d = dagger.dagger()
  d.add('1', ['2','3'])
  d.add('3', ['4','5'])
  d.add('6', ['3','7'])
  d.phony('3')
  
  all = '1 2 3 4 5 6 7'.split()
  touch(all,0)
  delete('3')
  d.stale('3')
  d.run()
  
  truth = {'1':1, '2':0, '3':1, '4':0, '5':0, '6':1, '7':0}
  states1 = stale_dict(d, all)
  if states1 <> truth:
    print 'states1 =',states1,'<>\ntruth   =',truth,'\n'
    return False

  d = dagger.dagger()
  d.add('1', ['2','3'])
  d.add('3', ['4','5'])
  d.add('6', ['3','7'])
  d.phony('3')
  
  all = '1 2 3 4 5 6 7'.split()
  touch(all,0)
  delete('3')
  d.stale('4')
  d.run()
  
  truth = {'1':1, '2':0, '3':1, '4':1, '5':0, '6':1, '7':0}
  states1 = stale_dict(d, all)
  if states1 <> truth:
    print 'states1 =',states1,'<>\ntruth   =',truth,'\n'
    return False

  return 1
  
def test_phony_time():
  """Make a missing file phony and ensure stale by stale child (that had older child)."""
  import dagger
  d = dagger.dagger()
  d.add('1', ['2','3'])
  d.add('3', ['4','5'])
  d.add('6', ['3','7'])
  d.phony('6')
  
  all = '1 2 3 4 5 6 7'.split()
  touch(all,0)
  touch('4',1)
  d.run()
  
  truth = {'1':1, '2':0, '3':1, '4':0, '5':0, '6':1, '7':0}
  states1 = stale_dict(d, all)
  if states1 <> truth:
    print 'states1 =',states1,'<>\ntruth   =',truth,'\n'
    return False

  return 1
  
def test_phony_hash():
  """Make a missing file phony and ensure stale by stale child (that had old hash)."""
  import dagger
  all = '1 2 3 4 5 6 7'.split()
  fill(all,'')
  
  db = dagger.hashdb('tmp.db')
  for f in all: db.update(f)
  db.export()

  fill(['4'], 'test')
  
  d = dagger.dagger('tmp.db')
  d.hashall = True
  d.add('1', ['2','3'])
  d.add('3', ['4','5'])
  d.add('6', ['3','7'])
  d.phony('6')
  d.run()
  
  truth = {'1':1, '2':0, '3':1, '4':1, '5':0, '6':1, '7':0}
  states1 = stale_dict(d, all)
  if states1 <> truth:
    print 'states1 =',states1,'<>\ntruth   =',truth,'\n'
    return False

  return 1
  
#############################################
tests = [
test_pathnames,
test_run_order,
test_run_paths,
test_run_allpaths,
test_force,
test_force_allpaths,
test_time,
test_time_allpaths,
test_hash_missing,
test_hash,
test_dot,
test_phony,
test_phony_force_stale,  
test_phony_time,
test_phony_hash,
]

from tester import test
import sys
if __name__=='__main__':
  sys.exit( not test(tests=tests) )
