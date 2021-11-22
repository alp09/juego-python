from Mapa import creador_mapa
from Mapa.Sala import Sala
from Mapa.Sala import interfaz_sala

FILAS_MATRIZ_MAPA = 7
COLUMNAS_MATRIZ_MAPA = 15


def generar_mapa():
	"""
	Llama al creador de mapas con el tamaño definido en el archivo
	:return: la matriz del mapa y un diccionario que contiene todas las salas
	"""
	matriz_mapa, lista_salas = creador_mapa.generar_mapa(FILAS_MATRIZ_MAPA, COLUMNAS_MATRIZ_MAPA)
	return matriz_mapa, lista_salas


def _crear_salas_mapa(cantidad_salas: int) -> list[Sala]:
	"""
	Crea las salas que componen el mapa. La primera sala siempre estará vacía y la segunda siempre tendrá un enemigo
	:return: la lista de salas creadas
	"""
	lista_salas_creadas = [interfaz_sala.crear_sala_vacia()]
	for i in range(cantidad_salas - 2):
		lista_salas_creadas.append(interfaz_sala.crear_sala_aleatoria())
	lista_salas_creadas.append(interfaz_sala.crear_sala_final())
	return lista_salas_creadas
