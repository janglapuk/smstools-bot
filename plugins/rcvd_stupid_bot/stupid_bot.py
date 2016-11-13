
__author__ = 'TRA'

import mount_point as mp
import smstools as st
import re

class StupidBot(mp.Bot):
  # This bot for RECEIVED only
  bot_event = mp.RECEIVED

  # Trim message body from unnecessary L/R spaces
  trim = True

  def run(self):
    headers = self.get_headers()
    body = self.get_body()

    # Balance check
    balance = body.lower() == '!cekpulsa'

    # Format: !bulk 0541234123[,1234,321] Message 
    bulk = re.search(r'(\!bulk)\s([0-9,]+)\s(.*)$', body, re.I|re.M)

    if balance:
      # Balance check
      self.balance_check()  
    elif bulk:
      # Bulk format
      self.bulk_sms(bulk.groups())
    else:
      # Forward to registered number for unformatted messages
      self.forward_sms(body)

  def balance_check(self):
    s = st.send_sms('555', 'PULSA', 'balance')
    print('balance_check', s)

  def bulk_sms(self, groups):
    addresses = groups[1].split(',')
    message = groups[2]
    
    for address in addresses:
      if address == '':
        # Skip wrong address
        continue 

      print(address)
    pass

  def forward_sms(self, body):
    pass