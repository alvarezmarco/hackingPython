from PyPDF2 import PdfFileReader, PdfFileWriter

def imprimirMetadatos():
      
       #Path el documento pdf para analizar
       archivoPDF=PdfFileReader(file('/root/Documents/Pyhton/Violent Python.pdf'))
       #Se obtienen los metadatos con  getDocumentInfo
       metadatos=archivoPDF.getDocumentInfo()
       
       #Se hace un recorrido por los metadatos que se obtiene
       for i in metadatos:
           # Se visualiza por pantalla
              print '[+] '+ i + ': '+metadatos[i]
              
imprimirMetadatos()             
