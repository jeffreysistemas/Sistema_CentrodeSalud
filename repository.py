from models import Paciente, Medico, CitaMedica

class CentroSaludRepository:
    _instance = None


    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CentroSaludRepository, cls).__new__(cls)
            cls._instance.pacientes = []
            cls._instance.medicos = []
            cls._instance.citas = []
            cls._instance._cargar_datos_iniciales()
        return cls._instance
    
    def _cargar_datos_iniciales(self):

        medico1 = Medico("45678912", "Carlos Pérez", 42, "CMP-12345", "Medicina General")
        medico2 = Medico("12345678", "María Gómez", 38, "CMP-67890", "Pediatría")
        self.medicos.extend([medico1, medico2])


        paciente1 = Paciente("87654321", "Juan Quispe", 25, "HC-001", "Ninguno")
        self.pacientes.append(paciente1)

    def agregar_paciente(self, paciente: Paciente) -> bool:
        self.pacientes.append(paciente)
        return True

    def buscar_paciente(self, dni: str) -> Paciente | None:
        for p in self.pacientes:
            if p.dni == dni:
                return p
        return None

    def agregar_medico(self, medico: Medico) -> bool:
        self.medicos.append(medico)
        return True

    def buscar_medico(self, cmp: str) -> Medico | None:
        for m in self.medicos:
            if m.cmp == cmp:
                return m
        return None

    def programar_cita(self, cita: CitaMedica) -> bool:
        self.citas.append(cita)
        return True





