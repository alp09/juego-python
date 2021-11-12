from json import dumps
from utils import generar_numero_aleatorio


class Dado:

	def __init__(self, valor_minimo: int = 1, valor_maximo: int = 6):
		"""
		El constructor de la clase dado
		:param valor_minimo: el valor minimo que se puede obtener en una tirada
		:param valor_maximo: el valor maximo que se puede obtener en una tirada
		"""
		self._minimo = valor_minimo
		self._maximo = valor_maximo
		self._valor = self.lanzar_dados()

	@property
	def valor(self):
		"""
		Getter del valor actual del dado
		:return: Devuelve el valor de la ultima tirada
		"""
		return self.valor

	def toJson(self):
		"""
		Parsea a JSON el objeto
		:return: devuelve un String del objeto en JSON
		"""
		return dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

	def lanzar_dados(self):
		"""
		Genera un nuevo numero aleatorio entre _minimo y _maximo
		:return: Devuelve el nuevo valor del dado
		"""
		self._valor = generar_numero_aleatorio(self._minimo, self._maximo)
		return self._valor
