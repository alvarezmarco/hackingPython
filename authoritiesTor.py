from stem.control import Controller
import getpass
controlador = Controller.from_port(port=9151)
pw = getpass.getpass("Controller password: ")
controlador.authenticate(pw)
for ruta in controlador.get_network_statuses():
	print ruta
