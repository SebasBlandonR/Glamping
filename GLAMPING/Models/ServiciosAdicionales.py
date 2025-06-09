class ServicioAdicional:
    def __init__(self, nombre: str, descripcion: str, precio: float, duracion_horas: float):
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__precio = precio
        self.__duracion_horas = duracion_horas

   
    def get_nombre(self) -> str:
        return self.__nombre

    def get_descripcion(self) -> str:
        return self.__descripcion

    def get_precio(self) -> float:
        return self.__precio

    def get_duracion_horas(self) -> float:
        return self.__duracion_horas

    def set_nombre(self, nuevo_nombre: str):
        self.__nombre = nuevo_nombre

    def set_descripcion(self, nueva_descripcion: str):
        self.__descripcion = nueva_descripcion

    def set_precio(self, nuevo_precio: float):
        if nuevo_precio >= 0:
            self.__precio = nuevo_precio
        else:
            raise ValueError("El precio no puede ser negativo")

    def set_duracion_horas(self, nueva_duracion: float):
        if nueva_duracion > 0:
            self.__duracion_horas = nueva_duracion
        else:
            raise ValueError("La duración debe ser mayor a 0 horas")

    def mostrar_info(self) -> str:
        info = (f"Servicio: {self.__nombre}\n"
                f"Descripción: {self.__descripcion}\n"
                f"Precio: ${self.__precio:.2f}\n"
                f"Duración: {self.__duracion_horas} horas")
        return info