#!/usr/bin/python

__author__ = 'TRA'

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
      pass

if __name__ == '__main__':
  prog = SmsBot('RECEIVED', 'example/incoming_1.sms')
  prog.main()