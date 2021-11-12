from Personaje.clase_personaje import Personaje

CANTIDAD_DADOS_DEFECTO = 2              # La cantidad de dados que tiene el heroe por defecto
VALOR_MAXIMO_DADO = 25                  # El valor maximo del dado usado por defecto


class Enemigo(Personaje):

	def __init__(
			self,
			id_enemigo: int,
			nombre_enemigo: str,
			tipo_enemigo: str,
			poder_enemigo: int,
			cantidad_dados: int = CANTIDAD_DADOS_DEFECTO,
			valor_maximo: int = VALOR_MAXIMO_DADO):
		"""
		Construcor de la clase Enemigo
		:param id_enemigo: el ID del enemigo, único y definido por la propiedad id en enemigos.json
		:param nombre_enemigo: el nombre del enemigo, definido por la propiedad nombre en enemigos.json
		:param tipo_enemigo: el tipo del enemigo, definido por la propiedad tipo en enemigos.json
		:param poder_enemigo: el poder/fuerza del enemigo, definido por la propiedad poder en enemigos.json
		:param cantidad_dados: la cantidad de dados que tendra (POR DEFECTO USA CANTIDAD_DADOS_DEFECTO)
		:param valor_maximo: para el rango de valores 1-valor_maximo (POR DEFECTO USA VALOR_MAXIMO_DADO)
		"""
		super().__init__(id_enemigo, nombre_enemigo, tipo_enemigo, cantidad_dados, valor_maximo)
		self._poder = poder_enemigo

	@property
	def poder(self):
		"""
		Getter del poder del enemigo
		:return: Devuelve el poder del enemigo, que será restado a los puntos_vida del heroe cuando pierda
		"""
		return self._poder
