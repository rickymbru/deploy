#!/usr/bin/env python2.7
import subprocess
import sys
import re
import os
import signal
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
if __name__ == '__main__':

    try:
        with time_limit(10):
            connect() 
    except TimeoutException as e:
        print("Timed out!")        



    DOMAIN_HOME=os.environ['DOMAIN_HOME']
    STARTWEBLOGIC='nohup ' +DOMAIN_HOME+ '/bin/startWebLogic.sh &'
    COMMAND_PID='netstat -ltnp 2>/dev/null| grep -w 7001 | grep :1 | awk \'{print $7}\' | cut -d \'/\' -f 1'
    PID = arch = subprocess.check_output(COMMAND_PID, shell=True);
    print(PID)
    COMMAND_KILL='kill -9 '+PID
    
    # Matar processo do Weblogic
    #os.system(COMMAND_KILL)

    # Iniciar Weblogic
    #os.system(STARTWEBLOGIC)
