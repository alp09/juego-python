from Sala.clase_sala import Sala
import Personaje.Enemigo.interfaz_enemigo as interfaz_enemigo
import Objeto.interfaz_objeto as interfaz_objeto


def crear_sala(id_sala: int, generar_enemigo: bool, cantidad_objetos: int):
	"""
	Crea una instacia de la clase Sala con el contenido indicado
	:param id_sala: el identificador numerico de la sala
	:param generar_enemigo: un booleano que indica si la sala tendrá o no un enemigo
	:param cantidad_objetos: la cantidad de objetos que contiene la sala
	:return: La instancia de la sala creada
	"""
	lista_enemigos = interfaz_enemigo.crear_enemigo() if generar_enemigo else None
	lista_objetos = interfaz_objeto.crear_objetos(cantidad_objetos) if cantidad_objetos > 0 else None
	nueva_sala = Sala(id_sala, lista_enemigos, lista_objetos)
	return nueva_sala
