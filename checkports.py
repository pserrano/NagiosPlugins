#!/usr/bin/env python

"""
Checkports.py : Basic check port for nagios
By Pablo Serrano 2012

Version 1.1

"""
import socket
import sys


def chequeo(direccion, puerto, espera):
    try:
        socket.gethostbyname(direccion)
        c = socket.create_connection((direccion, puerto), espera)
        c.close()
        print ("OK - Connection GOOD!")
        sys.exit(0)
    except socket.gaierror:
        print ("Critical - DNS Error")
        sys.exit(2)
    except socket.error:
        print ("Critical - Connection Error")
        sys.exit(2)
    except socket.timeout:
        print ("Critical - Timeout Error")
        sys.exit(2)
#Program start here
if sys.argv[1].startswith('--'):
    option = sys.argv[1][2:]
    # fetch sys.argv[1] but without the first two characters
    if option == 'version':
            print ("Version 1.1")
    elif option == 'help':
            print ("""\
This program makes basic check port
Usage:
     
     checkports.py host port Timewait
      
     ex: checkports.py google.com 80 5

Other options include:
  --version : Prints the version number
  --help    : Display this help""")
    else:
        print ("Unknown option. Try --help")
    sys.exit(3)
else:
    host = sys.argv[1]
    port = int(sys.argv[2])
    timesec = int(sys.argv[3])

chequeo(host, port, timesec)
