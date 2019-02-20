import nmap
from pymongo import MongoClient

class scanNmap():
          def _init_(self):
                    print 'Bienvenidos a bannergrabbing'
          def savemongo(self,ipv4, nport, nstate,nreason,nportstate, nproducto, ninfoproducto):
                        
                    
                    try:
                              client = MongoClient('localhost', 27017)
                              
                              db = client.banner_g   
                              collection = db.client.banner_g 
                              registroid=db.collection.insert ({"IP":ipv4,"Port":nport, "State": nstate, "Reason": nreason, "Port State": nportstate, "Product":nproducto, "InfoProduct":ninfoproducto})
                              
                              print 'Save successfull'
                    except Exception as e:
                              print e        


          
          
          def parsediccionario(self,diccionario, ip):      
                    try:
                              
                              for host in diccionario.all_hosts():
                                        nmapHost = diccionario[host]
                                    #    print nmapHost
                                        if diccionario[host].has_key ('status'):
                                                  nmapState = diccionario[host]['status']['state']
                                                  nmapReason = diccionario[host]['status']['reason']  
                                                 # print   nmapState
                                                 # print nmapReason                                                  
                                                  for protocol in ["tcp","udp", "icmp"]:
                                                            if diccionario[host].has_key (protocol):
                                                                      ports=diccionario[host][protocol].keys()                                                                     
                                                                      for port in ports:
                                                                                
                                                                                nmapPort = port
                                                                                nmapPortState= diccionario[host][protocol][port]['state'] 
                                                                                nmapProducto= diccionario[host][protocol][port]['product'] 
                                                                                nmapInfoProducto= diccionario[host][protocol][port]['extrainfo']
                                                                                self.savemongo(ip,nmapPort,nmapState,nmapReason,nmapPortState, nmapProducto, nmapInfoProducto)
                                                                                print ip, nmapPort,nmapState,nmapReason,nmapPortState, nmapProducto, nmapInfoProducto
                                                                                print 
                                                                                print
                                                                      
                                                                      
                                                                                                                                         
                                                                      
                                                            
                                                  
                                                  
                                                  
                              
                             
                    except Exception as e:
                              print e	          



def main():
          
          file1= open("/root/Desktop/ipaddress.txt", "r")
          file2=open("/root/Desktop/ports.txt", "r")
          ipaddress = file1.readlines()
          ports = file2.readlines()
          scanner=scanNmap()          
          for ip in ipaddress:
                    for p in ports:
                              nm=nmap.PortScanner()
                              nm.scan(str(ip),str(p))
                              scanner.parsediccionario(nm,str(ip))
                              
                             
                             
          
if __name__ == "__main__":
          main()



