class Persona:
    def __init__(self, run, nombre, apellido):
        self.__run = run
        self.__nombre = nombre
        self.__apellido = apellido

    def get_run(self):
        return self.__run
    
    def get_nombre(self):
        return self.__nombre
    
    def get_apellido(self):
        return self.__apellido
    
    def set_nombre(self, nombre):
        self.__nombre = nombre
    
    def set_apellido(self, apellido):
        self.__apellido = apellido
    
    def __str__(self):
        return f"RUN: {self.__run}, Nombre: {self.__nombre}, Apellido: {self.__apellido}"
    
    