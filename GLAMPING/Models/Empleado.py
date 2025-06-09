from datetime import date

class Persona:
    def __init__(self, nombre, edad, identificacion):
        self.__nombre = nombre  
        self.__edad = edad      
        self.__identificacion = identificacion

   
    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    def get_identificacion(self):
        return self.__identificacion

    def mostrar_info(self):
        print(f"Nombre: {self.__nombre}")
        print(f"Edad: {self.__edad}")
        print(f"Identificación: {self.__identificacion}")

class Empleado(Persona):
    def __init__(self, nombre, edad, identificacion, cargo, salario, fecha_ingreso):
        super().__init__(nombre, edad, identificacion)
        self.__cargo = cargo          
        self.__salario = salario      
      
        if isinstance(fecha_ingreso, date):
            self.__fecha_ingreso = fecha_ingreso
        else:
            raise ValueError("fecha_ingreso debe ser un objeto date.")

    def get_cargo(self):
        return self.__cargo

    def get_salario(self):
        return self.__salario

    def get_fecha_ingreso(self):
        return self.__fecha_ingreso

    def calcular_antiguedad(self):
        hoy = date.today()
        antiguedad = hoy.year - self.__fecha_ingreso.year - \
                     ((hoy.month, hoy.day) < (self.__fecha_ingreso.month, self.__fecha_ingreso.day))
        return antiguedad

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Cargo: {self.__cargo}")
        print(f"Salario: ${self.__salario:,.2f}")
        print(f"Fecha de Ingreso: {self.__fecha_ingreso.strftime('%d/%m/%Y')}")
        print(f"Antigüedad: {self.calcular_antiguedad()} años")



print("--- Creación de Objetos ---")

persona1 = Persona("Ana López", 30, "123456789")
persona1.mostrar_info()
print("-" * 30)


empleado1 = Empleado("Carlos Ruiz", 45, "987654321", "Gerente de Proyectos", 7500000, date(2018, 5, 15))
empleado1.mostrar_info()
print("-" * 30)

print("\n--- Encapsulamiento (acceso a atributos privados mediante métodos) ---")

print(f"Nombre de la persona : {persona1.get_nombre()}")
print(f"Salario del empleado : ${empleado1.get_salario():,.2f}")
print("-" * 30)

print("\n--- Herencia ---")
print("Empleado hereda de Persona, por lo que tiene los atributos y métodos de Persona,")
print("además de los suyos propios.")
print(f"El empleado '{empleado1.get_nombre()}' tiene la identificación '{empleado1.get_identificacion()}'.")
print("-" * 30)

print("\n--- Polimorfismo ---")


persona1.mostrar_info()
print("-" * 30)
empleado1.mostrar_info()
print("-" * 30)

print(f"Años de servicio de {empleado1.get_nombre()}: {empleado1.calcular_antiguedad()} años.")
print("-" * 30)