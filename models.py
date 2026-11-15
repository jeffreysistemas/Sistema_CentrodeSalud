from abc import ABC, abstractmethod

class persona(ABC):
    def __init__(self, dni: str , nombre: str , edad: int):
        self._dni = dni
        self._nombre = nombre
        self._edad = edad

    @property
    def dni(self) -> str:
        return self._dni

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def edad(self) -> int:
        return self._edad

    @abstractmethod
    def mostrar_info(self) -> None:
        pass


class Paciente(Persona):
    def __init__(self, dni: str, nombre: str, edad: int, historia_clinica: str, antecedentes: str):
        super().__init__(dni, nombre, edad)
        self.historia_clinica = historia_clinica
        self.antecedentes = antecedentes

    def mostrar_info(self) -> None:
        print(f"[PACIENTE] H.C: {self.historia_clinica} | Nombre: {self.nombre} | Edad: {self.edad} | DNI: {self.dni}")

class Medico(Persona):
    def __init__(self, dni: str, nombre: str, edad: int, cmp: str, especialidad: str):
        super().__init__(dni, nombre, edad)
        self._cmp = cmp
        self._especialidad = especialidad

    @property
    def cmp(self) -> str:
        return self._cmp

    @property
    def especialidad(self) -> str:
        return self._especialidad

    def mostrar_info(self) -> None:
        print(f"[MÉDICO] CMP: {self._cmp} | Dr(a). {self.nombre} | Especialidad: {self._especialidad}")

    def consultar_disponibilidad(self) -> bool:
        return True

class CitaMedica:
    def __init__(self, fecha: str, hora: str, paciente: Paciente, medico: Medico, estado: str = "PROGRAMADA"):
        self._fecha = fecha
        self._hora = hora
        self._paciente = paciente
        self._medico = medico
        self._estado = estado
    @property
    def fecha(self) -> str:
        return self._fecha

    @property
    def hora(self) -> str:
        return self._hora

    @property
    def estado(self) -> str:
        return self._estado

    @estado.setter
    def estado(self, nuevo_estado: str):
        self._estado = nuevo_estado

    def mostrar_detalles(self) -> None:
        print(f"Cita -> Fecha: {self._fecha} [{self._hora}] | Paciente: {self._paciente.nombre} | Médico: Dr(a). {self._medico.nombre} | Estado: {self._estado}")