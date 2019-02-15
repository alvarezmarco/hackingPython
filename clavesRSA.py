#Created on 15/02/2019
#Author: Marco Alvarez M.
#Este programa es de opensource.
#Reconocimiento-NoComercial-CompartirtIgual
#Se puede distribuir y/o modificar siempre y cuando no sean con fines comerciales.

#Script que genera una public y private key con el algoritmo de cifrado RSA a 2048 bits
#Cifra y descifra un archivo de texto.

from Crypto.PublicKey import  RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA



class generatekeys:
    
    def _init_(self):
        print("Public and Private Key RSA 2048")
         
   
    def generateprivatekey(self,key):
        try:
                              
            file=open("privatekey.pem", "w")
            #file.write(key.exportKey(passphrase=secret_code, pkcs=8))
            file.write(key.exportKey("PEM"))
            print ("RSA 2048 PRIVATE KEY SUCCESSFULLY GENERATED")
            file.close        
        except Exception as e:
            print e
            print 'Fail to generate Private Key'           
        
                
        
    def generatepublickey(self,key):
        try:
            file=open("publickey.pem", "w")
            file.write(key.publickey().exportKey("PEM"))
          #  file.write(key.publickey().exportKey(passphrase=secret_code, pkcs=8))
            print ("RSA 2048 PUBLIC KEY SUCCESSFULLY GENERATED")
            file.close     
        except Exception as e:
            print e
            print 'Fail to generate Public Key'
    
    def cifrar(self):
        try:
            mensaje= open ('textocifrar.txt','r').read()
            clavepublica=RSA.importKey(open("publickey.pem", "r").read())
            cifrado=PKCS1_OAEP.new(clavepublica)
            mensajecifrado =cifrado.encrypt(mensaje)
            filecifrado=open("archivocifrado.txt", "w")
            filecifrado.write(mensajecifrado)
            filecifrado.close
            print("The message was encrypted successfully")
        except Exception as e:
            print e
            print 'Fail to encrypt message'        
            
        
    def decifrar(self):
        try:
            mensaje=open("archivocifrado.txt", "r").read()
            clavepublica=RSA.importKey(open("privatekey.pem", "r").read())
            cifrado=PKCS1_OAEP.new(clavepublica)
            msgdescifrado =cifrado.decrypt(mensaje)
            print ("The message was decrypted successfully:", msgdescifrado)
            
             
        except Exception as e:
            print e
            print 'Fail to decrypt message'        
        
            
        
        


def main():
   
  
    llave = RSA.generate(2048)
    cifrado = generatekeys()
    cifrado.generateprivatekey(llave)
    cifrado.generatepublickey(llave)
    cifrado.cifrar()
    cifrado.decifrar()
    
    
    
    
if __name__ == "__main__":
    main()
