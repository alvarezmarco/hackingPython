#Created on 20/12/2017
#Author: Marco Alvarez M.
#Este programa es de opensource.
#Reconocimiento-NoComercial-CompartirtIgual
#Se puede distribuir y/o moificar siempre y cuando no sean con fines comerciales.

import socket
from pymongo import MongoClient
class bannergrabbing:
    def _init_(self):
        print ('Bienvenidos grabbing')
    def scan (self, ip, port):
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((ip,port))
        s.send('GET / HTTP/1.1\nHost: google.es\n\n')
        msg =s.recv(1024)        
        s.settimeout(2)
        return msg
       
    def guardarmongo(self,ip,result):
        try:
            client = MongoClient('localhost', 27017)
            db = client.banner_g   
            collection = db.client.banner_g  
            cursor = db.collection.insert({"ip":ip,"banner":result})
            print result
            print 'Los resultados se ha guardado en  la base de datos'
            db.collection.find()
        except Exception as e:
            print e
            print 'No se ha guardado'
        


def main():
    fichero = open("/root/Desktop/ipaddress.txt", "r")
    ipaddress=fichero.readlines()   
    b=bannergrabbing()
    for ip in ipaddress:
        banner = b.scan(str(ip),80)
        b.guardarmongo(str(ip),banner)
if __name__ == "__main__":
            main()
       