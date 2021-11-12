from abc import ABC, abstractmethod
from Dado.clase_dado import Dado

TIPOS_PERSONAJES = {
	"LUCHA": "LUCHA",
	"MAGIA": "MAGIA",
	"ASTUCIA": "ASTUCIA",
}


class Personaje(ABC):

	@abstractmethod
	def __init__(self, id_personaje: int, nombre_personaje: str, tipo: str, cantidad_dados: int, valor_maximo_dado: int):
		"""

		:param id_personaje: el id del personaje creado
		:param nombre_personaje: el nombre del personaje
		:param tipo: el tipo del personaje
		:param cantidad_dados: la cantidad de dados de la que dispondrá el personaje
		:param valor_maximo_dado: el valor maximo de los dados del personaje
		"""
		self._id = id_personaje
		self._nombre = nombre_personaje
		self._tipo = tipo
		self._dados = []

		for i in range(cantidad_dados):
			self._dados.append(Dado(valor_maximo=valor_maximo_dado))

	@property
	def nombre(self):
		"""
		Getter del nombre del personaje
		:return: devuelve el nombre del personaje
		"""
		return self._nombre

	@property
	def tipo(self):
		"""
		Getter del tipo del personaje
		:return: devuelve el tipo del personaje. Sobrescrito por Heroe bajo el nombre "habilidad"
		"""
		return self._tipo
