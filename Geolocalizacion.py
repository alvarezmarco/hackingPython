import pygeoip
geolocalizacion = pygeoip.GeoIP('/root/Desktop/GeoLiteCity.dat')
print (geolocalizacion.country_code_by_name('uoc.edu'))
print (geolocalizacion.record_by_addr('201.218.5.2'))
print (geolocalizacion.record_by_name('espoch.edu.ec'))
       

