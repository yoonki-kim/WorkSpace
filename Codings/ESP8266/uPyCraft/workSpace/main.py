# main.py -- put your code here!
import os
import localwifi
#import ftpd.uftpd as ftp
import ftpd.ftp as ftp

localwifi.connect()
#ftp.start()
ftp.ftpserver()    # ftpd.ftp
