#!/usr/bin/env python2.7
import smtplib
 
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

sendemail(from_addr    = 'fagundes@cedae.com.br', 
          to_addr_list = ['ricky@cedae.com.br'],
          cc_addr_list = [], 
          subject      = 'Sucess', 
          message      = 'Howdy from a python function')
