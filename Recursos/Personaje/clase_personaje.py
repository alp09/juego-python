from abc import ABC
from typing import Optional
from Utils import utils
from Recursos import Tipo
from Recursos import Recurso
from Recursos.Item import Item
from Recursos.Personaje.Dado import Dado


class Personaje(Recurso, ABC):

	def __init__(self, id_personaje: int, nombre_personaje: str, tipo_personaje: Tipo, cantidad_dados: int, valor_maximo_dado: int):
		"""
		Constructor de la clase abstracta personaje. Subclases -> Heroe y Enemigo
		:param id_personaje: el id del personaje creado
		:param nombre_personaje: el nombre del personaje
		:param tipo_personaje: el tipo del personaje
		:param cantidad_dados: la cantidad de dados de la que dispondrá el personaje
		:param valor_maximo_dado: el valor maximo de los dados del personaje
		"""
		super().__init__(id_personaje, nombre_personaje, tipo_personaje)
		self._dados = [Dado(valor_maximo=valor_maximo_dado) for _ in range(cantidad_dados)]

	@property
	def dados(self):
		"""
		Getter de los dados del personaje
		:return: devuelve los dados del personaje
		"""
		return self._dados


class Heroe(Personaje):

	PUNTOS_VIDA_MINIMO = 0  					# El valor minimo de puntos_vida del heroe. Al llegar a 0 estaría "muerto"
	PUNTOS_VIDA_MAXIMO = 200  					# El valor maximo de puntos_vida del heroe
	_PUNTOS_VIDA_CREACION_MINIMO = 100  		# El valor minimo de puntos_vida con los que puede iniciar el heroe
	_CANTIDAD_DADOS_DEFECTO_HEROE = 3  			# La cantidad de dados que tiene el heroe por defecto
	_VALOR_MAXIMO_DADO_HEROE = 20  				# El valor maximo del dado usado por defecto
	_ESPACIO_MAXIMO_INVENTARIO = 2              # La cantidad de items que puede guardar el heroe en su inventario

	def __init__(
			self,
			nombre_heroe: str,
			habilidad_heroe: Tipo,
			cantidad_dados: int = _CANTIDAD_DADOS_DEFECTO_HEROE,
			valor_maximo: int = _VALOR_MAXIMO_DADO_HEROE):
		"""
		Constructor del personaje Heroe, controlado por el jugador
		:param nombre_heroe: el nombre del heroe
		:param habilidad_heroe: la habilidad elegida por el heroe (DEBE ESTAR EN Recurso.TIPOS_PERSONAJES)
		:param cantidad_dados: la cantidad de dados que tendra el heroe (POR DEFECTO USA CANTIDAD_DADOS_DEFECTO)
		:param valor_maximo: para el rango de valores 1-valor_maximo (POR DEFECTO USA VALOR_MAXIMO_DADO)
		"""
		super().__init__(-1, nombre_heroe, habilidad_heroe, cantidad_dados, valor_maximo)
		self._puntos_vida = utils.generar_numero_aleatorio(Heroe._PUNTOS_VIDA_CREACION_MINIMO, Heroe.PUNTOS_VIDA_MAXIMO)
		self._inventario = []
		self._puntuacion = 0

	@property
	def id(self) -> int:
		"""
		Getter de la propiedad id
		:return: devuelve el id del heroe
		"""
		return self._id

	@property
	def nombre(self) -> str:
		"""
		Getter de la propiedad nombre
		:return: devuelve el id del heroe
		"""
		return self._nombre

	@property
	def tipo(self) -> Tipo:
		"""
		Override del getter de la propiedad tipo.
		:return: el tipo de heroe o dicho de otra forma la habilidad que se ha elegido
		"""
		return self._tipo

	@property
	def puntos_vida(self) -> int:
		"""
		Getter de la propiedad puntos_vida
		:return: devuelve los puntos_vida actuales
		"""
		return self._puntos_vida

	def modificar_puntos_vida(self, modificacion_puntos_vida) -> bool:
		"""
		Suma o resta los puntos indicados en puntos_vida
		:param modificacion_puntos_vida: la cantidad a sumar o restar de los puntos de vida actuales
		:return: los puntos_vida resultantes
		"""
		self._puntos_vida += modificacion_puntos_vida
		self._puntos_vida = max(self._puntos_vida, Heroe.PUNTOS_VIDA_MINIMO)
		self._puntos_vida = min(self._puntos_vida, Heroe.PUNTOS_VIDA_MAXIMO)
		return True if self._puntos_vida > 0 else False

	@property
	def inventario(self) -> list[Item]:
		"""
		Getter del inventario del heroe
		:return: devuelve la lista de objetos que tiene el heroe
		"""
		return self._inventario

	def guardar_en_inventario(self, nuevo_item: Item) -> bool:
		"""
		Guarda en el inventario del heroe el nuevo_item
		:return: devuelve True si se pudo guardar el item en el inventario
		"""
		# Todo: permitir que se guarden listas de Items
		hay_espacio_en_inventario = True
		if len(self._inventario) < Heroe._ESPACIO_MAXIMO_INVENTARIO:
			self._inventario.append(nuevo_item)
		else:
			hay_espacio_en_inventario = False
		return hay_espacio_en_inventario

	def descartar_de_inventario(self, indice_item_descartado) -> Optional[Item]:
		"""
		Descarta el item que se encuentre en el indice_item_descartado del inventario del heroe
		:return: devuelve el item descartado si el indice es válido
		"""
		item_descartado = None
		if self._inventario and 0 <= indice_item_descartado < len(self._inventario):
			item_descartado = self._inventario.pop(indice_item_descartado)
		return item_descartado

	@property
	def puntuacion(self) -> int:
		"""
		Getter de la propiedad puntuacion
		:return: devuelve los puntos_vida actuales
		"""
		return self._puntuacion

	def sumar_puntos_al_total(self, puntos) -> int:
		"""
		Suma o resta puntos a la puntuacion total del heroe
		:return: devuelve la puntuacion actual
		"""
		self._puntuacion += puntos
		return self._puntuacion


class Enemigo(Personaje):

	_CANTIDAD_DADOS_DEFECTO_ENEMIGO = 2  		# La cantidad de dados que tiene el heroe por defecto
	_VALOR_MAXIMO_DADO_ENEMIGO = 25  			# El valor maximo del dado usado por defecto

	def __init__(
		self,
		id_enemigo: int,
		nombre_enemigo: str,
		tipo_enemigo: Tipo,
		poder_enemigo: int,
		cantidad_dados: int = _CANTIDAD_DADOS_DEFECTO_ENEMIGO,
		valor_maximo: int = _VALOR_MAXIMO_DADO_ENEMIGO):
		"""
		Construcor de la clase Enemigo
		:param id_enemigo: el ID del enemigo, único y definido por la propiedad id en archivo_enemigos.json
		:param nombre_enemigo: el nombre del enemigo, definido por la propiedad nombre en archivo_enemigos.json
		:param tipo_enemigo: el tipo del enemigo, definido por la propiedad tipo en archivo_enemigos.json
		:param poder_enemigo: el poder/fuerza del enemigo, definido por la propiedad poder en archivo_enemigos.json
		:param cantidad_dados: la cantidad de dados que tendra (POR DEFECTO USA CANTIDAD_DADOS_DEFECTO)
		:param valor_maximo: para el rango de valores 1-valor_maximo (POR DEFECTO USA VALOR_MAXIMO_DADO)
		"""
		super().__init__(id_enemigo, nombre_enemigo, tipo_enemigo, cantidad_dados, valor_maximo)
		self._poder = poder_enemigo

	@property
	def id(self) -> int:
		"""
		Getter de la propiedad id
		:return: devuelve el id del enemigo
		"""
		return self._id

	@property
	def nombre(self) -> str:
		"""
		Getter de la propiedad nombre
		:return: devuelve el id del enemigo
		"""
		return self._nombre

	@property
	def tipo(self) -> Tipo:
		"""
		Override del getter de la propiedad tipo.
		:return: el tipo de enemigo que es
		"""
		return self._tipo

	@property
	def poder(self) -> int:
		"""
		Getter del poder del enemigo
		:return: Devuelve el poder del enemigo, que será restado a los puntos_vida del heroe cuando pierda
		"""
		return self._poder
