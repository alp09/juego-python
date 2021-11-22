import json
import random

# quantumrand.randint() tiene que hacer peticiones a la API de https://qrng.anu.edu.au/
# por lo que la velocidad del programa se ve ralentizada por el tiempo de respuesta de una petición a un servidor


def generar_numero_aleatorio(minimo: int = 0, maximo: int = 1):
	"""
	Genera un numero aleatorio entre el minimo y maximo especificado (ambos inclusive)
	Intercambia el valor de los parametros si minimo > maximo
	:param minimo: el valor minimo que se puede generar
	:param maximo: el valor maximo que se puede generar
	:return: el numero generado
	"""
	numero_aleatorio = random.randint(minimo, maximo)
	return numero_aleatorio


def calcular_probabilidad(probabilidad: int):
	"""
	Para una probabilidad dada, evalua si se sucede o no el evento
	:param probabilidad: un int entre 0 y 100
	:return: True si el suceso ocurre o False si no ocurre o la probabilidad no es valida
	"""
	numero_generado = generar_numero_aleatorio(1, 100)
	return True if numero_generado <= probabilidad else False


def to_json(datos) -> str:
	"""
	Parsea los datos pasados por parametro a JSON
	:param datos: los datos a parsear
	:return: una cadena con el resultado del parseo
	"""
	pass
	return json.dumps(datos, default=lambda objeto: objeto.__dict__, indent=4)

