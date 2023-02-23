

from Interfaces.ConstructorHabitacion import ConstructorHabitacion
from models.Habitacion import Habitacion


class Hotel():

    def __init__(self, nombre_hotel) -> None:
        self.nombre_hotel = nombre_hotel
        self._constructor = None

    @property
    def constructor(self) -> ConstructorHabitacion:
        return self._constructor

    @constructor.setter
    def constructor(self, constructor: ConstructorHabitacion) -> None:
        self._constructor = constructor

    def obtener_habitacion_sencilla(self) -> Habitacion:
        self._constructor.espacio_para(1)
        self._constructor.camas_para(1)
        self._constructor.con_tipo_cama("Sencilla")
        self._constructor.con_aire(False)
        self._constructor.con_calentador(True)
        self._constructor.habitacion_vip(False)

        return self._constructor.construir()

    def obtener_habitacion_romantica(self) -> Habitacion:
        self._constructor.espacio_para(2)
        self._constructor.camas_para(2)
        self._constructor.con_tipo_cama("King")
        self._constructor.con_aire(True)
        self._constructor.con_calentador(True)
        self._constructor.habitacion_vip(False)

        return self._constructor.construir()

    def obtener_habitacion_presidencial(self) -> Habitacion:
        self._constructor.espacio_para(2)
        self._constructor.camas_para(2)
        self._constructor.con_tipo_cama("Super King")
        self._constructor.con_aire(True)
        self._constructor.con_calentador(True)
        self._constructor.habitacion_vip(True)

        return self._constructor.construir()
