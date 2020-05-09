import os
import subprocess

def killweblogic(PORT):
    COMMAND_PID='netstat -ltnp 2>/dev/null| grep -w '+ PORT +' | grep :1 | awk \'{print $7}\' | cut -d \'/\' -f 1'
    PID = arch = subprocess.check_output(COMMAND_PID, shell=True);
    COMMAND_KILL='kill -9 '+PID    
    os.system(COMMAND_KILL)

killweblogic('7001')