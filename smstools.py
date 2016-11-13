
import config
import hashlib, os
from datetime import datetime

def add_phone_prefix(pn):
  if pn[0:1] == '0':
    return config.DEFAULT_CODE + pn[1:]
  return pn
  
def send_sms(to, message, prefix='sms'):
  retval = ()
  to = add_phone_prefix(to)

  out_dir = os.path.join(config.DIR_BASE, config.DIR_OUTGOING)

  now = str(datetime.now()).replace(' ', '_').replace(':', '')

  m = hashlib.md5()
  m.update(now.encode('utf-8'))

  rnd = m.hexdigest()[:8]
  fn = '%s/%s_%s_%s.sms' % (out_dir, prefix, str(now), str(rnd))

  c = 'To: %s\n\n%s' % (str(to), str(message))

  try:
    f = open(fn, 'w')
    f.write(c)
    f.close()
  except Exception as e:
    print(e)
    retval = (False)
  else:
    retval = (True, rnd, fn)

  return retval