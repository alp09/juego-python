from Sala.clase_sala import Sala
import Personaje.Enemigo.interfaz_enemigos as interfaz_enemigo
import Objeto.interfaz_objeto as interfaz_objeto


def crear_sala(cantidad_enemigos: int, cantidad_objetos: int):
	lista_enemigos = interfaz_enemigo.crear_enemigos(cantidad_enemigos)
	lista_objetos = interfaz_objeto.crear_objetos(cantidad_objetos)
	nueva_sala = Sala(lista_enemigos, lista_objetos)
	return nueva_sala
