from abc import ABC, abstractmethod
from Recursos import Tipo


class Recurso(ABC):

	def __init__(self, id_recurso: int, nombre_recurso: str, tipo_recurso: Tipo):
		"""
		Construcor de la clase Recurso
		:param id_recurso: el id del recurso
		:param nombre_recurso: el nombre asociado al recurso
		:param tipo_recurso: el tipo del recurso, registrado en el enum Tipo
		"""
		self._id = id_recurso
		self._nombre = nombre_recurso
		self._tipo = tipo_recurso

	@property
	@abstractmethod
	def id(self):
		"""
		Getter de la propiedad id
		:return: devuelve el id del recurso
		"""

	@property
	@abstractmethod
	def nombre(self):
		"""
		Getter de la propiedad nombre
		:return: devuelve el id del recurso
		"""

	@property
	@abstractmethod
	def tipo(self):
		"""
		Getter de la propiedad tipo
		:return: devuelve el id del recurso
		"""
