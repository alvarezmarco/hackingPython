# Este script consulta los registros DNS sobre IPv4 (del tipo A), IPv6 (del tipo AAAA),
# Name Serveres (NS), MailServers (MX)\
# Uso python informacionDNS.py -d nombredeldominio
# Ejemplo python informacionDNS.py -d nombredeldominio
# Autor: Marco Alvarez Murillo.

import dns
import dns.resolver
import argparse

def resolverdns (dom):
  try:
    
     tipoA=(dns.resolver.query(dom,'A'))
     tipoMX=(dns.resolver.query(dom,'MX'))
     tipoNS=(dns.resolver.query(dom,'NS'))
     tipoAAA=(dns.resolver.query(dom,'AAAA'))
     
     print tipoA.response
     print tipoMX.response
     print tipoNS.response
     print tipoAAA.response
  
  except Exception, e:
    print (e)

def main ():
    try:
     parser = argparse.ArgumentParser()
     
     #Se define el argumento a ingresar por consola, en este cado d y dominio
     parser.add_argument("-d", "--dominio" ,help="Ingresar un nombre de dominio")
     
     #Se pueden incluir mas opciones en est caso -a para ayuda.
     parser.add_argument("-a", "--ayuda", help="", action="store_true" )
     #Se pasan todos los argumentos a args.
     args = parser.parse_args()
     
     #Se comprueba si se el usuario escoge -d.
     if args.dominio :
        domin=args.dominio
        resolverdns(domin)
    
     # Ayuda HELP.
     if args.ayuda :
           print("Uso:  [OPTIONS]")
           print ("   -d Ingresar un nombre de dominio. Ex: python informacionDNS.py -d google.es ")
           print ("   -a Ayuda.")
    except Exception, e:
      print (e)  
if __name__ == "__main__":
  main()