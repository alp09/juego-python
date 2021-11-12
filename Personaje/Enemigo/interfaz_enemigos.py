from utils import generar_numero_aleatorio
from Personaje.Enemigo.clase_enemigo import Enemigo
from Recursos.recursos import ARCHIVO_ENEMIGOS_PATH
from Gestor.gestor_archivo import cargar_archivo_json

# Una lista con los enemigos cargados del archivo enemigos.json
LISTA_ENEMIGOS = cargar_archivo_json(ARCHIVO_ENEMIGOS_PATH)

# La cantidad de enemigos que contiene LISTA_ENEMIGOS
CANTIDAD_ENEMIGOS = len(LISTA_ENEMIGOS)


def _elegir_enemigo(cantidad: int = 1):
	"""
	Elige enemigos de la LISTA_ENEMIGOS (permite duplicados)
	:param cantidad: la cantidad de id de enemigos que se quiere generar
	:return: los id's de los enemigos generados
	"""
	cantidad = 1 if cantidad < 0 else min(cantidad, CANTIDAD_ENEMIGOS)
	id_enemigos_elegidos = []
	for i in range(cantidad):
		id_enemigos_elegidos.append(generar_numero_aleatorio(maximo=(CANTIDAD_ENEMIGOS - 1)))
	return id_enemigos_elegidos


def _crear_instancia_enemigo(id_enemigo: int):
	"""
	Genera una instacia de la clase Enemigo a partir del id del enemigo
	:param id_enemigo: el id del enemigo del que se quiere crear una instancia
	:return: la instancia del enemigo
	"""
	datos_enemigo = LISTA_ENEMIGOS[id_enemigo]
	enemigo_creado = Enemigo(
		id_enemigo=id_enemigo,
		nombre_enemigo=datos_enemigo["nombre"],
		tipo_enemigo=datos_enemigo["tipo"],
		poder_enemigo=datos_enemigo["poder"]
	)
	return enemigo_creado


def crear_enemigos(cantidad: int = 1):
	"""
	Devuelve una lista que contiene instancias de la clase enemigo
	:param cantidad: la cantidad de instancias que se quiere de la clase enemigo
	:return: una lista con los enemigos creados
	"""
	cantidad = 1 if cantidad < 0 else min(cantidad, CANTIDAD_ENEMIGOS)
	enemigos_elegidos = _elegir_enemigo(cantidad)
	enemigos_creados = []
	for enemigo in enemigos_elegidos:
		enemigos_creados.append(_crear_instancia_enemigo(enemigo))
	return enemigos_creados
