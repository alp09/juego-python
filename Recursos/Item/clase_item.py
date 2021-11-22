from Recursos import Tipo
from Recursos import Recurso


class Item(Recurso):

	def __init__(self, id_item: int, nombre_item: str, tipo_item: Tipo,	puntos: int):
		"""
		Construcor de la clase Enemigo
		:param id_item: el ID del item, único y definido por la propiedad id en archivo_items.json
		:param nombre_item: el nombre del item, definido por la propiedad nombre en archivo_items.json
		:param tipo_item: el tipo del item, definido por la propiedad tipo en archivo_items.json
		:param _puntos: los puntos del item, definido por la propiedad puntos en archivo_items.json
		"""
		super().__init__(id_item, nombre_item, tipo_item)
		self._puntos = puntos

	@property
	def id(self):
		"""
		Getter de la propiedad id
		:return: devuelve el id del item
		"""
		return self._id

	@property
	def nombre(self):
		"""
		Getter del nombre del item
		:return: devuelve el nombre del item
		"""
		return self._nombre

	@property
	def tipo(self):
		"""
		Getter del tipo del item
		:return: devuelve el tipo del item
		"""
		return self._tipo

	@property
	def puntos(self):
		"""
		Getter de los puntos del item
		:return: devuelve los puntos del item
		"""
		return self._puntos