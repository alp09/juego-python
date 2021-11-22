from enum import Enum


class Tipo(str, Enum):
	"""
	Enum de Tipo String que contiene los distintos Tipos del juego
	Contiene los tipos que engloban los objetos, enemigos y habilidad del heroe.
	"""

	LUCHA = "LUCHA"
	MAGIA = "MAGIA"
	ASTUCIA = "ASTUCIA"

	def __str__(self) -> str:
		"""
		Redefine como se ejecuta el método 'toString' del enum
		:return: un string con el valor del enum
		"""
		return self.value

	@classmethod
	def validar_tipo(cls, tipo: str) -> bool:
		"""
		Valida que el string tipo este registrado en la clase Tipo
		:param tipo: el tipo a validar
		:return: True si esta registrado o False si no lo esta
		"""
		return tipo.upper() in Tipo.__members__

	@classmethod
	def valor_de(cls, valor: str):
		"""
		Devuelve el Tipo enum al que corresponde el parametro valor
		:param valor: el valor del enum que se quiere
		:return: el enum correspondiente o None si no esta registrado
		"""
		return Tipo(valor) if Tipo.validar_tipo(valor.upper()) else None

	@classmethod
	def get_tipo_defecto(cls):
		"""
		:return: Devuelve el Tipo por defecto
		"""
		return Tipo.LUCHA
