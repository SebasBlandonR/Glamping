class Persona:
    def __init__(self, nombre, telefono, email, identificacion):
        self.__nombre = nombre
        self.__telefono = telefono
        self.__email = email
        self.__identificacion = identificacion

    def get_nombre(self):
        return self.__nombre

    def get_telefono(self):
        return self.__telefono

    def get_email(self):
        return self.__email

    def get_identificacion(self):
        return self.__identificacion

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_telefono(self, telefono):
        self.__telefono = telefono

    def set_email(self, email):
        self.__email = email

    def set_identificacion(self, identificacion):
        self.__identificacion = identificacion

    def mostrar_info(self):
        return f"Nombre: {self.__nombre}, Teléfono: {self.__telefono}, Email: {self.__email}, ID: {self.__identificacion}"
