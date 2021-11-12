class Sala:

	def __init__(self, id_sala: int, enemigo_sala: list = None, objetos_sala: list = None):
		self._id_sala = id_sala
		self._esta_explorada = False
		self._enemigo = enemigo_sala
		self._objetos = [] if objetos_sala is None else objetos_sala

	@property
	def id(self):
		"""
		Getter del id de la sala
		:return: Devuelve el id de la sala
		"""
		return self._id_sala

	@property
	def esta_explorada(self):
		"""
		Getter de la propiedad esta_explorada
		:return: Devuelve True o False, dependiendo si la sala esta explorada o no
		"""
		return self._esta_explorada

	@property
	def enemigo(self):
		"""
		Getter del enemigo
		:return: Devuelve el enemigo que hay en la sala de haberlo o None
		"""
		return self._enemigo

	@property
	def objetos(self):
		"""
		Getter de los objetos de la sala
		:return: Devuelve una lista de objetos de la sala de haberlos o None si no se generaron objetos
		"""
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
