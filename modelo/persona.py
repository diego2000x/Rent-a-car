class Persona:
    def __init__(self, run, nombre, apellido):
        self._run = run
        self._nombre = nombre
        self._apellido = apellido

    # Getters y Setters básicos
    def getRun(self): return self._run
    def getNombre(self): return self._nombre
    def getApellido(self): return self._apellido
    
    def __str__(self):
        return f"{self._run} - {self._nombre} {self._apellido}"