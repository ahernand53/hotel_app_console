from Interfaces.ConstructorHabitacion import ConstructorHabitacion
from models.Habitacion import Habitacion


class Asesor(ConstructorHabitacion):

    def __init__(self) -> None:
        self.limpiar()

    def limpiar(self) -> None:
        self._habitacion = Habitacion()

    @property
    def habitacion(self) -> Habitacion:
        habitacion = self._habitacion
        self.limpiar()
        return habitacion

    def construir(self):
        return self.habitacion

    def espacio_para(self, cantidad_personas):
        self._habitacion.cantidad_personas = cantidad_personas

    def camas_para(self, cantidad_camas):
        self._habitacion.cantidad_camas = cantidad_camas

    def con_tipo_cama(self, tipo):
        self._habitacion.tipo_camas = tipo

    def con_aire(self, con_aire):
        self._habitacion.aire_acondicionado = con_aire

    def con_calentador(self, con_calentador):
        self._habitacion.calentador = con_calentador

    def habitacion_vip(self, es_vip):
        self._habitacion.vip = es_vip
