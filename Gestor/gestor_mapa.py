import utils as utils
import Sala.interfaz_sala as interfaz_sala

_MINIMO_NUMERO_SALAS = 10
_MAXIMO_NUMERO_SALAS = 15
_CANTIDAD_SALAS_MAPA = utils.generar_numero_aleatorio(_MINIMO_NUMERO_SALAS, _MAXIMO_NUMERO_SALAS)
_salas_creadas = 0
salas_mapa = []

_PROBABILIDAD_PRIMER_OBJETO = 75
_PROBABILIDAD_SEGUNDO_OBJETO = 30

_PROBABILIDAD_GENERAR_MOSTRUO = 75
_PENALIZACION_MOSTRUO_GENERADO = 10
_salas_con_monstruo_consecutivas = 0
_probabilidad_actual_generar_monstruo = _PROBABILIDAD_GENERAR_MOSTRUO - (_PENALIZACION_MOSTRUO_GENERADO * _salas_con_monstruo_consecutivas)


def _generar_sala():
	"""
	Calcula el contenido de la sala_creada y posteriormente crea una instacion con los valores adecuados
	Una vez crea la sala, suma 1 al contador de salas creadas
	:return: una instancia de la sala ya creada
	"""
	global _salas_creadas
	generar_monstruo = utils.calcular_probabilidad(_probabilidad_actual_generar_monstruo)
	cantidad_objetos_generados = 0

	if utils.calcular_probabilidad(_PROBABILIDAD_PRIMER_OBJETO):
		cantidad_objetos_generados += 1
		if utils.calcular_probabilidad(_PROBABILIDAD_SEGUNDO_OBJETO):
			cantidad_objetos_generados += 1

	sala_creada = interfaz_sala.crear_sala(_salas_creadas, generar_monstruo, cantidad_objetos_generados)
	_salas_creadas += 1
	return sala_creada


def crear_mapa():

	for i in range(_CANTIDAD_SALAS_MAPA):
		salas_mapa.append(_generar_sala())
