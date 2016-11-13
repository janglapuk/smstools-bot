import spf, os
from email.parser import Parser

__author__ = "TRA"
__doc__ = '''Modified mount point module'''

RECEIVED = 'RECEIVED'
SENT = 'SENT'
FAILED = 'FAILED'
REPORT = 'REPORT'

class Bot(object, metaclass=spf.MountPoint):
  _runnable = False
  _program = None
  _headers = None
  _body = None
  trim = False

  def __init__(self, program):
    self._program = program
    self._runnable = self._program.event == self.bot_event
    
    self.__init()

  def __str__(self):
    return self.__class__.__name__

  def __init(self):
    self.__read_message()
    self.__run()
  
  def __read_message(self):
    if os.path.isfile(self._program.fn):
      fn = self._program.fn
      f = None

      try:
        f = open(fn, 'r')
        raw = f.read()
        self.__parse_message(raw)
        
      except Exception as e:
        print(self, 'Exception:\n', e)
      
      else:
        f.close()

  def __run(self):
    if self.is_runnable():
      self.run()

  def __parse_message(self, raw):
    parser = Parser()
    msg = parser.parsestr(raw)

    self._headers = {}
    for key in msg.keys():
      # Force all keys to lowercase
      k = key.lower() 

      self._headers[k] = msg.get(key)

    self._body = msg.get_payload()

    # Check if trim enabled and not binary body
    if self.trim and 'binary' not in self._headers.keys():
      self._body = self._body.strip()   

  def valid_event(self):
    return self.bot_event == self._program.event

  def is_runnable(self):
    return self._runnable

  def get_event(self):
    return self._program.event

  def get_headers(self):
    return self._headers

  def get_body(self):
    return self._body
