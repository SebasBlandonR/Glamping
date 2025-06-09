from datetime import date
from persona import Persona

class Huesped(Persona):
    def __init__(self, nombre, telefono, email, identificacion, fecha_nacimiento, pais_origen, preferencias_alimentarias):
        super().__init__(nombre, telefono, email, identificacion)
        self.__fecha_nacimiento = fecha_nacimiento
        self.__pais_origen = pais_origen
        self.__preferencias_alimentarias = preferencias_alimentarias

    def get_fecha_nacimiento(self):
        return self.__fecha_nacimiento

    def get_pais_origen(self):
        return self.__pais_origen

    def get_preferencias_alimentarias(self):
        return self.__preferencias_alimentarias

    def set_fecha_nacimiento(self, fecha_nacimiento):
        self.__fecha_nacimiento = fecha_nacimiento

    def set_pais_origen(self, pais_origen):
        self.__pais_origen = pais_origen

    def set_preferencias_alimentarias(self, preferencias_alimentarias):
        self.__preferencias_alimentarias = preferencias_alimentarias

    def calcular_edad(self):
        hoy = date.today()
        edad = hoy.year - self.__fecha_nacimiento.year
        if (hoy.month, hoy.day) < (self.__fecha_nacimiento.month, self.__fecha_nacimiento.day):
            edad -= 1
        return edad

    def mostrar_info(self):
        info_basica = super().mostrar_info()
        return f"{info_basica}, Fecha de nacimiento: {self.__fecha_nacimiento}, País de origen: {self.__pais_origen}, Preferencias alimentarias: {self.__preferencias_alimentarias}, Edad: {self.calcular_edad()} años"
