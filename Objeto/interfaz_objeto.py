import random
from Objeto.clase_objeto import Objeto
from Recursos.recursos import ARCHIVO_OBJETOS_PATH
from Gestor.gestor_archivo import cargar_archivo_json

# Una lista con los objetos cargados del archivo objetos.json
LISTA_OBJETOS = cargar_archivo_json(ARCHIVO_OBJETOS_PATH)

# La cantidad de objetos que contiene LISTA_OBJETOS
CANTIDAD_OBJETOS = len(LISTA_OBJETOS)


def _elegir_objetos(cantidad: int):
	"""
	Genera aleatoriamente id's de los objetos (sin duplicados)
	:param cantidad: la cantidad de objetos que se quiere.
	:return: los id's de los objetos generados
	"""
	id_objetos_disponibles = [objeto["id"] for objeto in LISTA_OBJETOS]
	random.shuffle(id_objetos_disponibles)
	return id_objetos_disponibles[0:cantidad:]


def _crear_instancia_objeto(id_objeto: int):
	"""
	Genera una instacia de la clase Objeto a partir del id del objeto
	:param id_objeto: el id del objeto del que se quiere crear una instancia
	:return: la instancia del objeto
	"""
	datos_objeto = LISTA_OBJETOS[id_objeto]
	objeto_creado = Objeto(
		id_objecto=datos_objeto["id"],
		nombre_objecto=datos_objeto["nombre"],
		tipo_objeto=datos_objeto["tipo"],
		puntos_objeto=datos_objeto["puntos"]
	)
	return objeto_creado


def crear_objetos(cantidad: int = 1):
	"""
	Devuelve una lista que contiene instancias de la clase objeto
	:param cantidad: la cantidad de instancias que se quiere de la clase objeto. No puede ser mayor que CANTIDAD_OBJETOS
	:return: una lista con los objetos creados (mínimo 1 objeto)
	"""
	cantidad = 1 if cantidad < 0 else min(cantidad, CANTIDAD_OBJETOS)
	id_objetos_elegidos = _elegir_objetos(cantidad)
	objetos_creados = []
	for id_objeto in id_objetos_elegidos:
		objetos_creados.append(_crear_instancia_objeto(id_objeto))
	return objetos_creados
