from json import dumps


class Objeto:

	def __init__(self, id_objecto: int, nombre_objecto: str, tipo_objeto: str, puntos_objeto: int):
		"""
		Constructor de la clase Objeto
		:param id_objecto: el id del objeto, único y definido por la propiedad id en objetos.json
		:param nombre_objecto: el nombre del objeto, definido por la propiedad nombre en objetos.json
		:param tipo_objeto: el tipo del objeto, definido por la propiedad tipo en objetos.json
		:param puntos_objeto: los puntos del objeto, definido por la propiedad puntos en objetos.json
		"""
		self._id = id_objecto
		self._tipo = tipo_objeto
		self._nombre = nombre_objecto
		self._puntos = puntos_objeto

	@property
	def tipo(self):
		"""
		Getter del tipo del objeto
		:return: Devuelve el tipo del objeto
		"""
		return self._tipo

	@property
	def nombre(self):
		"""
		Getter del nombre del objeto
		:return: Devuelve el nombre del objeto
		"""
		return self._nombre

	@property
	def puntos(self):
		"""
		Getter de los puntos del objeto
		:return: Devuelve los puntos del objeto
		"""
		return self._puntos

	def toJson(self):
		"""
		Parsea a JSON el objeto
		:return: devuelve un String del objeto en JSON
		"""
		return dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
