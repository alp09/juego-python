from random import randint


def generar_numero_aleatorio(minimo: int = 0, maximo: int = 1):
	numero_aleatorio = randint(minimo, maximo)
	return numero_aleatorio


def calcular_probabilidad(probabilidad: int):
	numero_generado = generar_numero_aleatorio(1, 100)
	return True if numero_generado <= probabilidad else False

# quantumrand.randint() tiene que hacer peticiones a la API de https://qrng.anu.edu.au/
# por lo que la velocidad del programa se ve ralentizada por el tiempo de respuesta de una petición a un servidor
