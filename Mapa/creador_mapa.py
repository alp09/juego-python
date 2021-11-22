import numpy as np
import matplotlib.pyplot as plt


def _crear_matriz_mapa(filas: int, columnas: int) -> np.ndarray:
	"""
	Crea una matriz para el mapa con valores 0 y 1 aleatorios
	:param filas: la cantidad de filas que se quiere en la matriz
	:param columnas: la cantidad de columnas que se quiere en la matriz
	:return: la matriz para el mapa
	"""
	# El valor maximo es exclusive por lo que en vez de un 1 pongo un 2
	matriz = np.random.randint(0, 2, (filas, columnas), dtype='int8')
	return matriz


def _crear_matriz_validacion(matriz: np.ndarray) -> np.ndarray:
	"""
	Crea una matriz de booleanos del mismo tamaño que matriz.
	:param matriz: la matriz de la que se quiere sacar una copia para validaciones
	:return: la matriz de validaciones rellena con False y True donde corresponde
	"""
	# Al pasarle matriz como parametro, colocará un True donde haya valores Truthy y False donde haya valores Falsy
	matriz_validacion = np.array(matriz, dtype=bool)
	return matriz_validacion


def _es_posicion_celda_valida(matriz: np.ndarray, x: int, y: int) -> bool:
	"""
	Comprueba que la celda matriz[y, x] no causa un IndexError
	:param matriz: la matrtiz de la que se sacan las dimensiones para validar
	:param x y: la posicion a validar en la matriz
	:return: True si la celda es valida o False si hubiese un IndexError
	"""
	filas, columas = matriz.shape
	if 0 <= y < filas and 0 <= x < columas:
		return True
	return False


def _cellular_automata(matriz: np.ndarray, valor_verdadero, valor_falso) -> int:
	"""
	Aplica el algoritmo cellular automata a la matriz pasada por parámetro.
	Popularizado en John Conway’s Game of Life (buscando este nombre en Google muestra una demo)
	El funcionamiento es sencillo (estos valores están ajustados para el propósito de mi juego):

		1.- Se itera la matriz.
		2.- Si la célula esta 'viva' y tiene menos de 3 vecinos (se queda sola), muere
		3.- Si la célula esta 'viva' y tiene 5 o más vecinos, muere (por sobrepoblación)
		4.- Aquellas células con 3 o 4 vecinos sobreviven.
		5.- Células 'muertas' con más de 2 vecinos pasan a estar vivas

	:param matriz: la matrtiz que se va a procesar. Debe estar rellena con 2 valores distintos (que simbolizen True y False)
	:param valor_verdadero: valor usado para interpretar células vivas
	:param valor_falso: valor usado para interpretar células muertas
	:return: la matriz procesada y el numero de células vivas
	"""
	cantidad_celdas = 0
	filas, columnas = matriz.shape

	# PASO 1
	for y in range(filas):
		for x in range(columnas):

			estado_casilla = matriz[y, x]
			numero_vecinos = _contar_celdas_vecinas(matriz, valor_verdadero, x=x, y=y)

			# Si la celula esta vida
			if estado_casilla == valor_verdadero:

				# PASO 2
				if numero_vecinos < 3:
					matriz[y, x] = valor_falso

				# PASO 4
				elif numero_vecinos < 5:
					matriz[y, x] = valor_verdadero
					cantidad_celdas += 1

				# PASO 3
				else:
					matriz[y, x] = valor_falso

			# Si la célula esta muerta
			else:

				# PASO 5
				if numero_vecinos > 2:
					matriz[y, x] = valor_verdadero
					cantidad_celdas += 1

	return cantidad_celdas


def _contar_celdas_vecinas(matriz: np.ndarray, valor_verdadero, x: int, y: int) -> int:
	"""
	Cuenta el numero de casillas alrededor de matriz[fila, columna] cuyo valor es valor_verdadero
	:param matriz: la matriz que se va a usar
	:param x y: la fila y columna de la celda que se va a comprobar su alrededor
	:param valor_verdadero: el valor que se esta contando
	:return: el numero de vecinos que tiene la celda
	"""
	# Recoge la fila y columa
	fila, columna = y, x

	# En caso de que la posicion matriz[fila, columna] tenga algun valor, se le deduce antes de empezar a contar
	numero_vecinos = -1 if matriz[fila, columna] == valor_verdadero else 0

	# Recorre las casillas alrededor de la celda matriz[fila, columna], incluida la propia celda,
	# por eso arriba se le deduce un vecino de tener esta algun valor
	for y in range(fila - 1, fila + 2):
		for x in range(columna - 1, columna + 2):
			if _es_posicion_celda_valida(matriz, x=x, y=y):
				if matriz[y, x] == valor_verdadero:
					numero_vecinos += 1

	return numero_vecinos


def _posiciones_cardinales(x: int, y: int) -> list[dict]:
	"""
	Calcula las posiciones cardinales de la coordenada pasada por parametro
	:param x: la columna de la coordenada
	:param y: la fila de la coordenada
	:return: una lista de diccionarios con dos claves; x e y
	"""
	# Guarda la variacion en las coordenadas de los 4 puntos cardinales
	# EJ: el norte de la coordenada x=3, y=8 seria x=3, y=8-1
	OFFSET_PUNTOS_CARDINALES = {
		#    		  y   x
		"NORTE": 	(-1,  0),
		"SUR": 		( 1,  0),
		"ESTE": 	( 0,  1),
		"OESTE": 	( 0, -1)
	}

	# Una lista de diccionarios que contiene las coordenadas de los puntos cardinales calculadas
	puntos_cardinales_calculados = []

	# Recorre el diccionario con las 4 posiciones cardinales y guarda el resultado en la lista
	for direccion, (offset_y, offset_x) in OFFSET_PUNTOS_CARDINALES.items():
		puntos_cardinales_calculados.append({"direccion": direccion, "x": x + offset_x, "y": y + offset_y})

	return puntos_cardinales_calculados


def _flood(matriz_validacion: np.ndarray, x: int, y: int, cantidad_celdas: int = 0) -> tuple[np.ndarray, int]:
	"""
	El algoritmo flood determina el área formada por elementos contiguos* en una matriz multidimensional.
	Usado por ejemplo en Paint para la herramienta 'cubeta'.

	*En mi caso lo implemento solo para las celdas que esten en los puntos cardinales, puesto que el jugador no podrá
	viajar a salas que esten en las diagonales.

	El uso que le doy sería el de 'marcar' todas las celdas que estan conectadas
	a la celda que paso por parametro en la primera llamada.

	Sabiendo si una celda esta 'marcada' o no, se si pertenece a una ramificacion de celdas distintas.

	:param matriz_validacion: la matriz usada para marcar las celdas ya rellenadas.
	:param x: la columna de la celda que se va a comprobar.
	:param y: la fila de la celda que se va a comprobar.
	:param cantidad_celdas: un contador de las celdas contiguas encontradas. Para uso interno de la funcion recursiva (no usarlo)
	:return: una tupla donde el primer valor es la matriz de validacion con las celdas encontradas marcadas a False
			y el segundo es la cantidad de celdas encontradas.
	"""
	# Si la posicion es valida (no esta 'marcada' aun ni es una pared)
	if matriz_validacion[y, x]:

		# Marca en la matriz de validacion la posicion como 'explorada'
		matriz_validacion[y, x] = False
		cantidad_celdas += 1

		# Llama de nuevo a la funcion (por eso es recursiva) desde las posiciones calculadas en _posiciones_cardinales() que sean validas
		for siguiente_posicion in _posiciones_cardinales(x=x, y=y):
			if _es_posicion_celda_valida(matriz_validacion, x=siguiente_posicion["x"], y=siguiente_posicion["y"]):
				matriz_validacion, cantidad_celdas = _flood(matriz_validacion, x=siguiente_posicion["x"], y=siguiente_posicion["y"], cantidad_celdas=cantidad_celdas)

	return matriz_validacion, cantidad_celdas


def _mapa_dijkstra(matriz: np.ndarray, matriz_validacion: np.ndarray, valor_actual: int, x: int, y: int) -> tuple[np.ndarray, np.ndarray]:
	"""
	Calcula el mapa dijkstra a partir de una posicion de origen
	Si la posición de origen es una pared no ejecutará nada

	Esta función recursiva recorre todas las posiciones accesibles desde la posicion de origen
	y no termina hasta que encuentra el camino más corto para cada una de las celdas

	:param matriz: la matriz en la que se va a plasmar el camino
	:param matriz_validacion: matriz de booleanos que contiene aquellas casillas ya exploradas o que son paredes
	:param valor_actual: el número de casillas desde la posición de origen
	:param x: la columna de la posicion que se esta comprobando
	:param y: la fila de la posicion que se esta comprobando
	:return: la matriz procesada junto con su matriz de validacion actualizado
	"""
	# Comprueba si la posicion es una pared o esta explorada
	# O si es una posicion explorada anteriormente por un camino más largo
	if matriz_validacion[y, x] or matriz[y, x] > valor_actual:

		# Establece la posicion actual al valor actual
		matriz[y, x] = valor_actual

		# Marca en la matriz de validacion la posicion como 'explorada'
		matriz_validacion[y, x] = False

		# Llama de nuevo a la funcion (por eso es recursiva) desde las posiciones calculadas en _posiciones_cardinales() que sean validas
		for siguiente_posicion in _posiciones_cardinales(x=x, y=y):
			if _es_posicion_celda_valida(matriz, x=siguiente_posicion["x"], y=siguiente_posicion["y"]):
				matriz, matriz_validacion = _mapa_dijkstra(matriz, matriz_validacion, valor_actual + 1, x=siguiente_posicion["x"], y=siguiente_posicion["y"])

	return matriz, matriz_validacion


def _localizar_origen_de_salas(matriz: np.ndarray) -> list[dict]:
	"""
	Esta funcion recorre la matriz pasada por parametro y recoge una coordenada (origen) para
	cada conjunto de celdas contiguas.

	:param matriz: la matriz que se va a recorrer
	:return: un diccionario donde la key son los puntos de origen de cada conjunto de celdas (x, y)
	y el valor es el volumen que ocupa esa ramificacion de celdas
	"""
	filas, columnas = matriz.shape
	matriz_validacion = _crear_matriz_validacion(matriz)
	lista_puntos_origen = []

	for y in range(filas):
		for x in range(columnas):

			if matriz_validacion[y, x]:
				matriz_validacion, volumen_sala = _flood(matriz_validacion, x=x, y=y)

				punto_origen = {"x": x, "y": y, "volumen": volumen_sala}
				lista_puntos_origen.append(punto_origen)

	return lista_puntos_origen


def _calcular_salidas_por_sala(matriz: np.ndarray):
	"""
	Recorre la matriz y por cada celda con un valor, recoge la posicion de esta y la de sus vecinos validos
	:param matriz: la matriz que se va a recorrer
	:return: una lista de diccionarios con la información de
	"""
	filas, columnas = matriz.shape
	lista_celdas = {}

	for y in range(filas):
		for x in range(columnas):

			# Si es una posicion de la matriz con contenido
			if matriz[y, x]:

				# Reune la informacion sobre las celdas vecinas
				informacion_vecinos = {}
				for sala_vecina in _posiciones_cardinales(x=x, y=y):
					if _es_posicion_celda_valida(matriz, x=sala_vecina["x"], y=sala_vecina["y"]):
						informacion_vecinos[sala_vecina["direccion"]] = (sala_vecina["x"], sala_vecina["y"])
					else:
						informacion_vecinos[sala_vecina["direccion"]] = None

				# Agrega una entrada al diccionario con las coordenadas de la celda y sus vecinos
				lista_celdas[(x, y)] = informacion_vecinos

	return lista_celdas


def dibujar_matriz(matriz: np.ndarray):
	"""
	Dibuja la matriz pasada por parámetro
	:param matriz: la matriz a dibujar
	"""
	plt.imshow((matriz + 5) * _crear_matriz_validacion(matriz), interpolation='nearest')
	plt.colorbar()
	plt.show()


def generar_mapa(cantidad_filas: int = 10, cantidad_columnas: int = 25):

	# Crea una matriz rellena de 0 y 1 aleatoriamente
	FILAS_MAPA = cantidad_filas
	COLUMAS_MAPA = cantidad_columnas
	nuevo_mapa = _crear_matriz_mapa(FILAS_MAPA, COLUMAS_MAPA)

	# Aplica el algoritmo cellular automata hasta que queden menos de la mitad de las casillas activas
	while _cellular_automata(nuevo_mapa, 1, 0) > FILAS_MAPA * COLUMAS_MAPA * .5:
		continue

	# Busca un punto de origen para cada conjunto de celdas contiguas y los ordeno por el volumen de estos
	puntos_origen = sorted(_localizar_origen_de_salas(nuevo_mapa), key=lambda punto_origen: punto_origen["volumen"])

	# Guardo la sala mas grande, que estará en la última posicion de la lista puntos_origen
	sala_mas_grande = puntos_origen.pop(-1)

	# El resto de salas las elimino
	for sala_origen in puntos_origen:

		# Marco en mapa_actualizado las celdas que pertenece a sala_a_borrar
		mapa_actualizado, _ = _flood(_crear_matriz_validacion(nuevo_mapa), sala_origen["x"], sala_origen["y"])

		# Despues 'borra' las salas que forman ese conjunto.
		# Esto es posible gracias a numpy, que ofrece entre otras cosas aplicar operaciones matematicas entre matrices.
		nuevo_mapa = nuevo_mapa * mapa_actualizado

		# Lo que esta ocurriendo es que esta multiplicando el valor de cada celda en mapa (que sera de 0 o 1)
		# por el valor del mapa_validacion (que sera True o False; que equivale a 1 o 0)
		# Una celda con valor 1 que queda 'marcada' en el mapa_validacion como False al multiplicarse da como resultado 0, convirtiendose en pared.

		# Por decirlo de otra forma, es como cuando vas a pintar en la pared un grafitti
		# pero pones por delante un trozo de cartón con la silueta de lo que quieres pintar.

	nuevo_mapa, _ = _mapa_dijkstra(nuevo_mapa, _crear_matriz_validacion(nuevo_mapa), 1, x=sala_mas_grande["x"], y=sala_mas_grande["y"])
	diccionario_salas = _calcular_salidas_por_sala(nuevo_mapa)

	return nuevo_mapa, diccionario_salas


if __name__ == "__main__":
	mapa, informacion_celdas = generar_mapa()
	dibujar_matriz(mapa)

# TODO: Elegir la ultima sala. Por ejemplo la mas lejana al punto_origen
