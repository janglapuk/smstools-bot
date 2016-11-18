#!/usr/bin/python

__author__ = 'TRA'

import sys, os
import mount_point
import spf

all_plugins = spf.load_plugins()

class SmsBot:
  bot_plugins = spf.ExtensionsAt(mount_point.Bot)

  def __init__(self, event, fn):
    self.event = event
    self.fn = fn

  def main(self):
    for plugin in self.bot_plugins:
      retval = plugin.is_runnable()
      print(plugin, '=> runnable and loaded!')

if __name__ == '__main__':
  if len(sys.argv) < 3:
    print('Usage: %s <[SENT|RECEIVED|FAILED|REPORT]> <path/to/sms/file>' % (sys.argv[0]))
    exit(-1)

  if not os.path.isfile(sys.argv[2]):
    print('File \'%s\' is not exist.' % (sys.argv[2]))
    exit(-2)

  event = sys.argv[1]
  file  = sys.argv[2]
  
  prog  = SmsBot(event, file)
  prog.main()

  exit(0)