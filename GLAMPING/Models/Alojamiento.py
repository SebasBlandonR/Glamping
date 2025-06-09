class Alojamiento:
    def __init__(self, numero, tipo, capacidad_maxima, precio_base_noche, amenidades, disponible=True):
        self.__numero = numero 
        tipos_validos = ["cabaña", "domo", "tienda_lujo"]
        if tipo.lower() in tipos_validos:
            self.__tipo = tipo.lower()  
        else:
            raise ValueError(f"Tipo de alojamiento inválido. Debe ser uno de: {', '.join(tipos_validos)}")
        
        self.__capacidad_maxima = capacidad_maxima  
        self.__precio_base_noche = precio_base_noche  
        self.__amenidades = list(amenidades) if amenidades else []  
        self.__disponible = disponible  

    
    def get_numero(self):
        return self.__numero

    def get_tipo(self):
        return self.__tipo

    def get_capacidad_maxima(self):
        return self.__capacidad_maxima

    def get_precio_base_noche(self):
        return self.__precio_base_noche

    def get_amenidades(self):
        return self.__amenidades[:] 

    def is_disponible(self):
        return self.__disponible


    def set_precio_base_noche(self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio_base_noche = nuevo_precio
        else:
            raise ValueError("El precio base de la noche debe ser un valor positivo.")

    def set_disponible(self, estado):
        if isinstance(estado, bool):
            self.__disponible = estado
        else:
            raise ValueError("El estado de disponibilidad debe ser booleano (True/False).")

    def calcular_precio_temporada(self, temporada):
        """
        Calcula el precio de la noche ajustado según la temporada.
        Args:
            temporada (str): La temporada ("alta", "media", "baja").
        Returns:
            float: El precio de la noche ajustado.
        """
        precio_ajustado = self.__precio_base_noche
        if temporada.lower() == "alta":
            precio_ajustado *= 1.25 
        elif temporada.lower() == "media":
            precio_ajustado *= 1.10  
        elif temporada.lower() == "baja":
            precio_ajustado *= 0.85 
        else:
            print("Advertencia: Temporada no reconocida. Se usará el precio base.")
        return precio_ajustado

    def reservar(self):
        """Cambia el estado de disponibilidad del alojamiento a False."""
        if self.__disponible:
            self.__disponible = False
            print(f"Alojamiento {self.__numero} ({self.__tipo}) reservado exitosamente.")
            return True
        else:
            print(f"Alojamiento {self.__numero} ({self.__tipo}) ya está reservado.")
            return False

    def liberar(self):
        """Cambia el estado de disponibilidad del alojamiento a True."""
        if not self.__disponible:
            self.__disponible = True
            print(f"Alojamiento {self.__numero} ({self.__tipo}) liberado exitosamente.")
            return True
        else:
            print(f"Alojamiento {self.__numero} ({self.__tipo}) ya está libre.")
            return False

    def mostrar_info(self):
        """Muestra la información detallada del alojamiento."""
        print(f"--- Información del Alojamiento {self.__numero} ---")
        print(f"Tipo: {self.__tipo.capitalize()}")
        print(f"Capacidad Máxima: {self.__capacidad_maxima} personas")
        print(f"Precio Base por Noche: ${self.__precio_base_noche:,.2f}")
        print(f"Amenidades: {', '.join(self.__amenidades) if self.__amenidades else 'Ninguna'}")
        estado_disponibilidad = "Disponible" if self.__disponible else "Reservado"
        print(f"Estado: {estado_disponibilidad}")
        print("-" * 35)


        
print("--- Creación y Mostrar Información de Alojamientos ---")
try:
    cabaña1 = Alojamiento(101, "cabaña", 4, 150000, ["wifi", "chimenea", "jacuzzi"])
    domo1 = Alojamiento(201, "domo", 2, 100000, ["wifi", "vista_panorámica"])
    tienda_lujo1 = Alojamiento(301, "tienda_lujo", 2, 80000, ["wifi", "iluminación_ambiente"], disponible=False)

    cabaña1.mostrar_info()
    domo1.mostrar_info()
    tienda_lujo1.mostrar_info()

except ValueError as e:
    print(f"\nError al crear alojamiento: {e}")

print("\n--- Demostración de Getters y Setters ---")
print(f"Precio base de la cabaña 101: ${cabaña1.get_precio_base_noche():,.2f}")
cabaña1.set_precio_base_noche(160000)
print(f"Nuevo precio base de la cabaña 101: ${cabaña1.get_precio_base_noche():,.2f}")

print(f"¿Domo 201 disponible? {domo1.is_disponible()}")
domo1.set_disponible(False)
print(f"¿Domo 201 disponible después de setter? {domo1.is_disponible()}")
domo1.set_disponible(True) 

print("\n--- Cálculo de Precio por Temporada ---")
print(f"Precio cabaña 101 en temporada alta: ${cabaña1.calcular_precio_temporada('alta'):,.2f}")
print(f"Precio domo 201 en temporada baja: ${domo1.calcular_precio_temporada('baja'):,.2f}")
print(f"Precio tienda de lujo 301 en temporada media: ${tienda_lujo1.calcular_precio_temporada('media'):,.2f}")

print("\n--- Demostración de Reservar y Liberar ---")
cabaña1.reservar()
cabaña1.mostrar_info()
cabaña1.reservar()

print("-" * 35)

tienda_lujo1.liberar()
tienda_lujo1.mostrar_info()
tienda_lujo1.liberar() 