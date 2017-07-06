import dns
import dns.resolver
tipoA=(dns.resolver.query('google.com','A'))
tipoMX=(dns.resolver.query('google.com','MX'))
tipoNS=(dns.resolver.query('google.com','NS'))
tipoAAA=(dns.resolver.query('google.com','AAAA'))
print tipoA.response
print tipoMX.response
print tipoNS.response
print tipoAAA.response






