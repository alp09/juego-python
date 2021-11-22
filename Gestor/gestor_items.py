from Mapa import Sala
from Recursos.Item import Item
from Recursos.Personaje import Heroe


def mostrar_items_sala(sala_actual: Sala) -> list[Item]:
	"""
	Llama al getter de items que hay en la sala actual
	:param sala_actual: la sala de la que se quiere ver los items
	:return: los items que hay en la sala
	"""
	return sala_actual.items


def coger_item(heroe: Heroe, indice_item_recogido: int, sala_actual: Sala) -> bool:
	"""
	Recoge el item indicado en indice_item_recogido y lo añade al inventario del heroe si este tiene espacio
	:param heroe: el heroe al que se le va a guardar el item en su inventario
	:param indice_item_recogido: el indice del item en la lista de items de la sala
	:param sala_actual: la sala de la que se va a tomar el item
	:return: True si queda espacio en el inventario del heroe (y puedo guardarlo) o False si se cancelo la operacion
	"""
	item_recogido = sala_actual.coger_item(indice_item_recogido)
	queda_espacion_inventario_heroe = True

	if item_recogido is not None:
		queda_espacion_inventario_heroe = heroe.guardar_en_inventario(item_recogido)
		if not queda_espacion_inventario_heroe:
			sala_actual.soltar_item_en_sala(item_recogido)

	return queda_espacion_inventario_heroe


def soltar_item(heroe: Heroe, indice_item_soltado: int, sala_actual: Sala) -> bool:
	"""
	Elimina la primera aparicion del item_soltado del inventario del heroe
	:param heroe: el heroe del que se va a quitar el item_soltado
	:param indice_item_soltado: el indice del item que se quiere soltar
	:param sala_actual: la sala donde se va a dejar el item
	:return: True si el item se soltó correctamente o False si el indice_item_soltado no es válido
	"""
	item_soltado = heroe.descartar_de_inventario(indice_item_soltado)
	if item_soltado is not None:
		sala_actual.soltar_item_en_sala(item_soltado)
	return True if item_soltado is not None else False
