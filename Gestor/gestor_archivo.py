import json


def cargar_archivo_json(path_archivo: str):
	"""
	Deserialza el contenido del archivo objetos.json
	:param path_archivo: la direccion del archivo
	:return: el resultado de la deserialización del archivo JSON
	"""
	with open(path_archivo) as archivo:
		contenido_leido = json.load(archivo)
	return contenido_leido


def guardar_en_archivo_json(path_archivo: str, datos):
	# Todo: serializar datos y guardarlos en el path_archivo
	pass
