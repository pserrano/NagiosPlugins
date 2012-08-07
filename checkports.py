#!/usr/bin/env python

"""
Chequeo básico de puertos por segundos para NAGIOS. Esto hace un check
de los puertos en tiempo de espera para ver el estado

Modo de uso:

checkports.py host puerto TiempoEspera

By Pablo Serrano 2012

Version 1.0

"""

import socket
import sys


def chequeo(direccion, puerto, espera):
    try:
        socket.gethostbyname(direccion)
        c = socket.create_connection((direccion, puerto), espera)
        c.close()
        print ("OK - Conexion funcional")
        sys.exit(0)
    except socket.gaierror:
        print ("Critical - Error de Dns")
        sys.exit(2)
    except socket.error:
        print ("Critical - Error de conexion")
        sys.exit(2)
    except socket.timeout:
        print ("Critical - Error de timeout")
        sys.exit(2)

host = sys.argv[1]
port = int(sys.argv[2])
timesec = int(sys.argv[3])

chequeo(host, port, timesec)
