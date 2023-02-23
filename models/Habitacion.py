import uuid


class Habitacion():

    def __init__(self):
        self.id = uuid.uuid1()
        self.cantidad_personas = ""
        self.cantidad_camas = ""
        self.aire_acondicionado = False
        self.vip = False
        self.calentador = False
        self.tipo_camas = ""

    def tiene_aire(self):
        return "Yes." if self.aire_acondicionado else "Not."

    def tiene_calentador(self):
        return "Yes." if self.calentador else "Not."

    def es_vip(self):
        return "Yes." if self.vip else "Not."

    def __str__(self) -> str:
        return "--------------------------\nhab-{}: \nCantidad de personas: {} \nCantidad de camas: {} \nAire Acondicionado: {} \nVIP: {} \nCalentador: {} \nTipo Camas: {}\n--------------------------".format(self.id, self.cantidad_personas, self.cantidad_camas, self.tiene_aire(), self.es_vip(), self.tiene_calentador(), self.tipo_camas)
