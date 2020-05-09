import subprocess
import signal
import os
from datetime import datetime as dt

process_name="java"
PORT='7001'
COMMAND_PID='netstat -ltnp 2>/dev/null| grep -w '+ PORT +' | awk \'{print $7}\' | cut -d \'/\' -f 1'
proc = subprocess.Popen([COMMAND_PID], stdout=subprocess.PIPE, shell=True) 
for pid in proc.stdout:
    print(pid)