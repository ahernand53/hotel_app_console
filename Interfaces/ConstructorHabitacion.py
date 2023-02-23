from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


class ConstructorHabitacion(ABC):

    @property
    @abstractmethod
    def habitacion(self):
        pass

    @abstractmethod
    def espacio_para(self, cantidad_personas):
        pass

    @abstractmethod
    def camas_para(self, cantidad_camas):
        pass

    @abstractmethod
    def con_tipo_cama(self, tipo_cama):
        pass

    @abstractmethod
    def con_aire(self):
        pass

    @abstractmethod
    def con_calentador(self):
        pass

    @abstractmethod
    def habitacion_vip(self):
        pass
