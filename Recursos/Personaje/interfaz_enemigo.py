from Utils import utils
from Archivos import path
from Gestor import gestor_archivo
from Recursos import Tipo
from Recursos.Personaje import Enemigo

# Una lista con los enemigos cargados del archivo archivo_enemigos.json
LISTA_ENEMIGOS = gestor_archivo.cargar_archivo_json(path.PATH_ARCHIVO_ENEMIGOS)

# La cantidad de enemigos que contiene LISTA_ENEMIGOS
CANTIDAD_ENEMIGOS = len(LISTA_ENEMIGOS)


def _elegir_enemigo():
	"""
	Elige un enemigo de la LISTA_ENEMIGOS
	:return: el id de los enemigos generados
	"""
	id_enemigo_elegido = utils.generar_numero_aleatorio(maximo=(CANTIDAD_ENEMIGOS - 1))
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
		tipo_enemigo=Tipo.valor_de(datos_enemigo["tipo"]),
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
