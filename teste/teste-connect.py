#!/usr/bin/env python2.7
import signal
import time
import os
import subprocess
import smtplib
from contextlib import contextmanager

def criaconnect():
    os.system('echo "connect()">connect-default.py')
def sendemail(from_addr, to_addr_list, cc_addr_list,
              subject, message,
              smtpserver='10.10.0.128:25'):
    header  = 'From: %s' % from_addr+'\n'
    header += 'To: %s' % ','.join(to_addr_list)+'\n'
    header += 'Cc: %s' % ','.join(cc_addr_list)+'\n'
    header += 'Subject: %s' % subject+'\n'
    message = header + message
 
    server = smtplib.SMTP(smtpserver)
    problems = server.sendmail(from_addr, to_addr_list, message)
    server.quit()
def connect(WLST):
    criaconnect()    
    if os.system(WLST+' connect-default.py') == 0:
        message='Weblogic Connect !'
        print(message)
        sendemail(from_addr    = 'fagundes@cedae.com.br', 
          to_addr_list = ['ricky@cedae.com.br'],
          cc_addr_list = [], 
          subject      = message, 
          message      = message)
    else:
        message='Weblogic not Connect ! Starting...'        
        print(message)
        sendemail(from_addr    = 'fagundes@cedae.com.br', 
          to_addr_list = ['ricky@cedae.com.br'],
          cc_addr_list = [], 
          subject      = message, 
          message      = message)
        startweblogic()

WLST = '/u01/middleware/wls12c/oracle_common/common/bin/wlst.sh'
connect(WLST)