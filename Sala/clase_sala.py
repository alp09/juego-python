class Sala:

	def __init__(self, enemigos_sala: list = None, objetos_sala: list = None):
		self._esta_explorada = False
		self._enemigos = [] if enemigos_sala is None else enemigos_sala
		self._objetos = [] if objetos_sala is None else objetos_sala

	@property
	def esta_explorada(self):
		return self._esta_explorada

	@property
	def enemigos(self):
		return self._enemigos

	@property
	def objetos(self):
		return self._objetos

	def coger_objeto(self, indice_objeto: int):
		"""
		Metodo usado para recoger objetos de la sala y actualizar la lista _objetos de la misma
		:param indice_objeto: el objeto que se quiere coger
		:return: si el indice es valido, devuelve el objeto almacenado en self._objetos[indice_objeto], sino devuelve None
		"""
		objeto_cogido = None
		if 0 <= indice_objeto < len(self._objetos):
			objeto_cogido = self._objetos.pop(indice_objeto)
		return objeto_cogido
