import json


def cargar_archivo_json(path_archivo: str):
	"""
	Deserialza el contenido del archivo archivo_items.json
	:param path_archivo: la direccion del archivo
	:return: el resultado de la deserialización del archivo JSON
	"""
	with open(path_archivo) as archivo:
		contenido_leido = json.load(archivo)
	return contenido_leido


def guardar_en_archivo_json(path_archivo: str, datos):
	"""
	Toma los datos pasados por parametros, los parsea a JSON y posteriormente lo guarda en el archivo indicado
	:param path_archivo: el archivo donde se quiere guardar
	:param datos: los datos que se quieren serializar
	"""
	with open(path_archivo, 'w') as archivo:
		json.dump(datos, archivo, default=lambda o: o.__dict__, indent=4)
