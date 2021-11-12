from utils import generar_numero_aleatorio
from Personaje.Enemigo.clase_enemigo import Enemigo
from Recursos.recursos import ARCHIVO_ENEMIGOS_PATH
from Gestor.gestor_archivo import cargar_archivo_json

# Una lista con los enemigos cargados del archivo enemigos.json
LISTA_ENEMIGOS = cargar_archivo_json(ARCHIVO_ENEMIGOS_PATH)

# La cantidad de enemigos que contiene LISTA_ENEMIGOS
CANTIDAD_ENEMIGOS = len(LISTA_ENEMIGOS)


def _elegir_enemigo():
	"""
	Elige un enemigo de la LISTA_ENEMIGOS
	:return: el id de los enemigos generados
	"""
	id_enemigo_elegido = generar_numero_aleatorio(maximo=(CANTIDAD_ENEMIGOS - 1))
	return id_enemigo_elegido


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


def crear_enemigo():
	"""
	Elige aleatoriamente un enemigo de la LISTA_ENEMIGOS y crea una instacia de él
	:return: Devuelve una instancia de la clase enemigo
	"""
	enemigo_elegido = _elegir_enemigo()
	enemigo_creado = _crear_instancia_enemigo(enemigo_elegido)
	return enemigo_creado
