from typing import Optional
from Recursos.Item import Item
from Recursos.Personaje import Enemigo


class Sala:

	def __init__(self, id_sala: int, enemigo_sala: Enemigo = None, items_sala: list = None):
		"""
		Constructor de la clase sala
		:param id_sala: el id de la sala
		:param enemigo_sala: una lista con los enemigos de la sala. De no haber tendrá valor None
		:param items_sala: una lista con los items de la sala. De no haber tendrá valor None
		"""
		self._id_sala = id_sala
		self._esta_explorada = False
		self._enemigo = enemigo_sala
		self._items = items_sala

	@property
	def id(self) -> int:
		"""
		Getter del id de la sala
		:return: Devuelve el id de la sala
		"""
		return self._id_sala

	@property
	def esta_explorada(self) -> bool:
		"""
		Getter de la propiedad esta_explorada
		:return: Devuelve True o False, dependiendo si la sala esta explorada o no
		"""
		return self._esta_explorada

	@property
	def enemigo(self) -> Enemigo:
		"""
		Getter del enemigo
		:return: Devuelve el enemigo que hay en la sala de haberlo o None
		"""
		return self._enemigo

	@property
	def items(self) -> list[Item]:
		"""
		Getter de los items de la sala
		:return: Devuelve una lista de items de la sala de haberlos o None si no se generaron items
		"""
		return self._items

	def coger_item(self, indice_item: int) -> Optional[Item]:
		"""
		Metodo usado para recoger items de la sala y actualizar la lista _items de la misma
		:param indice_item: el item que se quiere coger
		:return: si el indice es valido, devuelve el item almacenado en self._items[indice_item], sino devuelve None
		"""
		item_recogido = None
		if 0 <= indice_item < len(self._items):
			item_recogido = self._items.pop(indice_item)
		return item_recogido

	def soltar_item_en_sala(self, item_soltado) -> None:
		"""
		Añade el item soltado a la lista de items de la sala
		:param item_soltado: el item que se ha soltado en la sala
		"""
		self._items.append(item_soltado)
