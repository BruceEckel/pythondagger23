def test_md5_missing():
  import os,dagger
  return dagger.hashdb.md5('tmp.missing') == None

def test_md5():
  import os,dagger
  os.system('touch tmp')
  return dagger.hashdb.md5('tmp')
  
def test_load_missing():
  import os,dagger
  d = dagger.hashdb()
  d.load(silent=True)
  return 1
  
def test_get_missing():
  import os,dagger
  d = dagger.hashdb()
  return not d.get('tmp')

def test_update():
  import os,dagger
  os.system('touch tmp')
  d = dagger.hashdb()
  d.update('tmp')
  return d.get('tmp')

def test_export():
  import os,dagger
  os.system('echo 1 > tmp1')
  os.system('echo 1 > tmp2')
  os.system('echo 2 > tmp3')
  d = dagger.hashdb('tmp.db')
  d.update('tmp1')
  d.update('tmp2')
  d.update('tmp3')
  d.export()
  del d
  
  lut = dict([x.split(',') for x in open('tmp.db').readlines()])
  
  return lut and len(lut['tmp1']) > 1 and lut['tmp1'] == lut['tmp2'] and lut['tmp1'] <> lut['tmp3']

def test_load():
  import os,dagger
  d = dagger.hashdb('tmp.db')
  d.load()
  return d.db and len(d.db['tmp1']) > 1 and d.db['tmp1'] == d.db['tmp2'] and d.db['tmp1'] <> d.db['tmp3']

#############################################
tests = [
test_md5_missing,
test_md5,
test_load_missing,
test_get_missing,
test_update,
test_export,
test_load,
]

from tester import test
import sys
sys.exit( not test(tests=tests) )