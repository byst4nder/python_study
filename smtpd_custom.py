#encoding:utf-8

import smtpd
import asyncore

class CustomSMTPServer(smtpd.SMTPServer):
    def process_message(self,peer,mailfrom,rcpttos,data):
        print 'Receiving mssage from:',peer
        print 'Message address from:',mailfrom
        print 'Message addressed to :',rcpttos
        print 'Message length :',len(data)
        return

server=CustomSMTPServer(('127.0.0.1',1025),None)
asyncore.loop()
