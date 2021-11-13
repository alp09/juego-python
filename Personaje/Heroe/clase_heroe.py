from Personaje.clase_personaje import Personaje
from utils import generar_numero_aleatorio

PUNTOS_VIDA_MINIMO = 0                  # El valor minimo de puntos_vida del heroe. Al llegar a 0 estaría "muerto"
PUNTOS_VIDA_MAXIMO = 200                # El valor maximo de puntos_vida del heroe
_PUNTOS_VIDA_CREACION_MINIMO = 100		# El valor minimo de puntos_vida con los que puede iniciar el heroe
_CANTIDAD_DADOS_DEFECTO = 3             # La cantidad de dados que tiene el heroe por defecto
_VALOR_MAXIMO_DADO = 20                 # El valor maximo del dado usado por defecto


class Heroe(Personaje):

	def __init__(
			self,
			nombre_heroe: str,
			habilidad_heroe: str,
			cantidad_dados: int = _CANTIDAD_DADOS_DEFECTO,
			valor_maximo: int = _VALOR_MAXIMO_DADO):
		"""
		Constructor del personaje Heroe, controlado por el jugador
		:param nombre_heroe: el nombre del heroe
		:param habilidad_heroe: la habilidad elegida por el heroe (DEBE ESTAR EN Personaje.TIPOS_PERSONAJES)
		:param cantidad_dados: la cantidad de dados que tendra el heroe (POR DEFECTO USA CANTIDAD_DADOS_DEFECTO)
		:param valor_maximo: para el rango de valores 1-valor_maximo (POR DEFECTO USA VALOR_MAXIMO_DADO)
		"""
		super().__init__(-1, nombre_heroe, habilidad_heroe, cantidad_dados, valor_maximo)
		self._puntos_vida = generar_numero_aleatorio(_PUNTOS_VIDA_CREACION_MINIMO, PUNTOS_VIDA_MAXIMO)

	@Personaje.tipo.getter
	def habilidad(self):
		"""
		Override del getter de la propiedad tipo.
		Notese que el nombre del metodo es habilidad, renombrando asi el nombre de la propiedad
		:return: el tipo de heroe o dicho de otra forma (para que se vea mas claro) la habilidad que se ha elegido
		"""
		return self._tipo

	@property
	def puntos_vida(self):
		"""
		Getter de la propiedad puntos_vida
		:return: devuelve los puntos_vida actuales
		"""
		return self._puntos_vida

	def modificar_puntos_vida(self, modificacion_puntos_vida):
		"""
		Suma o resta los puntos indicados en puntos_vida
		:param modificacion_puntos_vida: la cantidad a sumar o restar de los puntos de vida actuales
		:return: los puntos_vida resultantes
		"""
		self._puntos_vida += modificacion_puntos_vida
		self._puntos_vida = max(self._puntos_vida, PUNTOS_VIDA_MINIMO)
		self._puntos_vida = min(self._puntos_vida, PUNTOS_VIDA_MAXIMO)
		return self._puntos_vida
