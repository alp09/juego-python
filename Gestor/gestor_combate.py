from Recursos.Personaje import Heroe
from Recursos.Personaje import Enemigo


def ejecutar_lucha(heroe: Heroe, enemigo: Enemigo):
	"""
	Comienza la lucha y procesa el resultado de esta
	:param heroe: el heroe que esta luchando
	:param enemigo: el enemigo al que se esta enfrentando
	:returns: una tupla donde el primer valor es un booleano con el estado del heroe; True si sigue vivo o False si sus puntos_vida llegaron a 0
	y el segundo valor es el resultado de la lucha; negativo si perdió o la cantidad de puntos si ganó
	"""
	while (resultado_lucha := _lanzar_dados(heroe.dados, enemigo.dados)) == 0:
		continue

	if resultado_lucha > 0:
		esta_vivo_heroe = True
		resultado_lucha = _procesar_victoria_lucha(heroe, enemigo)
	else:
		esta_vivo_heroe = _procesar_derrota_lucha(heroe, enemigo)

	return esta_vivo_heroe, resultado_lucha


def _lanzar_dados(dados_heroe: list, dados_enemigo: list) -> int:
	"""
	Lanza todos los dados del heroe y enemigo y los posteriormente los compara
	La comparación se hace n a n. Esto es, el más grande del heroe con el más grande del enemigo,
	el segundo del heroe con el segundo del enemigo, etc.
	:param dados_heroe: la lista de dados del heroe
	:param dados_enemigo: la lista de dados del enemigo
	:return: el resultado del lanzamiento de dados. Mayor que 0 significa que ganó el heroe, menor que 0 que perdió y 0 que empató.
	"""
	resultados_dados_heroe = sorted([dado.lanzar_dados() for dado in dados_heroe], reverse=True)
	resultados_dados_enemigo = sorted([dado.lanzar_dados() for dado in dados_enemigo], reverse=True)

	resultado_lucha = 0
	for i in range(min(len(dados_heroe), len(dados_enemigo))):
		if resultados_dados_heroe[i] > resultados_dados_enemigo[i]:
			resultado_lucha += 1
		elif resultados_dados_heroe[i] < resultados_dados_enemigo[i]:
			resultado_lucha -= 1

	return resultado_lucha


def _procesar_derrota_lucha(heroe: Heroe, enemigo: Enemigo) -> bool:
	"""
	Resta los puntos de poder del enemigo a la vida del heroe
	:param heroe: el heroe al que se le va a restar la vida
	:param enemigo: el enemigo que ha atacado al heroe
	:return: True si el heroe sigue vivo a False si muere
	"""
	esta_vivo_heroe = heroe.modificar_puntos_vida(-enemigo.poder)
	return esta_vivo_heroe


def _procesar_victoria_lucha(heroe: Heroe, enemigo: Enemigo) -> int:
	"""
	Suma los puntos de los items cuyos Tipos sean iguales a los del enemigo que acaba de derrotar
	:param heroe: el heroe del cual se va a buscar en su inventario
	:param enemigo: el enemigo que se acaba de derrotar
	:return: la puntuacion actual del heroe
	"""
	item_utiles = list(filter(lambda item: item.tipo == enemigo.tipo, heroe.inventario))
	[heroe.sumar_puntos_al_total(item.puntos) for item in item_utiles]
	heroe.sumar_puntos_al_total(enemigo.poder)
	return heroe.puntuacion
