import nmap
from pymongo import MongoClient
ports=[21,22,80,443]
totalports=len(ports)

class bannergrabbing:
    def _init_(self):
        print 'Bienvenidos a bannergrabbing'
    def scan(self,ip,port):
        results=''
        try:
            nm=nmap.PortScanner()
            results=nm.scan(ip,port)
            res=results.csv()
            print (res)
            return res
        except Exception as e:
            print e	
    def guardarmongo(self,result):
        
        try:
            client = MongoClient('localhost', 27017)
            db = client.banner_g   
            collection = db.client.banner_g     
            registroid=db.collection.insert ({"reg":result})
            { item: "envelopes", qty : 100, type: "Clasp" }
            print 'Guardadocorrectamente', result
        except Exception as e:
            print e        
        
    

def main():
    fichero = open("/root/Desktop/ipaddress.txt", "r")
    ipaddress=fichero.readlines()
    b=bannergrabbing()
    for ip in ipaddress:
        for p in ports:
            resultado=b.scan(str(ip),str(p))  
          #  b.guardarmongo(resultado)
            
if __name__ == "__main__":
    main()