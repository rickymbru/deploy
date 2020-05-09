#!/usr/bin/env python2.7
import smtplib
import os


def send(FROM, TO, MESSAGE):
    COMMAND = 'echo '+MESSAGE+'| mailx -s '+MESSAGE+' -r '+FROM+' '+TO
    os.system(COMMAND)

send('fagundes@cedae.com.br','ricky@cedae.com.br','SUCESS')