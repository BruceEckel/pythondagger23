def test_add(): 
  import os, dagger
  os.system('touch tmp tmp.1')
  n1 = dagger.node('tmp')
  n2 = dagger.node('tmp.1')
  n1.add(n2)
  
  return len(n1.nodes)

def test_format_abs(): 
  import os, dagger
  os.system('touch tmp')
  n = dagger.node('tmp')
  
  # Should return '*/tmp'.
  s = n.format('%a'); #print s
  return len(s) > 4

def test_format_date(): 
  import os, dagger
  os.system('touch tmp')
  n = dagger.node('tmp')
  
  # Should return 'yyyy-mm-dd'.
  s = n.format('%d'); #print s
  return len(s) > 8

def test_format_time(): 
  import os, dagger
  os.system('touch tmp')
  n = dagger.node('tmp')
  
  # Should return 'hh:mm:ss'.
  s = n.format('%t'); #print s
  return len(s) > 6

def test_format_base(): 
  import os, dagger
  os.system('touch tmp.1')
  n = dagger.node('tmp.1')
  
  s = n.format('%b'); #print s
  return s == 'tmp.1'

def test_format_base_dot(): 
  import os, dagger
  os.system('touch .tmp')
  n = dagger.node('.tmp')
  
  s = n.format('%b'); #print s
  return s == '.tmp'

def test_format_root(): 
  import os, dagger
  os.system('touch tmp.1')
  n = dagger.node('tmp.1')
  
  s = n.format('%r'); #print s
  return s == 'tmp'

def test_format_root_dot(): 
  import os, dagger
  os.system('touch .tmp')
  n = dagger.node('.tmp')
  
  s = n.format('%r'); #print s
  return s == '.tmp'

def test_update_time(): 
  import os, dagger
  os.system('touch tmp')
  n = dagger.node('tmp')
  
  n.update(time=True, hash=False)
  return n.time > 0

def test_update_hash(): 
  import os, dagger
  os.system('touch tmp')
  n = dagger.node('tmp')
  
  n.update(time=False, hash=True); #print n.hash
  return n.hash
  
def test_missing_is_stale():
  import os, dagger
  os.system('touch tmp1')
  n1 = dagger.node('tmp1')
  n1.update()

  n2 = dagger.node('tmp_missing')
  n2.update()

  return n1.stale == None and n2.stale
  
#############################################
tests = [
test_add,
test_format_abs,
test_format_date,
test_format_time,
test_format_base,
test_format_base_dot,
test_format_root,
test_format_root_dot,
test_update_time,
test_update_hash,
test_missing_is_stale,
]

from tester import test
import sys
sys.exit( not test(tests=tests) )