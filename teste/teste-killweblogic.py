import os
import subprocess

def killweblogic(PORT):
    COMMAND_PID='netstat -ltnp 2>/dev/null| grep -w '+ PORT +' | awk \'{print $7}\' | cut -d \'/\' -f 1'
    PROC = subprocess.Popen([COMMAND_PID], stdout=subprocess.PIPE, shell=True) 
    OLDPID=""
    for PID in PROC.stdout:
        if OLDPID != PID:
            COMMAND_KILL='kill -9 '+PID
            os.system(COMMAND_KILL)
        OLDPID = PID

killweblogic('7001')