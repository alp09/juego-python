import random
from Archivos import path
from Gestor import gestor_archivo
from Recursos.Item import Item

# Una lista con los items cargados del archivo archivo_items.json
LISTA_ITEMS = gestor_archivo.cargar_archivo_json(path.PATH_ARCHIVO_ITEMS)

# La cantidad de items que contiene LISTA_itemS
CANTIDAD_ITEMS = len(LISTA_ITEMS)


def _elegir_items(cantidad: int) -> list[int]:
	"""
	Genera aleatoriamente id's de los items (sin duplicados)
	:param cantidad: la cantidad de items que se quiere.
	:return: los id's de los items generados
	"""
	id_items_disponibles = [item["id"] for item in LISTA_ITEMS]
	random.shuffle(id_items_disponibles)
	return id_items_disponibles[0:cantidad:]


def _crear_instancia_item(id_item: int) -> Item:
	"""
	Genera una instacia de la clase Item a partir del id del item
	:param id_item: el id del item del que se quiere crear una instancia
	:return: la instancia del item
	"""
	datos_item = LISTA_ITEMS[id_item]
	item_creado = Item(
		datos_item["id"],
		datos_item["nombre"],
		datos_item["tipo"],
		datos_item["puntos"]
	)
	return item_creado


def crear_items(cantidad: int = 1) -> list[Item]:
	"""
	Devuelve una lista que contiene instancias de la clase item
	:param cantidad: la cantidad de instancias que se quiere de la clase item. No puede ser mayor que CANTIDAD_itemS
	:return: una lista con los items creados (mínimo 1 item)
	"""
	cantidad = 1 if cantidad < 0 else min(cantidad, CANTIDAD_ITEMS)
	id_items_elegidos = _elegir_items(cantidad)
	items_creados = [_crear_instancia_item(id_item) for id_item in id_items_elegidos]
	return items_creados
