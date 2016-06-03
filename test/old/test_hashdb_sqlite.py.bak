def fwrite(txt, fn): open(fn,'w').write(txt)

def rm(fn):
  import os
  try: os.remove(fn)
  except: pass
  
def test_load_missing():
  import dagger
  d = dagger.hashdb_sqlite()
  d.load(silent=True)
  return 1

def test_get_missing():
  import dagger
  d = dagger.hashdb_sqlite()
  return not d.get('tmp')

def test_update():
  import dagger
  f = 'tmp.sqlite'
  rm(f)

  fwrite('','tmp')

  d = dagger.hashdb_sqlite(f)
  d.load()
  d.update('tmp')
  h1 = d.get('tmp'); #print h1
  d.export()
  
  fwrite('stuff','tmp')
  d.load()
  d.update('tmp')
  h2 = d.get('tmp'); #print h2
  
  return h1 and h2 and (h1 <> h2)

def test_load_memory():
  import dagger
  f = 'tmp.sqlite'
  rm(f)

  fwrite('','tmp')
  
  d = dagger.hashdb_sqlite(f)
  d.load()
  d.update('tmp')
  d.export()
  del d
  
  d = dagger.hashdb_sqlite(f, True)
  d.load()
  h = d.get('tmp'); #print h
  return h and len(h[0]) > 10

def test_export():
  import dagger
  f1 = 'tmp1'
  f2 = 'tmp2'
  f3 = 'tmp3'
  fwrite('1',f1)
  fwrite('1',f2)
  fwrite('3',f3)
  
  f = 'tmp.sqlite'
  rm(f)
  
  d = dagger.hashdb_sqlite(f)
  d.load()
  d.update(f1)
  d.update(f2)
  d.update(f3)
  d.export()
  del d
  
  d = dagger.hashdb_sqlite(f)
  d.load()

  h1 = d.get(f1)
  h2 = d.get(f2)
  h3 = d.get(f3); #print h1,h2,h3
  
  return d.db and h1 and h1 == h2 and h1 <> h3

def test_export_memory():
  import dagger
  f1 = 'tmp1'
  f2 = 'tmp2'
  f3 = 'tmp3'
  fwrite('1',f1)
  fwrite('1',f2)
  fwrite('3',f3)
  f = 'tmp.sqlite'
  rm(f)
  
  d = dagger.hashdb_sqlite(f, True)
  d.load()
  d.update(f1)
  d.update(f2)
  d.update(f3)
  d.export()
  del d
  
  d = dagger.hashdb_sqlite(f, True)
  d.load()

  h1 = d.get(f1)
  h2 = d.get(f2)
  h3 = d.get(f3); #print h1,h2,h3
  
  return d.db and h1 and h1 == h2 and h1 <> h3

#############################################
tests = [
test_load_missing,
test_get_missing,
test_update,
test_export,
test_load_memory,
test_export_memory,
]

from tester import test
import sys
sys.exit( not test(tests=tests) )
