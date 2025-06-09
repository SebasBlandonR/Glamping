from datetime import date
from typing import List, Optional

class Glamping:
    
    def __init__(self, nombre: str, ubicacion: str):
        self.__nombre = nombre
        self.__ubicacion = ubicacion
        self.__alojamientos = []
        self.__huespedes = []
        self.__empleados = []
        self.__reservas = []
        self.__servicios_disponibles = []
    
    def get_nombre(self) -> str:
        return self.__nombre
    
    def get_ubicacion(self) -> str:
        return self.__ubicacion
    
    def get_alojamientos(self) -> List:
        return self.__alojamientos.copy()
    
    def get_huespedes(self) -> List:
        return self.__huespedes.copy()
    
    def get_empleados(self) -> List:
        return self.__empleados.copy()
    
    def get_reservas(self) -> List:
        return self.__reservas.copy()
    
    def get_servicios_disponibles(self) -> List:
        return self.__servicios_disponibles.copy()
    
    def set_nombre(self, nombre: str):
        self.__nombre = nombre
    
    def set_ubicacion(self, ubicacion: str):
        self.__ubicacion = ubicacion
    
    def agregar_alojamiento(self, alojamiento):
        for aloj in self.__alojamientos:
            if aloj.get_numero() == alojamiento.get_numero():
                print(f"Error: Ya existe un alojamiento con el número {alojamiento.get_numero()}")
                return False
        
        self.__alojamientos.append(alojamiento)
        print(f"Alojamiento #{alojamiento.get_numero()} agregado exitosamente")
        return True
    
    def registrar_huesped(self, huesped):
        for h in self.__huespedes:
            if h.get_identificacion() == huesped.get_identificacion():
                print(f"Error: El huésped con ID {huesped.get_identificacion()} ya está registrado")
                return False
        
        self.__huespedes.append(huesped)
        print(f"Huésped {huesped.get_nombre()} registrado exitosamente")
        return True
    
    def contratar_empleado(self, empleado):
        for emp in self.__empleados:
            if emp.get_identificacion() == empleado.get_identificacion():
                print(f"Error: El empleado con ID {empleado.get_identificacion()} ya está registrado")
                return False
        
        self.__empleados.append(empleado)
        print(f"Empleado {empleado.get_nombre()} contratado como {empleado.get_cargo()}")
        return True
    
    def agregar_servicio_disponible(self, servicio):
        self.__servicios_disponibles.append(servicio)
        print(f"Servicio '{servicio.get_nombre()}' agregado al catálogo")
    
    def buscar_huesped_por_id(self, identificacion: str):
        for huesped in self.__huespedes:
            if huesped.get_identificacion() == identificacion:
                return huesped
        return None
    
    def buscar_alojamiento_por_numero(self, numero: int):
        for alojamiento in self.__alojamientos:
            if alojamiento.get_numero() == numero:
                return alojamiento
        return None
    
    def crear_reserva(self, huesped_id: str, alojamiento_num: int, 
            fecha_checkin: date, fecha_checkout: date):
        if fecha_checkin >= fecha_checkout:
            print("Error: La fecha de check-in debe ser anterior a la fecha de check-out")
            return None
        
        if fecha_checkin < date.today():
            print("Error: La fecha de check-in no puede ser en el pasado")
            return None
        
        huesped = self.buscar_huesped_por_id(huesped_id)
        if not huesped:
            print(f"Error: No se encontró huésped con ID: {huesped_id}")
            return None
        
        alojamiento = self.buscar_alojamiento_por_numero(alojamiento_num)
        if not alojamiento:
            print(f"Error: No se encontró alojamiento #{alojamiento_num}")
            return None
        
        if not self._verificar_disponibilidad_alojamiento(alojamiento_num, fecha_checkin, fecha_checkout):
            print(f"Error: El alojamiento #{alojamiento_num} no está disponible en las fechas solicitadas")
            return None
        
        codigo_reserva = f"RES{len(self.__reservas) + 1:04d}"
        
        try:
            print(f"Reserva {codigo_reserva} creada exitosamente")
            print(f"Huésped: {huesped.get_nombre()}")
            print(f"Alojamiento: #{alojamiento.get_numero()}")
            print(f"Fechas: {fecha_checkin} a {fecha_checkout}")
            return codigo_reserva
        except Exception as e:
            print(f"Error al crear la reserva: {e}")
            return None
    
    def _verificar_disponibilidad_alojamiento(self, alojamiento_num: int, 
                                            fecha_checkin: date, fecha_checkout: date) -> bool:
        alojamiento = self.buscar_alojamiento_por_numero(alojamiento_num)
        if not alojamiento or not alojamiento.get_disponible():
            return False
        
        for reserva in self.__reservas:
            if (reserva.get_alojamiento().get_numero() == alojamiento_num and
                reserva.get_estado() in ["confirmada", "en_curso"]):
                if not (fecha_checkout <= reserva.get_fecha_checkin() or 
                        fecha_checkin >= reserva.get_fecha_checkout()):
                    return False
        
        return True
    
    def buscar_alojamiento_disponible(self, tipo: str, fecha_checkin: date, fecha_checkout: date) -> List:
        disponibles = []
        
        for alojamiento in self.__alojamientos:
            if (alojamiento.get_tipo().lower() == tipo.lower() and 
                self._verificar_disponibilidad_alojamiento(alojamiento.get_numero(), 
                    fecha_checkin, fecha_checkout)):
                disponibles.append(alojamiento)
        
        return disponibles
    
    def calcular_ocupacion_actual(self) -> float:
        if not self.__alojamientos:
            return 0.0
        
        alojamientos_ocupados = 0
        fecha_actual = date.today()
        
        for alojamiento in self.__alojamientos:
            for reserva in self.__reservas:
                if (reserva.get_alojamiento().get_numero() == alojamiento.get_numero() and
                    reserva.get_estado() in ["confirmada", "en_curso"] and
                    reserva.get_fecha_checkin() <= fecha_actual <= reserva.get_fecha_checkout()):
                    alojamientos_ocupados += 1
                    break
        
        return (alojamientos_ocupados / len(self.__alojamientos)) * 100
    
    def listar_reservas_activas(self) -> List:
        reservas_activas = []
        
        for reserva in self.__reservas:
            if reserva.get_estado() in ["confirmada", "en_curso"]:
                reservas_activas.append(reserva)
        
        return reservas_activas
    
    def generar_reporte_ingresos_mes(self, mes: int, año: int) -> dict:
        if not (1 <= mes <= 12):
            print("Error: El mes debe estar entre 1 y 12")
            return {}
        
        ingresos_totales = 0.0
        reservas_mes = []
        numero_reservas = 0
        
        for reserva in self.__reservas:
            if (reserva.get_fecha_checkin().month == mes and 
                reserva.get_fecha_checkin().year == año and
                reserva.get_estado() != "cancelada"):
                
                reservas_mes.append(reserva)
                numero_reservas += 1
                ingresos_totales += reserva.get_precio_total()
        
        promedio_por_reserva = ingresos_totales / numero_reservas if numero_reservas > 0 else 0
        
        reporte = {
            "mes": mes,
            "año": año,
            "glamping": self.__nombre,
            "total_reservas": numero_reservas,
            "ingresos_totales": ingresos_totales,
            "promedio_por_reserva": promedio_por_reserva,
            "reservas_detalle": reservas_mes
        }
        
        return reporte
    
    def mostrar_estadisticas_generales(self):
        print(f"\n{'='*50}")
        print(f"ESTADÍSTICAS GENERALES - {self.__nombre}")
        print(f"{'='*50}")
        print(f"Ubicación: {self.__ubicacion}")
        print(f"Total de alojamientos: {len(self.__alojamientos)}")
        print(f"Total de huéspedes registrados: {len(self.__huespedes)}")
        print(f"Total de empleados: {len(self.__empleados)}")
        print(f"Total de reservas históricas: {len(self.__reservas)}")
        print(f"Servicios disponibles: {len(self.__servicios_disponibles)}")
        print(f"Ocupación actual: {self.calcular_ocupacion_actual():.1f}%")
        
        if self.__reservas:
            estados_count = {}
            for reserva in self.__reservas:
                estado = reserva.get_estado()
                estados_count[estado] = estados_count.get(estado, 0) + 1
            
            print(f"\nReservas por estado:")
            for estado, cantidad in estados_count.items():
                print(f"  - {estado.capitalize()}: {cantidad}")
        
        if self.__alojamientos:
            tipos_count = {}
            for alojamiento in self.__alojamientos:
                tipo = alojamiento.get_tipo()
                tipos_count[tipo] = tipos_count.get(tipo, 0) + 1
            
            print(f"\nAlojamientos por tipo:")
            for tipo, cantidad in tipos_count.items():
                print(f"  - {tipo.capitalize()}: {cantidad}")
        
        print(f"{'='*50}")
    
    def listar_alojamientos_disponibles(self):
        print(f"\n--- ALOJAMIENTOS EN {self.__nombre} ---")
        if not self.__alojamientos:
            print("No hay alojamientos registrados")
            return
        
        for alojamiento in self.__alojamientos:
            estado = "DISPONIBLE" if alojamiento.get_disponible() else "OCUPADO"
            print(f"#{alojamiento.get_numero()} - {alojamiento.get_tipo()} - {estado}")
    
    def buscar_servicio_por_nombre(self, nombre_servicio: str):
        for servicio in self.__servicios_disponibles:
            if servicio.get_nombre().lower() == nombre_servicio.lower():
                return servicio
        return None