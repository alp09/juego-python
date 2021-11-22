from Utils import utils
from Mapa.Sala import Sala
from Recursos.Item import interfaz_item
from Recursos.Personaje import interfaz_enemigo

# Un contador con las salas que se han creado hasta ahora. Se usa para asignar ID's a las salas
cantidad_salas_creadas = 0

# Constantes usadas para la generacion de objetos
_PROBABILIDAD_PRIMER_OBJETO = 75
_PROBABILIDAD_SEGUNDO_OBJETO = 30

# Constantes usadas para la generacion de enemigos
_PROBABILIDAD_GENERAR_MOSTRUO = 75
_PENALIZACION_MOSTRUO_GENERADO = 10
_salas_con_monstruo_consecutivas = 0


def _crear_instancia_sala(generar_enemigo: bool, cantidad_objetos: int, id_sala: int = cantidad_salas_creadas) -> Sala:
	"""
	Crea una instacia de la clase Sala con el contenido indicado
	:param id_sala: el identificador numerico de la sala
	:param generar_enemigo: un booleano que indica si la sala tendrá o no un enemigo
	:param cantidad_objetos: la cantidad de objetos que contiene la sala
	:return: La instancia de la sala creada
	"""
	# Crea los recursos necesarios segun indique los parametros y despues crea un objeto sala
	lista_enemigos = interfaz_enemigo.crear_enemigo() if generar_enemigo else None
	lista_objetos = interfaz_item.crear_items(cantidad_objetos) if cantidad_objetos > 0 else None
	nueva_sala = Sala(id_sala, lista_enemigos, lista_objetos)

	# Suma 1 a la cantidad de salas creadas
	global cantidad_salas_creadas
	cantidad_salas_creadas += 1

	return nueva_sala


def crear_sala_vacia() -> Sala:
	"""
	Crea una sala vacía, sin objetos ni enemigos
	:return: la instancia de la clase Sala
	"""
	sala_creada = _crear_instancia_sala(False, 0)
	return sala_creada


def crear_sala_aleatoria() -> Sala:
	"""
	Calcula el contenido de la sala_creada y posteriormente crea una instacion con los valores adecuados
	:return: un objeto de la clase Sala con parametros aleatorios
	"""

	# Aqui se evaluan las probabilidades de generar monstruos
	global _salas_con_monstruo_consecutivas
	_probabilidad_actual_generar_monstruo = _PROBABILIDAD_GENERAR_MOSTRUO - (_PENALIZACION_MOSTRUO_GENERADO * _salas_con_monstruo_consecutivas)
	if utils.calcular_probabilidad(_probabilidad_actual_generar_monstruo):
		generar_monstruo = True
		_salas_con_monstruo_consecutivas += 1
	else:
		generar_monstruo = False
		_salas_con_monstruo_consecutivas = 0

	# Aqui se evaluan las probabilidades de generar objetos
	cantidad_objetos_generados = 0
	if utils.calcular_probabilidad(_PROBABILIDAD_PRIMER_OBJETO):
		cantidad_objetos_generados += 1
		if utils.calcular_probabilidad(_PROBABILIDAD_SEGUNDO_OBJETO):
			cantidad_objetos_generados += 1

	sala_creada = _crear_instancia_sala(generar_monstruo, cantidad_objetos_generados)
	return sala_creada


def crear_sala_final() -> Sala:
	"""
	Crea una sala con el id_sala 'FIN' que contendrá un enemigo
	:return: la instancia de la clase Sala
	"""
	sala_creada = _crear_instancia_sala(True, 0, id_sala=-1)
	return sala_creada
