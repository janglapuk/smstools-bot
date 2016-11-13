
import config
import md5, os
from datetime import datetime

def send_sms(to, message, prefix='sms'):
	retval = ()

	out_dir = os.path.join(config.DIR_BASE, config.DIR_OUTGOING)

	now = str(datetime.now()).replace(' ', '_').replace(':', '')

	m = md5.new()
	m.update(now)

	rnd = m.digest().encode('hex')[:6]
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