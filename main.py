

from models.Asesor import Asesor
from models.Hotel import Hotel

hotel = Hotel("Hotel 1")
asesor = Asesor()

hotel.constructor = asesor

hab1 = hotel.obtener_habitacion_sencilla()
hab2 = hotel.obtener_habitacion_romantica()
print(hab1)
print(hab2)
