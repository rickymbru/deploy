#!/usr/bin/env python2.7
import signal
import time
import os
import subprocess
import smtplib
from contextlib import contextmanager

class TimeoutException(Exception): pass

@contextmanager
def time_limit(seconds):
    def signal_handler(signum, frame):
        raise TimeoutException("Timed out!")
    signal.signal(signal.SIGALRM, signal_handler)
    signal.alarm(seconds)
    try:
        yield
    finally:
        signal.alarm(0)

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

def startweblogic():
    DOMAIN_HOME = os.environ.get('DOMAIN_HOME')
    STARTWEBLOGIC='nohup '+ DOMAIN_HOME +'/bin/startWebLogic.sh > /dev/null 2>&1 &'
    os.system(STARTWEBLOGIC)

def killweblogic(PORT):
    COMMAND_PID='netstat -ltnp 2>/dev/null| grep -w '+ PORT +' | awk \'{print $7}\' | cut -d \'/\' -f 1'
    PROC = subprocess.Popen([COMMAND_PID], stdout=subprocess.PIPE, shell=True) 
    OLDPID=""
    for PID in PROC.stdout:
        if OLDPID != PID:
            COMMAND_KILL='kill -9 '+PID
            os.system(COMMAND_KILL)
        OLDPID = PID    

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

# Variaveis
WLST = '/u01/middleware/wls12c/oracle_common/common/bin/wlst.sh'
PORT = '7001'

try:
    with time_limit(20):        
        connect(WLST)
except TimeoutException as e:
    message='Weblogic Timout! Killing and starting...'
    print(message)
    sendemail(from_addr    = 'fagundes@cedae.com.br', 
        to_addr_list = ['ricky@cedae.com.br'],
        cc_addr_list = [], 
        subject      = message, 
        message      = message)    
    killweblogic(PORT)
    startweblogic() 