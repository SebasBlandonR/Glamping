import ServiciosAdicionales

class Reserva:
    def __init__(self, codigo_reserva: str, huesped, alojamiento, fecha_checkin, fecha_checkout):
        self.__codigo_reserva = codigo_reserva
        self.__huesped = huesped
        self.__alojamiento = alojamiento
        self.__fecha_checkin = fecha_checkin
        self.__fecha_checkout = fecha_checkout
        self.__servicios_adicionales = []
        self.__precio_total = 0.0
        self.__estado = "confirmada"  #el estado es el incial
        
        
        self.__alojamiento.reservar()


    def get_codigo_reserva(self) -> str:
        return self.__codigo_reserva

    def get_huesped(self):
        return self.__huesped

    def get_alojamiento(self):
        return self.__alojamiento

    def get_fecha_checkin(self):
        return self.__fecha_checkin

    def get_fecha_checkout(self):
        return self.__fecha_checkout

    def get_servicios_adicionales(self) -> list:
        return self.__servicios_adicionales

    def get_precio_total(self) -> float:
        return self.__precio_total

    def get_estado(self) -> str:
        return self.__estado


    def set_codigo_reserva(self, nuevo_codigo: str):
        self.__codigo_reserva = nuevo_codigo

    def set_huesped(self, nuevo_huesped):
        self.__huesped = nuevo_huesped

    def set_alojamiento(self, nuevo_alojamiento):
    
        self.__alojamiento.liberar()
        self.__alojamiento = nuevo_alojamiento
        nuevo_alojamiento.reservar()

    def set_fecha_checkin(self, nueva_fecha):
        if hasattr(self, '_Reserva__fecha_checkout') and nueva_fecha > self.__fecha_checkout:
            raise ValueError("Check-in no puede ser después del check-out")
        self.__fecha_checkin = nueva_fecha

    def set_fecha_checkout(self, nueva_fecha):
        if hasattr(self, '_Reserva__fecha_checkin') and nueva_fecha < self.__fecha_checkin:
            raise ValueError("Check-out no puede ser antes del check-in")
        self.__fecha_checkout = nueva_fecha

    def set_estado(self, nuevo_estado: str):
        estados_validos = ["confirmada", "en_curso", "finalizada", "cancelada"]
        if nuevo_estado.lower() in estados_validos:
            self.__estado = nuevo_estado.lower()
            
     
            if nuevo_estado.lower() in ["cancelada", "finalizada"]:
                self.__alojamiento.liberar()
        else:
            raise ValueError(f"Estado no válido. Debe ser uno de: {', '.join(estados_validos)}")

    def calcular_noches(self) -> int:
        """Calcula el número de noches de la reserva"""
        diferencia = self.__fecha_checkout - self.__fecha_checkin
        return diferencia.days

    def agregar_servicio(self, servicio: ServiciosAdicionales):
        """Agrega un servicio adicional a la reserva"""
        if isinstance(servicio, ServiciosAdicionales):
            self.__servicios_adicionales.append(servicio)
            self.__precio_total += servicio.get_precio()
        else:
            raise TypeError("El objeto debe ser de tipo ServicioAdicional")

    def calcular_precio_total(self, temporada: str = "baja") -> float:
        """Calcula el precio total de la reserva incluyendo alojamiento y servicios"""
        noches = self.calcular_noches()
        precio_alojamiento = self.__alojamiento.calcular_precio_temporada(temporada) * noches
        
        precio_servicios = sum(servicio.get_precio() for servicio in self.__servicios_adicionales)
        
        self.__precio_total = precio_alojamiento + precio_servicios
        return self.__precio_total

    def cambiar_estado(self, nuevo_estado: str):
        """Cambia el estado de la reserva"""
        self.set_estado(nuevo_estado)
    def mostrar_info(self) -> str:
        """Muestra información completa de la reserva"""
        info = (f"Reserva #{self.__codigo_reserva}\n"
                f"Huésped: {self.__huesped.get_nombre()}\n"
                f"Alojamiento: {self.__alojamiento.get_tipo()} (#{self.__alojamiento.get_numero()})\n"
                f"Check-in: {self.__fecha_checkin.strftime('%d/%m/%Y')}\n"
                f"Check-out: {self.__fecha_checkout.strftime('%d/%m/%Y')}\n"
                f"Noches: {self.calcular_noches()}\n"
                f"Estado: {self.__estado.upper()}\n"
                f"Servicios adicionales ({len(self.__servicios_adicionales)}):")
        
        for servicio in self.__servicios_adicionales:
            info += f"\n- {servicio.get_nombre()} (${servicio.get_precio():.2f})"
        
        info += f"\nPrecio total: ${self.__precio_total:.2f}"
        
        return info